#!/bin/python3
from subprocess import call

framework_string = r'''\documentclass[border=10pt]{standalone}

\usepackage{tikz}
\usetikzlibrary{timeline,positioning}

\begin{document}

\begin{tikzpicture}
\timeline{5}

\begin{phases}
   %\initialphase
   %\phase

\end{phases}

%\addmilestone

\end{tikzpicture}

\end{document}
'''

def init_file(name, tex=framework_string):

    '''Creates a .tex file which is the basis of the entire timeline. Run only once.'''

    main_file = open(name + '.tex', 'w')
    main_file.write(tex)

def create(name, engine='xelatex', remove_tex_file=True):

    '''Compiles the .tex file into a .pdf using the engine specified in the parameters, then displays it using the evince pdf reader.'''

    call([engine, name + '.tex'])
    call(['evince', name + '.pdf']) # if you want, change 'evince' to the pdf viewer of your choice

def add_phase(start_week, end_week, in_val, string=framework_string, color='red', involvement_degree='2.5cm'):

    new_string = string;

    index = new_string.find('\phase')
    index = new_string[index:].find('\n') + index; # find the next newline after the first phase
    new_string = new_string[:index] + '\n\t' + r'\phase{between week=' + str(start_week) + ' and ' + str(end_week) + ' in ' + str(in_val) + ',involvement degree=' + involvement_degree + ',phase color=' + color + '}' + new_string[index:]

    return new_string

def set_interval(interval_length, string=framework_string, custom_interval=False):

    if custom_interval:
        print("Please input your custom interval markers: ")
        next_interval = ''
        custom_intervals = []
        while True:
            next_interval = input()
            if next_interval.lower() == 'done':
                break
            custom_intervals.append(next_interval)
        # replace \timeline
        begin_index = string.find(r'\timeline')
        end_index = begin_index + string[begin_index:].find('\n')

        new_timeline = r'\timeline[custom interval=true]{'
        for item in range(len(custom_intervals)-1):
            new_timeline = new_timeline + custom_intervals[item] + ','
        new_timeline = new_timeline + custom_intervals[len(custom_intervals)-1] + '}\n'

        new_string = string[:begin_index] + new_timeline + string[end_index:]

        # add timespan=[]
        begin_index = new_string.find(r'\begin{tikzpicture}')
        end_index = begin_index + new_string[begin_index:].find('\n')

        new_string = new_string[:begin_index] + r'\begin{tikzpicture}[timespan={}]' + new_string[end_index:]

    else:
        begin_index = string.find(r'\timeline')
        end_index = begin_index + string[begin_index:].find('\n')
        new_timeline = r'\timeline{' + str(interval_length) + '}'

    return new_string

def add_milestone(phase, phase_degree, direction, length, placement, width, text, string=framework_string):

    index = string.find(r'\addmilestone')
    index = index + string[index:].find('\n')

    new_string = string[:index] + '\n' + r'\addmilestone{at=phase-' + str(phase) + '.' + str(phase_degree) + ',direction=' + str(direction) + ':' + str(length) + 'cm,text={' + text + '},text options={' + placement + ',text width=' + str(width)
    new_string = new_string + 'cm}}\n' + string[index:]

    return new_string

if __name__ == '__main__':

    import sys

    # to generate an example timeline
    name = sys.argv[1]
    tex = set_interval(0,framework_string,True)

    tex = add_phase(1,2,0.5,tex,'red','2.5cm')
    tex = add_phase(2,3,0.5,tex,'orange','3.5cm')
    tex = add_phase(3,4,0.5,tex,'yellow','4.5cm')
    tex = add_phase(4,5,0.5,tex,'green','5.6cm')

    tex = add_milestone(2,90,90,2,'above',5,'This is a mason jar containing a last laugh.',tex)

    init_file(name, tex)

    create(name)
