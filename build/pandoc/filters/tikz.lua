-- Modified from https://pandoc.org/lua-filters.html#building-images-with-tikz

-- This template will help you create multi-panel figures for publication. A detailed description is provided on my blog: 
    -- https://shannonmlocke.wordpress.com/2021/01/15/create-multipanel-figures-in-latex/
    --
    -- Created by Shannon Marie Locke, Jan 2019.
    -- Edited by SML, Jan 2020 - added custom nodes.

local system = require 'pandoc.system'

local tikz_doc_template = [[
    \documentclass[tikz,border=0cm]{standalone}
    \usepackage{graphicx}
    \usepackage{tikz}
    \usepackage{contour}
    \contourlength{0.6pt}
    \usetikzlibrary{positioning}
    \usetikzlibrary{arrows,snakes,shapes,fadings}
    \usetikzlibrary{fit}
    \usetikzlibrary{calc}
    \def\centerarc[#1](#2)(#3:#4:#5){ \draw[#1] ($(#2)+({#5*cos(#3)},{#5*sin(#3)})$) arc (#3:#4:#5); }
    \usetikzlibrary{3d}
    \usetikzlibrary{backgrounds}
    \usepackage{fontspec}
    \setmainfont{Roboto}[
      Extension = .otf,
      UprightFont = *-Regular,
      BoldFont = *-Bold,
      ItalicFont = *-Italic,
      BoldItalicFont = *-BoldItalic,
    ]    \usepackage{etoolbox} 
    \usepackage{enumitem}
    \setlist{nosep,leftmargin=*}
    \newcommand{\figwidth}{%s} 
    \newcommand{\figheight}{%s} 
    \newcommand{\fontselect}{\large\bf} 
    \newcommand{\fontannot}{\bf} 
    
    \tikzset{
      labelNode/.style={anchor=south east, above left=0cm and 0cm of anchor, font=\fontselect}, 
      annotNode/.style={anchor=center, font=\fontannot},
      redAnchorNode/.style={anchor=center, left=-0.1cm of anchor, circle, fill=red, minimum size=0.2cm}, 
      graphicNode/.style={anchor=north west, below right=0cm and 0cm of anchor}, 
      mnNode/.style={below left=0.1cm and 0cm of rect.south east, font=\fontannot},
      block/.style = {rectangle, draw, fill=gray!20, text width=12em, text centered, rounded corners, minimum height=2em,inner sep=0.5em},
      line/.style = {draw, -latex'}
    }
    
    \newtoggle{draft}
     \toggle%s{draft}
     %%\togglefalse{draft} 
    
    \begin{document}
    \begin{tikzpicture}[
      every node/.style={inner sep=0pt},
      box/.style = {draw=#1, line width=0.8mm,inner sep=0.0mm}
    ]
    
    \iftoggle{draft}{\node[anchor=south west, rectangle, draw, red, line width=2pt, minimum width=\figwidth, minimum height=\figheight] at (0,0) {};}
    {
      \begin{scope}[on background layer]

      \node[anchor=south west, rectangle, fill=white, minimum width=\figwidth, minimum height=\figheight] at (0,0) {};
      \end{scope}
    };
     
    %s
    \iftoggle{draft}{\draw[lightgray,step=1] (0,0) grid (\figwidth,\figheight);}{};
    \end{tikzpicture}
    \end{document}
]]

local function get_file_name(file)
  local file_name = file:match("[^/]*$")
  return file_name
end


local function tikz2image(width,height,draft,src, filetype, outfile)
    local f = io.open(get_file_name(outfile) .. '.tex', 'w')
    f:write(tikz_doc_template:format(width,height,draft,src))
    f:close()
    os.execute('tectonic ' .. get_file_name(outfile) .. '.tex')
    if filetype == 'pdf' then
        os.rename(get_file_name(outfile) .. '.pdf', outfile)
    else
        os.execute('pdf2svg ' .. get_file_name(outfile) .. '.pdf '  .. outfile .. '.svg')
        os.rename(get_file_name(outfile) .. '.pdf', outfile .. '.pdf')
        os.execute('convert -density 200 '.. outfile .. '.pdf' .. ' -background white -alpha remove ' .. outfile .. '.png')
        
        print(outfile)
    end
    os.rename(get_file_name(outfile) .. '.tex', outfile .. '.tex')
end

extension_for = {
  html = 'svg',
  html4 = 'svg',
  html5 = 'svg',
  markdown = 'svg',
  latex = 'pdf',
  beamer = 'pdf' }

local function file_exists(name)
  local f = io.open(name, 'r')
  if f ~= nil then
    io.close(f)
    return true
  else
    return false
  end
end

local function starts_with(start, str)
  return str:sub(1, #start) == start
end


function Para(para)
  if para.content[1].t == "Image" and string.match(para.content[1].src, "tikz:") then
    new_path = 'figures/' .. string.sub(para.content[1].src,6) .. '.png' 
    para.content[1].src = new_path
    return para
  else
    return para
  end
end


function Block(bl)
  if bl and bl.t == "CodeBlock" then
    if bl.attr.classes[1] == 'tikz-figure' then
      local filetype = extension_for[FORMAT] or 'svg'
      local fbasename = '/output/figures/' .. bl.identifier 
      local fname = system.get_working_directory() .. fbasename
      tikz2image(bl.attr.attributes['width'],bl.attr.attributes['height'],bl.attr.attributes['draft'],bl.text, filetype, fname)
      
      return pandoc.Null()
    
    end
  end
  
end