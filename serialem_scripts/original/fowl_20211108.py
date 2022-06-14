import numpy as np
import glob
import time
import os
import math
import matplotlib.pyplot as plt
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import json
from pathlib import Path

import sys
sys.path.insert(0, 'C:\Program Files\SerialEM\PythonModules')
import serialem

# TODO:
#    - Switch to no tilt angles (X)
#    - Read form spceific Navigator item (x)
#    - Calibration images better chosen (x)
#    - Write grid manager
#    - Write inital alignment
#    - Extrapolate calibration (x)     
#    - Graceful stop (now will always extrapolate )
#    - Save view image (x)
#   


class fowl_session:
    def __init__(self,name,directory,load_from_file=False):
        self.state = {}
        self.name = name
        self.directory = directory

        self.state["grids"] = []
        self.state["microscope_settings"] = {}

    def write_to_disk(self):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        filename = f"{self.name}_{timestr}.npy"
        filename = os.path.join(self.directory, filename)
        np.save(filename, self.state)
   
    def load_from_disk(self):
        potential_files = glob.glob(os.path.join(
            self.directory, self.name+"_*.npy"))
        if len(potential_files) < 1:
            raise(FileNotFoundError("Couldn't find saved files"))
        most_recent = sorted(potential_files)[-1]
        print(f"Loading file {most_recent}")
        self.state = np.load(most_recent, allow_pickle=True).item()
    def add_current_setting(self, name, fringe_free=False):

        settings = {}
        settings["magnification"] = serialem.ReportMag()
        settings["magnification_index"] = serialem.ReportMagIndex()
        settings["spot_size"] = serialem.ReportSpotSize()
        settings["illuminated_area"] = serialem.ReportIlluminatedArea()
        settings["beam_tilt"] = serialem.ReportBeamTilt()
        settings["objective_stigmator"] = serialem.ReportObjectiveStigmator()
        settings["fringe_free"] = fringe_free

        if fringe_free:
            settings["fringe_free_nominal_defocus_c2aperture"] = serialem.ReportDefocus()
            settings["fringe_free_stage_z_diff"] = serialem.ReportStageXYZ()[2] - self.eucentric_z

        self.state["microscope_settings"][name] = settings


    def focus_sample_by_stage_movement(self,defocus=-5):
        self.eucentric_z = serialem.ReportStageXYZ()[2]
        serialem.MoveStage(0,0,30)
        repeats = 0
        while repeats < 20:
            repeats += 1 
            serialem.Preview()
            ctf_results = serialem.CtfFind('A',-0.2,-20)
            shift = defocus-ctf_results[0]
            serialem.MoveStage(0,0,shift)
    

class fowl_grid:
    def __init__(self,name,directory,beam_radius,load_from_file=False, defocus=-5.0,start_from=0.0, numtilts=41, tiltstep=3.0):
        self.state = {}
        self.name = name
        self.directory = directory
        Path(directory).mkdir(parents=True, exist_ok=True)

        self.state["acquisition_areas"] = []

    def write_to_disk(self):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        filename = f"{self.name}_{timestr}.npy"
        filename = os.path.join(self.directory, filename)
        np.save(filename, self.state)
   
    def load_from_disk(self):
        potential_files = glob.glob(os.path.join(
            self.directory, self.name+"_*.npy"))
        if len(potential_files) < 1:
            raise(FileNotFoundError("Couldn't find saved files"))
        most_recent = sorted(potential_files)[-1]
        print(f"Loading file {most_recent}")
        self.state = np.load(most_recent, allow_pickle=True).item()
    
    def initialize_area_template_matching(self):
        for lamella in self.state["acquisition_areas"]:
            lamella.calculate_acquisition_positions(expansion=1.0)
            lamella.designate_calibration_positions()
            lamella.plot_acquisition_positions()
            lamella.write_to_disk()
    
    def collect_areas_template_matching(self):
        for lamella in self.state["acquisition_areas"]:
            fowl.serialem.LongOperation("Da","2")
            fowl.serialem.SetFolderForFrames(os.path.join(os.path.abspath(lamella.directory),"frames/"))
            fowl.serialem.GoToLowDoseArea('V')
            fowl.serialem.SetDefocus(-20)
            lamella.move_to_position()
            fowl.serialem.GoToLowDoseArea('R')
            fowl.serialem.SetDefocus(0)
            fowl.serialem.ManageDewarsAndPumps(-1)
            while fowl.serialem.AreDewarsFilling():
                time.sleep(60)
            lamella.acquire_single_tilt_slow(tilt=-15.0)
            lamella.write_to_disk()


class fowl_acquisition_area:

    def __init__(self, name, directory, beam_radius, load_from_file=False, defocus=-5.0, start_from=0.0, numtilts=41, tiltstep=3.0, exposure_time=0.5):

        self.state = {}
        self.name = name
        self.directory = directory
        Path(directory).mkdir(parents=True, exist_ok=True)
        self.frames_directory = os.path.join(directory,"frames")
        Path(self.frames_directory).mkdir(parents=True, exist_ok=True)
        self.images ={} 

        if load_from_file:
            self.load_from_disk()
        else:
            self.state["beam_radius"] = beam_radius
            self.state["exposure_time"] = exposure_time
            self.state["desired_defocus"] = defocus

            self.state["stage_position"] = None
            self.state["corner_positions_specimen"] = None
            self.state["corner_positions_stage_diff"] = None
            self.state["corner_positions_stage_absolute"] = None
            self.state["corner_positions_image"] = None
            self.state["view_stage_to_specimen"] = None
            self.state["view_specimen_to_camera"] = None
            self.state["record_speciment_to_camera"] = None
            self.state["record_IS_to_camera"] = None
            self.state["count_threshold_for_beamshift"]=1000
            # Array (n,2) of speciment coordinates to be acquired
            self.state["acquisition_positions"] = None

            # Directory key: tilt angle, valeu array (bool,n) indicating of position acquired
            self.state["positions_acquired"] = {}

            # list containing indices to acquisition_positions that will be used to calibrate defocus
            self.state["calibration_positions"] = []

            # Directory, key: "tilt", value {directory: defocus_measures, absolute_defocus, score, resolution}
            self.state["defocus_calibrations"] = {}

            # List of tilts
            self.state["tilts"] = []
            self.state["tilts"].append(start_from)
            for i in range(numtilts-1):
                value = (((i % 3)) + 1) + ((i // 6)) * 3.0
                value = math.copysign(value, (i % 6) - 3)
                self.state["tilts"].append(start_from + value * tiltstep)
            self.state["tilts"] = np.array(self.state["tilts"])
            # Directory, key: tilt angle, value: direcotry, keys("list of positions","filename")
            self.state["fast_acquisitions"] = {}
            # self.write_to_disk()
            self.view_images = {}

    def write_to_disk(self):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        filename = f"{self.name}_{timestr}.npy"
        filename = os.path.join(self.directory, filename)
        np.save(filename, self.state)
    
    def save_images(self):
        filename = f"{self.name}-images.npy"
        filename = os.path.join(self.directory, filename)
        np.save(filename, self.images)

    def load_images(self):
        filename = f"{self.name}-images.npy"
        filename = os.path.join(self.directory, filename)
        self.images = np.load(filename, allow_pickle=True).item()

    def load_from_disk(self):
        potential_files = glob.glob(os.path.join(
            self.directory, self.name+"_*.npy"))
        if len(potential_files) < 1:
            raise(FileNotFoundError("Couldn't find saved files"))
        most_recent = sorted(potential_files)[-1]
        print(f"Loading file {most_recent}")
        self.state = np.load(most_recent, allow_pickle=True).item()

    def initialize_from_navigator(self,item=None):
        if item is None:
            (index, x, y, z, t) = serialem.ReportNavItem()
        else:
            (index, x, y, z, t) = serialem.ReportOtherItem(item)
        self.state["stage_position"] = np.array([x, y, z])
        self.state["navigator_index"] = index
        serialem.LoadOtherMap(int(index),"K")
        view_image = np.asarray(serialem.bufferImage("K"))
        self.images[self.state["tilts"][0]] = view_image
        self.save_images()
        corner_coordinates_stage = []
        corner_coordinates_stage_diff = []
        corner_coordinates_specimen = []
        corner_coordinates_image = []
        for i in range(4):
            (ci, cx, cy, cz, ct) = serialem.ReportOtherItem(i + int(index)+1)
            corner_coordinates_stage.append((cx, cy))
            dx = cx - x
            dy = cy - y
            corner_coordinates_stage_diff.append((dx, dy))
            serialem.ImageShiftByStageDiff(dx, dy)
            corner_coordinates_specimen.append(serialem.ReportSpecimenShift())
            serialem.SetImageShift(0, 0)
            corner_coordinates_image.append(serialem.ReportItemImageCoords(i + int(index)+1,"K") )
        self.state["corner_positions_specimen"] = np.array(
            corner_coordinates_specimen)
        self.state["corner_positions_stage_diff"] = np.array(
            corner_coordinates_stage_diff)
        self.state["corner_positions_stage_absolute"] = np.array(
            corner_coordinates_stage)
        self.state["corner_positions_image"] = np.array(
            corner_coordinates_image)
        serialem.GoToLowDoseArea("V")
        # Use ReportItemImageCoordinates to calculate ScaleMat
        self.state["view_stage_to_specimen"] = np.array(
            serialem.StageToSpecimenMatrix(0))
        self.state["view_specimen_to_camera"] = np.array(
            serialem.SpecimenToCameraMatrix(0))
        serialem.GoToLowDoseArea("R")
        self.state["record_speciment_to_camera"] = np.array(
            serialem.SpecimenToCameraMatrix(0))
        self.state["record_IS_to_camera"] = np.array(
            serialem.ISToCameraMatrix(0))

    def calculate_acquisition_positions(self, direction=1, rotation_direction=1, expansion=1.1, add_overlap=0.05):

        top_left = self.state["corner_positions_specimen"][0] * expansion
        top_right = self.state["corner_positions_specimen"][1] * expansion
        bottom_right = self.state["corner_positions_specimen"][2] * expansion
        bottom_left = self.state["corner_positions_specimen"][3] * expansion

        square = Polygon([top_left, top_right, bottom_right, bottom_left])
        square = square.buffer(0.001)

        def rotate(p, origin=(0, 0), degrees=0):
            angle = np.deg2rad(degrees)
            R = np.array([[np.cos(angle), -np.sin(angle)],
                          [np.sin(angle),  np.cos(angle)]])
            o = np.atleast_2d(origin)
            p = np.atleast_2d(p)
            return np.squeeze((R @ (p.T-o.T) + o.T).T)

        acquisition_positions = [top_left]
        last_position = top_left
        cont = True
        counter = 0
        tcounter = 0
        rcounter = 0

        line_vector = (1-add_overlap) * 2 * ((top_right - top_left) / np.linalg.norm(
            top_right - top_left)) * self.state["beam_radius"] * np.cos(30*np.pi/180)

        while cont:
            new_position = last_position + line_vector * direction
            if square.contains(Point(new_position)):
                acquisition_positions.append(new_position)
                counter += 1
                rcounter = 0
            else:
                if np.linalg.norm(new_position - acquisition_positions[-1]) < 5.0:
                    tcounter += 1
                else:
                    # New row
                    # p1 = rotate(line_vector,degrees = 60)
                    p2 = rotate(line_vector, degrees=360 -
                                rotation_direction * 60 * direction)
                    # acquisition_positions.append(last_position + p1 * direction)
                    new_position = last_position + p2 * direction
                    if square.contains(Point(new_position)):
                        acquisition_positions.append(new_position)
                        counter += 1
                    direction *= -1

                    tcounter += 1
                    if tcounter > 1800:
                        cont = False
            last_position = new_position
        self.state["acquisition_positions"] = np.array(acquisition_positions)
        for tilt in self.state["tilts"]:
            self.state["positions_acquired"][tilt] = np.zeros(
                (self.state["acquisition_positions"].shape[0]), dtype='bool')

    def plot_acquisition_positions(self):
        top_left = self.state["corner_positions_specimen"][0]
        top_right = self.state["corner_positions_specimen"][1] 
        bottom_right = self.state["corner_positions_specimen"][2] 
        bottom_left = self.state["corner_positions_specimen"][3] 

        msquare = np.array([top_left, top_right, bottom_right, bottom_left])

        line = plt.Polygon(msquare, closed=True, fill=None, edgecolor='r')
        plt.axes()
        plt.gca().add_patch(line)
        for i, ap in enumerate(self.state["acquisition_positions"]):
            if i in self.state["calibration_positions"]:
                color = "r"
            else:
                color = "b"
            circle = plt.Circle(
                ap, radius=self.state["beam_radius"], fill=None, edgecolor=color)
            plt.gca().add_patch(circle)
        plt.axis('scaled')
        fig = plt.gcf()
        fig.set_size_inches(18.5, 10.5)
        plt.show()

    def designate_calibration_positions(self, num=10):
        from sklearn.cluster import KMeans

        kmeans = KMeans(n_clusters=num, random_state=0).fit(self.state["acquisition_positions"])
        self.state["calibration_positions"] = []
        
        for cluster in kmeans.cluster_centers_:
            closest_point_index = min(range(
                len(self.state["acquisition_positions"])), key=lambda i: abs(np.linalg.norm(self.state["acquisition_positions"][i]-cluster)))
            self.state["calibration_positions"].append(closest_point_index)
        self.state["calibration_positions"] = np.array(self.state["calibration_positions"])
    
    def move_to_position(self):
        serialem.RealignToOtherItem(int(self.state["navigator_index"]),0,0,0.05,4,1)


    def extrapolate_defocus_calibration(self, tilt, plot_diagnostics=False):
        existing_calibrations = list(
                [tilt for tilt in self.state["defocus_calibrations"].keys()
                    if "fit" in self.state["defocus_calibrations"][tilt] and
                    self.state["defocus_calibrations"][tilt]["fit"][3] > 0.5])
        if tilt in self.state["defocus_calibrations"] and "fit" in self.state["defocus_calibrations"][tilt] and self.state["defocus_calibrations"][tilt]["fit"][3] > 0.5:
            print(f"Experimental fit exists, extrapolation unnescessary")
            return(self.state["defocus_calibrations"][tilt]["fit"])
        if len([tilts for tilts in self.state["defocus_calibrations"] if "fit" in self.state["defocus_calibrations"][tilts] and self.state["defocus_calibrations"][tilts]["fit"][3] > 0.5]) < 9:
            
            closest_calibration_tilt = existing_calibrations[min(range(
                len(existing_calibrations)), key=lambda i: abs(existing_calibrations[i]-tilt))]
            print(
                f"Calibrating, starting from calibration at tilt {closest_calibration_tilt}")
            closest_calibration = self.state["defocus_calibrations"][closest_calibration_tilt]
            return(closest_calibration)
        
        closest_calibration_tilts = np.array(sorted([existing_calibrations[i] for i in sorted(range(len(existing_calibrations)), key=lambda i: abs(existing_calibrations[i]-tilt))[:9]]))
        print(closest_calibration_tilts)
        x_coeffs = np.array([float(self.state["defocus_calibrations"][tilts]["fit"][0]) for tilts in closest_calibration_tilts])
        y_coeffs = np.array([float(self.state["defocus_calibrations"][tilts]["fit"][1]) for tilts in closest_calibration_tilts])
        height_coeffs = np.array([float(self.state["defocus_calibrations"][tilts]["fit"][2]) for tilts in closest_calibration_tilts])
        x_fit = np.polyfit(closest_calibration_tilts,x_coeffs,1)
        x_func = np.poly1d(x_fit)
        x_extra = x_func(tilt)
        if plot_diagnostics:
            f, axs = plt.subplots(1,3,figsize=(15,5))
            axs[0].plot(closest_calibration_tilts,x_coeffs)
            new_x = np.linspace(-70,70)
            new_y = x_func(new_x)
            axs[0].plot(new_x,new_y,"-")
        
        y_fit = np.polyfit(closest_calibration_tilts,y_coeffs,1)
        y_func = np.poly1d(y_fit)
        y_extra = y_func(tilt)
        if plot_diagnostics:
            axs[1].plot(closest_calibration_tilts,y_coeffs)
            new_x = np.linspace(-70,70)
            new_y = y_func(new_x)
            axs[1].plot(new_x,new_y,"-")

        height_fit = np.polyfit(closest_calibration_tilts,height_coeffs,1)
        height_func = np.poly1d(height_fit)
        height_extra = height_func(tilt)
        if plot_diagnostics:
            axs[2].plot(closest_calibration_tilts,height_coeffs)
            new_x = np.linspace(-70,70)
            new_y = height_func(new_x)
            axs[2].plot(new_x,new_y,"-")
        return({"fit":[x_extra,y_extra,height_extra,0.0]})

        #print(closest_calibrations)


    def acquire_single_tilt_slow(self, tilt):
        serialem.TiltTo(tilt)
        self.state["defocus_calibrations"][tilt] = {}
        self.state["defocus_calibrations"][tilt]["measurements"] = []
        for index in range(len(self.state["acquisition_positions"])):
            if self.state["positions_acquired"][tilt][index]:
                continue
            print(f"Acquiring image {index+1} out of {len(self.state['acquisition_positions'])}")
            serialem.ImageShiftByMicrons(
                self.state["acquisition_positions"][index][0], self.state["acquisition_positions"][index][1])
                
            serialem.ManageDewarsAndPumps(1)
            serialem.Record()
            self.state["positions_acquired"][tilt][index] = True
            counts = serialem.ReportMeanCounts()
            if counts > self.state["count_threshold_for_beamshift"]:
                print(f"Counts high enough {counts} for beamshift correction")
                serialem.CenterBeamFromImage(0,0.4)
            serialem.SetImageShift(0, 0)
            #(defocus, astigmatism, angle, shift, score,
            #    resolution) = serialem.CtfFind("A", -1, -12)
            ctf_results = serialem.CtfFind("A", -0.1, -12)
            self.state["defocus_calibrations"][tilt]["measurements"].append({"defocus": ctf_results[0],
                                                                            "score": ctf_results[4],
                                                                            "fit_resolution": -1,
                                                                            "nominal_defocus": serialem.ReportDefocus(),
                                                                            "specimen_x": self.state["acquisition_positions"][index][0],
                                                                            "specimen_y": self.state["acquisition_positions"][index][1],
                                                                             "beamshift": serialem.ReportBeamShift()
                                                                            })
            
            if ctf_results[4] > 0.07:
                offset = self.state["desired_defocus"] - ctf_results[0]
                serialem.ChangeFocus(offset)
                print(
                    f"Measured defocus of {ctf_results[0]}, adjusting by {offset} to get to { self.state['desired_defocus'] }")
            else:
                print("Unreliable defocus, defocusing by 0.03")
                serialem.ChangeFocus(-0.03)
        

    def perform_defocus_calibration(self, tilt, use_existing_tilt=False):
        if not use_existing_tilt:
            print("Calibrating assuming a flat sample")
        else:
            closest_calibration = self.extrapolate_defocus_calibration(tilt)
        serialem.TiltTo(tilt)
        self.state["defocus_calibrations"][tilt] = {}
        self.state["defocus_calibrations"][tilt]["measurements"] = []
        for index in self.state["calibration_positions"]:
            serialem.ImageShiftByMicrons(
                self.state["acquisition_positions"][index][0], self.state["acquisition_positions"][index][1])
            if use_existing_tilt:
                set_defocus = closest_calibration["fit"][0] * self.state["acquisition_positions"][index][0] + closest_calibration["fit"][1] * \
                    self.state["acquisition_positions"][index][1] + \
                        closest_calibration["fit"][2] + \
                            self.state["desired_defocus"]
                serialem.SetDefocus(set_defocus)
            serialem.ManageDewarsAndPumps(1)
            serialem.Record()
            serialem.ReportMeanCounts()

            serialem.SetImageShift(0, 0)
            #(defocus, astigmatism, angle, shift, score,
            #    resolution) = serialem.CtfFind("A", -1, -12)
            ctf_results = serialem.CtfFind("A", -1, -12)
            self.state["defocus_calibrations"][tilt]["measurements"].append({"defocus": ctf_results[0],
                                                                            "score": ctf_results[4],
                                                                            "fit_resolution": -1,
                                                                            "nominal_defocus": serialem.ReportDefocus(),
                                                                            "specimen_x": self.state["acquisition_positions"][index][0],
                                                                            "specimen_y": self.state["acquisition_positions"][index][1]
                                                                            })
            self.state["positions_acquired"][tilt][index] = True
            if not use_existing_tilt:
                if ctf_results[4] > 0.07:
                    offset = self.state["desired_defocus"] - ctf_results[0]
                    serialem.ChangeFocus(offset)
                    print(
                        f"Measured defocus of {ctf_results[0]}, adjusting by {offset} to get to { self.state['desired_defocus'] }")
                else:
                    print("Unreliable defocus")

    def plot_calibrations(self):
        calibrations = [tilt for tilt in self.state["defocus_calibrations"] if "fit" in self.state["defocus_calibrations"][tilt]]
        calibrations = sorted(calibrations)
        x_tilt = [float(self.state["defocus_calibrations"][tilt]["fit"][0]) for tilt in calibrations]
        y_tilt = [float(self.state["defocus_calibrations"][tilt]["fit"][1]) for tilt in calibrations]
        offset = [float(self.state["defocus_calibrations"][tilt]["fit"][2]) for tilt in calibrations]
        f, axs = plt.subplots(1,3,figsize=(15,5))
        axs[0].plot(calibrations,x_tilt)
        axs[0].set_xlabel("Tilt angle")
        axs[0].set_ylabel("Slope along tilt-axis")
        axs[1].plot(calibrations,y_tilt)
        axs[1].set_xlabel("Tilt angle")
        axs[1].set_ylabel("Slope across tilt-axis")
        axs[2].plot(calibrations,offset)
        axs[2].set_xlabel("Tilt angle")
        axs[2].set_ylabel("Defocus offset")
    
    def plot_defocus_measurements(self,tilts=[-45.0,-15.0,15.0]):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
        for tilt in tilts:
            xs = []
            ys = []
            zs = []
            ws = []
            for i, measurement in enumerate(self.state["defocus_calibrations"][tilt]["measurements"]):
                if measurement["score"] < 0.08:
                    continue
                xs.append(measurement["specimen_x"])
                ys.append(measurement["specimen_y"])
                # zs contains the nominal defocus value at which speciment would be in focus
                zs.append(measurement["nominal_defocus"] - measurement["defocus"])
                ws.append(measurement["score"])
            ax.scatter(xs, ys, zs)
            
        for k,tilt in enumerate(tilts):
            xs = []
            ys = []
            zs = []
            ws = []
            for i, measurement in enumerate(self.state["defocus_calibrations"][tilt]["measurements"]):
                if measurement["score"] < 0.08:
                    continue
                xs.append(measurement["specimen_x"])
                ys.append(measurement["specimen_y"])
                # zs contains the nominal defocus value at which speciment would be in focus
                zs.append(measurement["nominal_defocus"] - measurement["defocus"])
                ws.append(measurement["score"])
            xlim = ax.get_xlim()
            ylim = ax.get_ylim()
            X,Y = np.meshgrid(np.arange(xlim[0], xlim[1]),
                           np.arange(ylim[0], ylim[1]))
            Z = np.zeros(X.shape)
            fit = self.state["defocus_calibrations"][tilt]["fit"]
            for r in range(X.shape[0]):
                for c in range(X.shape[1]):
                    Z[r,c] = fit[0] * X[r,c] + fit[1] * Y[r,c] + fit[2]
            ax.plot_wireframe(X,Y,Z,color=colors[k])

    def analyze_defocus_calibration(self, tilt, minimum_score=0.08, min_measurement=4, extrapolate_distance=10):

        xs = []
        ys = []
        zs = []
        ws = []
        for i, measurement in enumerate(self.state["defocus_calibrations"][tilt]["measurements"]):
            if measurement["score"] < minimum_score:
                continue
            xs.append(measurement["specimen_x"])
            ys.append(measurement["specimen_y"])
            # zs contains the nominal defocus value at which speciment would be in focus
            zs.append(measurement["nominal_defocus"] - measurement["defocus"])
            ws.append(measurement["score"])
        if len(xs) < min_measurement:
            print(f"At tilt {tilt} not sufficent measurements: {len(xs)}. Using extrapolation")
            self.state["defocus_calibrations"][tilt]["fit"] = self.extrapolate_defocus_calibration(tilt)["fit"]
            return()
        print(f"At tilt {tilt} using {len(xs)} measurements")
        # ax.scatter(xs, ys, zs,color=mapper.to_rgba(data["tilts"][ind]))

        tmp_A = []
        tmp_b = []
        tmp_w = []
        for i in range(len(xs)):
            tmp_A.append([xs[i], ys[i], 1])
            tmp_b.append(zs[i])
            tmp_w.append(ws[i])
        weights = np.diag(tmp_w)
        b = np.dot(weights, np.matrix(tmp_b).T)
        A = np.dot(weights,np.matrix(tmp_A))
        fit = (A.T * A).I * A.T * b
        #errors = b - A * fit
        #residual = np.linalg.norm(errors)

        # Or use Scipy
        # from scipy.linalg import lstsq
        # fit, residual, rnk, s = lstsq(A, b)

        print("solution: %f x + %f y + %f = z" % (fit[0], fit[1], fit[2]))
        # Fourth value indicates whether fit is experimental or extrapolated
        self.state["defocus_calibrations"][tilt]["fit"] = [float(fit[0]),float(fit[1]),float(fit[2]),1.0]

        # plot plane
        # xlim = ax.get_xlim()
        # ylim = ax.get_ylim()
        # X,Y = np.meshgrid(np.arange(xlim[0], xlim[1]),
        #                np.arange(ylim[0], ylim[1]))
        # Z = np.zeros(X.shape)
        # for r in range(X.shape[0]):
        #    for c in range(X.shape[1]):
        #        Z[r,c] = fit[0] * X[r,c] + fit[1] * Y[r,c] + fit[2]
        # ax.plot_wireframe(X,Y,Z,color=mapper.to_rgba(data["tilts"][ind]))

    def acquire_data(self, tilt,num_pos=40,only_write=False):
        serialem.TiltTo(tilt)
        set_defocus = self.state["defocus_calibrations"][tilt]["fit"][2]+self.state["desired_defocus"]
        serialem.SetDefocus(set_defocus)
        if tilt not in self.state["fast_acquisitions"]:
            self.state["fast_acquisitions"][tilt] = []
        while sum(np.invert(self.state["positions_acquired"][tilt])) > 0:
            #print(sum(np.invert(self.state["positions_acquired"][tilt])))
            to_acquire = np.argwhere(self.state["positions_acquired"][tilt]==False)
            acquire_now = to_acquire[:num_pos]
            #print(f"Acquiring at indices {acquire_now}")
            tilt_series_commands=[]
            for index in acquire_now:
                index = index[0]
                x = self.state["acquisition_positions"][index][0]
                y = self.state["acquisition_positions"][index][1]
                defocus_offset = self.state["defocus_calibrations"][tilt]["fit"][0] * x + self.state["defocus_calibrations"][tilt]["fit"][1] * y
                tilt_series_commands.append(
                    [self.state["exposure_time"], self.state["exposure_time"]+0.1, defocus_offset, x, y])
            tilt_series_commands=np.array(tilt_series_commands)
            timestr = time.strftime("%Y%m%d-%H%M%S")
            filename = f"command_{self.name}_{timestr}.txt"
            filename = os.path.join(self.directory, filename)
            command_file = os.path.abspath(filename)
            np.savetxt(command_file,tilt_series_commands, fmt = '%.4f')
            if not only_write:
                serialem.ManageDewarsAndPumps(1)
                serialem.CallFunction("40::RunFISE", command_file, (self.state["exposure_time"]+0.15) * len(acquire_now) + 4.0)
                for index in acquire_now:
                    self.state["positions_acquired"][tilt][index] = True
                self.state["fast_acquisitions"][tilt].append({ "positions" : acquire_now, "filename" : serialem.ReportLastFrameFile()})
            else:
                break



#if __name__ == "__main__":
#    test=Spotscanner("test", "./",beam_radius=1.0)
#    print(test.state["tilts"])

