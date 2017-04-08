#!/bin/python3

# TODO 
# redo the entire thing with string formatting
from subprocess import call

class Timeline:
    def __init__(self, name='placeholder'):
        self.string = r"""\documentclass[border=10pt]{standalone}
        \usepackage{tikz}
        \usetikzlibrary{timeline,positioning}
        \begin{document}

        \begin{tikzpicture}
        \timeline{5} % default value for no particular reason

        \begin{phases}
           %\initialphase
           %\phase
        \end{phases}

        %\addmilestone

        \end{tikzpicture}
        \end{document}
        """

        self.name = name
        self.phases = 0

    def set_name(self, name):
        self.name = name

    def create(self, engine='xelatex', remove_tex_file=True):
        """Compiles the .tex file and displays the result with a .pdf viewer. If remove_tex_file is set to false, the .tex file is left intact after compilation; for debugging purposes or advanced users."""

        call([engine, self.name + '.tex'])
        #call(['evince', self.name + '.pdf']) # change evince to pdf viewer of your choice
        call(('convert -density 300 ' + self.name + '.pdf -quality 90 -scale 578x264 ' +\
        self.name + '.png').split(' '))
#       call(('ristretto ' + self.name + '.png').split(' '))

    def init_file(self):
        """Creates the .tex file on first run; writes self.string to it."""

        f = open(self.name + '.tex', 'w')
        f = f.write(self.string)

    def add_phase(self, start_week, end_week, in_val, color='red', degree=2.5):
        """Adds a phase to the timeline. Takes these args:
            Starting week, end week, in_val (which is a value between 0 and 1 which specifies
            where the phase should be placed between the weeks), color, and degree, which is the radius of the phase in centimeters."""

        new_string = self.string
        index = new_string.find('\phase')
        index = new_string[index:].find('\n') + index; # find the next newline after the first phase

        new_string = new_string[:index] + '\n\t' + r'\phase{between week=' + str(start_week) + \
		  ' and ' + str(end_week) + ' in ' + str(in_val) + ',involvement degree=' + str(degree)\
		   + 'cm,phase color=' + color + '}' + new_string[index:]

        self.phases = self.phases + 1
        self.string = new_string

    def _get_custom_intervals():
        print("Please input your interval markers: ")
        custom_intervals = []
        while True:
            next_interval = input()
            if next_interval.lower() == 'done':
                break
            custom_intervals.append(next_interval)
        return custom_intervals

    def set_interval(self, interval_length, custom_interval=False,\
    custom_intervals=[]):
        """Sets the interval markers on the timeline. The default is weeks."""

        if custom_interval:
            # replace \timeline
            begin_index = self.string.find(r'\timeline')
            end_index = begin_index + self.string[begin_index:].find('\n')

            new_timeline = r'\timeline[custom interval=true]{'
            for item in range(len(custom_intervals)-1):
                new_timeline = new_timeline + custom_intervals[item] + ','
            new_timeline = new_timeline + custom_intervals[len(custom_intervals)-1] + '}\n'

            new_string = self.string[:begin_index] + new_timeline + self.string[end_index:]

            # add timespan=[]
            begin_index = new_string.find(r'\begin{tikzpicture}')
            end_index = begin_index + new_string[begin_index:].find('\n')

            new_string = new_string[:begin_index] + r'\begin{tikzpicture}[timespan={}]' + new_string[end_index:]

        else:
            begin_index = self.string.find(r'\timeline')
            end_index = begin_index + self.string[begin_index:].find('\n')
            new_string = self.string[:begin_index] + r'\timeline{' + str(interval_length) + '}' + \
            self.string[end_index:]

        self.string = new_string

    def add_milestone(self, phase, phase_degree, direction, length, placement, width, text, c_width=True):
        """Adds a label attached to a phase with all the specified params."""

        index = self.string.find(r'\addmilestone')
        index = index + self.string[index:].find('\n')

        if c_width:
            new_string = self.string[:index] + '\n' + r'\addmilestone{at=phase-' + str(phase) + \
    		  '.' + str(phase_degree) + ',direction=' + str(direction) + ':' + str(length) +\
    		  'cm,text={' + text + '},text options={' + placement + ',text width=' + str(width)\
    		  + 'cm}}\n' + self.string[index:]
        else:
            new_string = self.string[:index] + '\n' + r'\addmilestone{at=phase-' + str(phase) + \
    		  '.' + str(phase_degree) + ',direction=' + str(direction) + ':' + str(length) +\
    		  'cm,text={' + text + '},text options={' + placement + '}}\n' + self.string[index:]

        self.string = new_string

    def remove_phase(self, phase_index):
        """removes a phase at the specified index"""

        phase_index = self.phases - phase_index # because entries are added above the previous 
        phase_start, phase_end = 0, 0
        current_index = 0

        while current_index != phase_index:
            phase_start = self.string[phase_end:].find(r'\phase{') + phase_end
            phase_end = self.string[phase_start:].find('\n') + phase_start
            current_index = current_index + 1

        self.string = self.string[:phase_start] + self.string[phase_end:]