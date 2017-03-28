from subprocess import call

class Timeline:

    def __init__(self, name):

        self.string = r'''\documentclass[border=10pt]{standalone}
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

        self.name = name

    def create(self, engine='xelatex', remove_tex_file=True):

        call([engine, self.name + '.tex'])
        call(['evince', self.name + '.pdf']) # change evince to pdf viewer of your choice

    def init_file(self):

        f = open(self.name + '.tex', 'w')
        f = f.write(self.string)

    def add_phase(self, start_week, end_week, in_val, color='red', degree=2.5):

        new_string = self.string
        index = new_string.find('\phase')
        index = new_string[index:].find('\n') + index; # find the next newline after the first phase

        new_string = new_string[:index] + '\n\t' + r'\phase{between week=' + str(start_week) + ' and ' + str(end_week) + ' in ' + str(in_val) + ',involvement degree=' + involvement_degree + 'cm,phase color=' + color + '}' + new_string[index:]

        self.string = new_string

    def set_interval(self, interval_length, custom_interval=False):

        if custom_interval:
            print("Please input your interval markers: ")
            next_interval = ''
            custom_intervals = []
            while True:
                next_interval = input()
                if next_interval.lower() == 'done':
                    break
                custom_intervals.append(next_interval)
            # replace \timeline
            begin_index = self.string.find(r'\timeline')
            end_index = begin_index + self.string[begin_index:].find('\n')

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
            begin_index = self.string.find(r'\timeline')
            end_index = begin_index + self.string[begin_index:].find('\n')
            new_timeline = r'\timeline{' + str(interval_length) + '}'

        self.string = new_string

    def add_milestone(self, phase, phase_degree, direction, length, placement, width, text):

        index = self.string.find(r'\addmilestone')
        index = index + self.string[index:].find('\n')

        new_string = self.string[:index] + '\n' + r'\addmilestone{at=phase-' + str(phase) + '.' + str(phase_degree) + ',direction=' + str(direction) + ':' + str(length) + 'cm,text={' + text + '},text options={' + placement + ',text width=' + str(width)
        new_string = new_string + 'cm}}\n' + string[index:]

        self.string = new_string
