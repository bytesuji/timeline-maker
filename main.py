import timeline as tl
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk

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
    # phase input things
    pi_start_week = builder.get_object('pi-start-week')
    pi_end_week = builder.get_object('pi-end-week')
    pi_distance = builder.get_object('pi-distance')
    pi_color = builder.get_object('pi-color')
    pi_size = builder.get_object('pi-size')
    pi_add = builder.get_object('pi-add')
    # milestone things
    mi_phase = builder.get_object('mi-phase')
    mi_phase_degree = builder.get_object('mi-phase-degree')
    mi_direction = builder.get_object('mi-direction')
    mi_length = builder.get_object('mi-length')
    mi_placement = builder.get_object('mi-placement')
    mi_width = builder.get_object('mi-width')
    mi_text = builder.get_object('mi-text')
    mi_add = builder.get_object('mi-add')
    # interval things
    ii_quantity = builder.get_object('ii-quantity')
    ii_custom_interval = builder.get_object('ii-custom-interval')
    ii_set = builder.get_object('ii-set')
    # menu bar buttons
    # file
    file_new = builder.get_object('file-new')
    file_open = builder.get_object('file-open')
    file_save = builder.get_object('file-save')
    file_save_as = builder.get_object('file-save-as')
    file_quit = builder.get_object('file-quit')
    # edit
    edit_new_phase = builder.get_object('edit-new-phase')
    # help
    help_about = builder.get_object('help-about')
    ## initialiser window ##
    project_init_window = builder.get_object('project-init-window')
    project_init_input = builder.get_object('project-init-input')
    project_init_ok = builder.get_object('project-init-ok')
    ## custom interval window ##
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
