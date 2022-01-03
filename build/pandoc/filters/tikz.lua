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
    \usetikzlibrary{positioning}
    \usetikzlibrary{arrows,snakes,shapes,fadings}
    \usepackage{fontspec}
    \setmainfont{Roboto}[
      Extension = .otf,
      UprightFont = *-Regular,
      BoldFont = *-Bold,
      ItalicFont = *-Italic,
      BoldItalicFont = *-BoldItalic,
    ]    \usepackage{etoolbox} 
    
    \newcommand{\figwidth}{16cm} 
    \newcommand{\figheight}{10cm} 
    \newcommand{\fontselect}{\large\bf} 
    
    \tikzset{
      labelNode/.style={anchor=south east, above left=0cm and 0cm of anchor, font=\fontselect}, 
      redAnchorNode/.style={anchor=center, left=-0.1cm of anchor, circle, fill=red, minimum size=0.2cm}, 
      graphicNode/.style={anchor=north west, below right=0cm and 0cm of anchor}, 
    }
    
    \newtoggle{draft}
        \toggletrue{draft}
        %% \togglefalse{draft} 
    
    \begin{document}
    \begin{tikzpicture}[every node/.style={inner sep=0pt}]
    
    \iftoggle{draft}{\node[anchor=south west, rectangle, draw, red, line width=2pt, minimum width=\figwidth, minimum height=\figheight] at (0,0) {};}
    {\node[anchor=south west, rectangle, fill=white, minimum width=\figwidth, minimum height=\figheight] at (0,0) {};};
     
    %s
    \end{tikzpicture}
    \end{document}
]]

local function tikz2image(src, filetype, outfile)
    local f = io.open('tikz.tex', 'w')
    f:write(tikz_doc_template:format(src))
    f:close()
    os.execute('tectonic tikz.tex')
    if filetype == 'pdf' then
        os.rename('tikz.pdf', outfile)
    else
        os.execute('pdf2svg tikz.pdf ' .. outfile)
        os.rename('tikz.pdf', outfile .. '.pdf')
        print(outfile)
    end
    -- os.remove('tikz.tex')
end

extension_for = {
  html = 'svg',
  html4 = 'svg',
  html5 = 'svg',
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
  if para.content[1].t == "Image" then

    return pandoc.Para({pandoc.Image(para.content[1].caption,'output/figures/' .. para.content[1].src .. '.' .. extension_for[FORMAT])})
  else
    return para
  end
end


function Block(bl)
  if bl and bl.t == "CodeBlock" then
    if bl.attr.classes[1] == 'tikz-figure' then
      local filetype = extension_for[FORMAT] or 'svg'
      local fbasename = '/output/figures/' .. bl.identifier .. '.' .. filetype
      local fname = system.get_working_directory() .. fbasename
      tikz2image(bl.text, filetype, fname)
      
      return pandoc.Null()
    
    end
  end
  
end