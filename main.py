#!/bin/python3
from subprocess import call

framework_string = r'''\documentclass[border=10pt]{standalone}

\usepackage{tikz}
\usetikzlibrary{timeline,positioning}

\begin{document}

\begin{tikzpicture}
\timeline{5}

\begin{phases}
   \initialphase{involvement degree=3cm}
   \phase{between week=1 and 2 in 0.2,involvement degree=2.25cm,phase color=green}

\end{phases}

\addmilestone{at=phase-0.90,direction=90:1cm,text={Initial meeting},text options={above}}

\end{tikzpicture}

\end{document}
'''

def init_file(name, tex=framework_string):
    
    '''Creates a .tex file which is the basis of the entire timeline. Run only once.'''

    main_file = open(name + '.tex', 'w')
    main_file.write(tex)

def create(name, engine='xelatex'):

    '''Compiles the .tex file into a .pdf using the engine specified in the parameters, then displays it using the evince pdf reader.'''

    call([engine, name + '.tex'])
    call(['evince', name + '.pdf']) # if you want, change 'evince' to the pdf viewer of your choice

def add_phase(start_week, end_week, in_val, string=framework_string, color='red', involvement_degree='2.5cm'):

    new_string = string;

    index = new_string.find('\phase')
    index = new_string[index:].find('\n') + index; # find the next newline after the first phase
    new_string = new_string[:index] + '\n\t' + r'\phase{between week=' + str(start_week) + ' and ' + str(end_week) + ' in ' + str(in_val) + ',involvement degree=' + involvement_degree + ',phase color=' + color + '}\n' + new_string[index:]

    return new_string

if __name__ == '__main__':

    import sys

    name = sys.argv[1]
    tex = add_phase(2,3,0.5,framework_string,'blue','5.6cm')
    tex = add_phase(4,5,0.1,tex,'orange','3cm')


    init_file(name, tex)

    create(name)
