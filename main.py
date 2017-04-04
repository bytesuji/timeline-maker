import timeline as tl
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk

def hide_widget(widget, data):
    data.hide()

def show_widget(widget, data):
    data.show()

def recompile(widget, data):
    data.init_file()
    data.create()

def init_project(widget, data):
    textbox = data[1]
    data[0] = textbox.get_text()
    data[2].hide()

def main():

    builder = gtk.Builder()
    builder.add_from_file('timeline.ui')

    ### object definitions ###
    ## main window ##
    main_window = builder.get_object('main-window')
    menubar = builder.get_object('menubar')
    main_new_phase = builder.get_object('main-new-phase')
    main_new_milestone = builder.get_object('main-new-milestone')
    main_recompile = builder.get_object('main-recompile')
    main_set_interval = builder.get_object('main-set-interval')

    phase_input = builder.get_object('phase-input')
    pi_start_week = builder.get_object('pi-start-week')
    pi_end_week = builder.get_object('pi-end-week')
    pi_distance = builder.get_object('pi-distance')
    pi_color = builder.get_object('pi-color')
    pi_size = builder.get_object('pi-size')
    pi_add = builder.get_object('pi-add')

    milestone_input = builder.get_object('milestone-input')
    mi_phase = builder.get_object('mi-phase')
    mi_phase_degree = builder.get_object('mi-phase-degree')
    mi_direction = builder.get_object('mi-direction')
    mi_length = builder.get_object('mi-length')
    mi_placement = builder.get_object('mi-placement')
    mi_width = builder.get_object('mi-width')
    mi_text = builder.get_object('mi-text')
    mi_add = builder.get_object('mi-add')

    interval_input = builder.get_object('interval-input')
    ii_quantity = builder.get_object('ii-quantity')
    ii_custom_interval = builder.get_object('ii-custom-interval')
    ii_set = builder.get_object('ii-set')

    file_new = builder.get_object('file-new')
    file_open = builder.get_object('file-open')
    file_save = builder.get_object('file-save')
    file_save_as = builder.get_object('file-save-as')
    file_quit = builder.get_object('file-quit')

    edit_new_phase = builder.get_object('edit-new-phase')

    help_about = builder.get_object('help-about')
    ## initialiser window ##
    project_init_window = builder.get_object('project-init-window')
    project_init_input = builder.get_object('project-init-input')
    project_init_ok = builder.get_object('project-init-ok')

    ci_done = builder.get_object('ci-done')
    ci_1 = builder.get_object('ci-1')
    ci_2 = builder.get_object('ci-2')
    ci_3 = builder.get_object('ci-3')
    ci_4 = builder.get_object('ci-4')
    ci_5 = builder.get_object('ci-5')
    ci_6 = builder.get_object('ci-6')
    ci_7 = builder.get_object('ci-7')
    ci_8 = builder.get_object('ci-8')
    ci_9 = builder.get_object('ci-9')
    ci_10 = builder.get_object('ci-10')

    ### connections ###
    ## init ##
    project_name = None
    init_tuple = (project_name, project_init_input, project_init_window)
    project_init_ok.connect('clicked', init_project, project_name)

    ## main window ##
    main_new_phase.connect('clicked', show_widget, phase_input)
    main_new_milestone.connect('clicked', show_widget, milestone_input)
    main_set_interval.connect('clicked', show_widget, interval_input)
    main_recompile.connect('clicked', recompile)


if __name__ == '__main__':
    main()
