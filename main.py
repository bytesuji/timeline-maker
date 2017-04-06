#!/bin/python3
### TODO ###
# make color selection a dropdown menu
# make placement a dropdown
# make 'added' confirm labels

import timeline as tl
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
from gi.repository import GObject as gobject

def hide_widget(widget, data):

    data.hide()

def show_widget(widget, data):

    data.show()

def run_widget(widget, data):

    data.run()
    data.destroy()

def recompile(widget, data):

    timeline = data[0]
    preview = data[1]
    viewport = data[2]

    timeline.init_file()
    timeline.create()

    preview.set_from_file(timeline.name + '.png')
    viewport.show()

def init_project(widget, data):

    textbox = data[0]
    timeline = data[2]
    name = textbox.get_text()
    timeline.set_name(name)
    data[1].hide()

def add_new_phase(widget, data):

    start_week = data[0].get_text()
    end_week = data[1].get_text()
    distance = data[2].get_value()
    color = data[3].get_text()
    size = data[4].get_value()
    timeline = data[5]

    timeline.add_phase(start_week, end_week, distance, color, size)

    # cleanup
    data[0].set_text('')
    data[1].set_text('')
    data[2].set_value(0)
    data[3].set_text('')
    data[4].set_value(0)

def set_interval(widget, data):

    weeks = data[0]
    switch = data[1]
    window = data[2]
    timeline = data[3]

    if switch.get_active():
        window.show()
    else:
        timeline.set_interval(weeks.get_text())

    switch.set_active(False)
    weeks.set_text('')

def ci_set(widget, data):

    timeline = data[10]
    custom_intervals = []
    for i in range(10):
        if data[i].get_text():
            custom_intervals.append(data[i].get_text())
    timeline.set_interval(0, True, custom_intervals)

def add_new_milestone(widget, data):

    phase = data[0].get_text()
    phase_degree = data[1].get_value()
    direction = data[2].get_value()
    length = data[3].get_text()
    placement = data[4].get_active()
    if placement == 1:
        placement = 'above'
    if placement == 2:
        placement = 'below'
    width = data[5].get_text()
    text = data[6].get_text()
    timeline = data[7]

    timeline.add_milestone(phase, phase_degree, direction,\
    length, placement, width, text)

    data[0].set_text('')
    data[1].set_value(0)
    data[2].set_value(0)
    data[3].set_text('')
    data[4].set_active(0)
    data[5].set_text('')
    data[6].set_text('')


def new_project(widget, data):

    # new_project_tuple = [timeline, project_new_window, project_new_input, project_new_ok]
    timeline = data[0]
    timeline.__init__()
    window = data[1]
    textbox = data[2]
    ok = data[3]

    window.show()

    def _ok_callback(widget, data):

        data[0].set_name(data[2].get_text())
        data[1].hide()

    ok.connect('clicked', _ok_callback, data)

def label_hider(labels):

    for label in labels:
        label.hide()

    gobject.timeout_add(5000, label_hider, labels)

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

    compiled_image = builder.get_object('compiled-image')
    viewport = builder.get_object('viewport')

    confirm_label = builder.get_object('confirm-label')
    ii_set_confirm_label = builder.get_object('ii-set-confirm-label')

    phase_input = builder.get_object('phase-input')
    pi_start_week = builder.get_object('pi-start-week')
    pi_end_week = builder.get_object('pi-end-week')
    pi_distance_adjust = builder.get_object('pi-distance-adjust')
    pi_color = builder.get_object('pi-color')
    pi_size_adjust = builder.get_object('pi-size-adjust')
    pi_add = builder.get_object('pi-add')

    milestone_input = builder.get_object('milestone-input')
    mi_phase = builder.get_object('mi-phase')
    mi_phase_degree_adjust = builder.get_object('mi-phase-degree-adjust')
    mi_direction_adjust = builder.get_object('mi-direction-adjust')
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
    file_quit = builder.get_object('file-quit')

    help_about = builder.get_object('help-about')
    ## initialiser window ##
    project_init_window = builder.get_object('project-init-window')
    project_init_input = builder.get_object('project-init-input')
    project_init_ok = builder.get_object('project-init-ok')
    ## new window ##
    project_new_window = builder.get_object('project-new-window')
    project_new_input = builder.get_object('project-new-input')
    project_new_ok = builder.get_object('project-new-ok')

    custom_interval_window = builder.get_object('custom-interval-window')
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

    ## about window ##
    about_window = builder.get_object('about-window')

    ### connections ###
    ## init ##
    timeline = tl.Timeline()
    init_tuple = [project_init_input, project_init_window, timeline]
    project_init_ok.connect('clicked', init_project, init_tuple)
    ## main window ##
    main_new_phase.connect('clicked', show_widget, phase_input)
    main_new_milestone.connect('clicked', show_widget, milestone_input)
    main_set_interval.connect('clicked', show_widget, interval_input)
    recompile_tuple = (timeline, compiled_image, viewport)
    main_recompile.connect('clicked', recompile, recompile_tuple)

    pi_data_tuple = (pi_start_week, pi_end_week, pi_distance_adjust,\
    pi_color, pi_size_adjust, timeline)
    pi_add.connect('clicked', add_new_phase, pi_data_tuple)
    pi_add.connect('clicked', show_widget, confirm_label)

    mi_data_tuple = (mi_phase, mi_phase_degree_adjust, mi_direction_adjust,\
    mi_length, mi_placement, mi_width, mi_text, timeline)
    mi_add.connect('clicked', add_new_milestone, mi_data_tuple)
    mi_add.connect('clicked', show_widget, confirm_label)

    ii_data_tuple = (ii_quantity, ii_custom_interval, custom_interval_window, timeline)
    ii_set.connect('clicked', set_interval, ii_data_tuple)
    ii_set.connect('clicked', show_widget, ii_set_confirm_label)

    ci_data_tuple = (ci_1, ci_2, ci_3, ci_4, ci_5, ci_6, ci_7, ci_8, ci_9, ci_10, timeline)
    ci_done.connect('clicked', ci_set, ci_data_tuple)
    ci_done.connect('clicked', hide_widget, custom_interval_window)


    # for hiding non-used widgets
    hiders = (main_new_milestone, main_set_interval, main_recompile)
    for hider in hiders:
        hider.connect('clicked', hide_widget, phase_input)
    hiders = (main_new_phase, main_set_interval, main_recompile)
    for hider in hiders:
        hider.connect('clicked', hide_widget, milestone_input)
    hiders = (main_new_phase, main_new_milestone, main_recompile)
    for hider in hiders:
        hider.connect('clicked', hide_widget, interval_input)
    hiders = (main_new_phase, main_new_milestone, main_set_interval)
    for hider in hiders:
        hider.connect('clicked', hide_widget, viewport)
    del hiders

    ## destroys ##
    main_window.connect('destroy', gtk.main_quit)
    custom_interval_window.connect('destroy', hide_widget, custom_interval_window)
    project_init_window.connect('destroy', hide_widget, project_init_window)

    ## menu clickies ##
    new_project_tuple = [timeline, project_new_window, project_new_input, project_new_ok]
    file_new.connect('activate', new_project, new_project_tuple)
    file_quit.connect('activate', gtk.main_quit)
    help_about.connect('activate', run_widget, about_window)

    # misc
    project_init_window.set_default(project_init_ok)
    project_new_window.set_default(project_init_ok)
    labels_tuple = (confirm_label, ii_set_confirm_label)
    gobject.timeout_add(5000, label_hider, labels_tuple)


    gtk.main()

if __name__ == '__main__':
    main()
