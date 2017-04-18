#!/bin/python3
### TODO ###
# add remove options (lots of code required)

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
from gi.repository import GObject as gobject

import timeline as tl
from callbacks import * # safe because these have all been defined by me

def main():
	builder = gtk.Builder()
	builder.add_from_file('timeline.ui')

	### object definitions ###
	## main window ##
	main_window = builder.get_object('main-window')
	menubar = builder.get_object('menubar')

	main_buttons = builder.get_object('main-buttons')
	main_new_phase = builder.get_object('main-new-phase')
	main_new_milestone = builder.get_object('main-new-milestone')
	main_recompile = builder.get_object('main-recompile')
	main_set_interval = builder.get_object('main-set-interval')

	negative_buttons = builder.get_object('negative-buttons')
	main_reset = builder.get_object('main-reset')
	main_remove_phase = builder.get_object('main-remove-phase')
	main_remove_milestone = builder.get_object('main-remove-milestone')

	compiled_image = builder.get_object('compiled-image')

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

	remove = builder.get_object('remove')
	remove_remove = builder.get_object('remove-remove')
	remove_index = builder.get_object('remove-index')

	file_new = builder.get_object('file-new')
	file_open = builder.get_object('file-open')
	file_quit = builder.get_object('file-quit')

	edit_show_additive = builder.get_object('edit-show-additive')
	edit_show_destructive = builder.get_object('edit-show-destructive')

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

	## dialogues ## 
	about_window = builder.get_object('about-window')
	reset_confirm_window = builder.get_object('reset-confirm-window')
	reset_ok = builder.get_object('reset-ok')
	reset_cancel = builder.get_object('reset-cancel')

	### connections ###

	## init ##
	timeline = tl.Timeline()
	init_tuple = [project_init_input, project_init_window, timeline]
	project_init_ok.connect('clicked', init_project, init_tuple)

	## main window ##
	main_new_phase.connect('clicked', show_widget, phase_input)
	main_new_milestone.connect('clicked', show_widget, milestone_input)
	main_set_interval.connect('clicked', show_widget, interval_input)
	recompile_tuple = (timeline, compiled_image)
	main_recompile.connect('clicked', recompile, recompile_tuple)

	main_reset.connect('clicked', show_widget, reset_confirm_window) 
	reset_ok.connect('clicked', reset_timeline, timeline)
	reset_cancel.connect('clicked', hide_widget, reset_confirm_window)

	# code to make the two remove buttons work on a single widget
	which_clicked = None
	main_remove_phase.connect('clicked', show_remove, (remove, which_clicked, 'phase'))
	main_remove_milestone.connect('clicked', show_remove, (remove, which_clicked, 'milestone'))

	remove_remove.connect('clicked', remove_phase_or_ms, (timeline, which_clicked, remove_index,
														  confirm_label))
	remove_remove.connect('clicked', show_widget, confirm_label)

	pi_data_tuple = (pi_start_week, pi_end_week, pi_distance_adjust,\
	pi_color, pi_size_adjust, timeline, confirm_label)
	pi_add.connect('clicked', add_new_phase, pi_data_tuple)
	pi_add.connect('clicked', show_widget, confirm_label)

	mi_data_tuple = (mi_phase, mi_phase_degree_adjust, mi_direction_adjust,\
	mi_length, mi_placement, mi_width, mi_text, timeline, confirm_label)
	mi_add.connect('clicked', add_new_milestone, mi_data_tuple)
	mi_add.connect('clicked', show_widget, confirm_label)

	ii_data_tuple = (ii_quantity, ii_custom_interval, custom_interval_window, timeline)
	ii_set.connect('clicked', set_interval, ii_data_tuple)
	ii_set.connect('clicked', show_widget, ii_set_confirm_label)

	ci_data_tuple = (ci_1, ci_2, ci_3, ci_4, ci_5, ci_6, ci_7, ci_8, ci_9, ci_10, timeline)
	ci_done.connect('clicked', ci_set, ci_data_tuple)
	ci_done.connect('clicked', hide_widget, custom_interval_window)


	# for hiding unused widgets
	hiders = (main_new_milestone, main_set_interval, main_recompile)
	for hider in hiders:
		hider.connect('clicked', hide_widget, phase_input)
	hiders = (main_new_phase, main_set_interval, main_recompile)
	for hider in hiders:
		hider.connect('clicked', hide_widget, milestone_input)
	hiders = (main_new_phase, main_new_milestone, main_recompile)
	for hider in hiders:
		hider.connect('clicked', hide_widget, interval_input)
	del hiders

	## destroys ##
	main_window.connect('destroy', gtk.main_quit)
	custom_interval_window.connect('destroy', hide_widget, custom_interval_window)
	project_init_window.connect('destroy', hide_widget, project_init_window)

	## menu clickies ##
	new_project_tuple = [timeline, project_new_window, project_new_input, project_new_ok]

	file_new.connect('activate', new_project, new_project_tuple)
	file_quit.connect('activate', gtk.main_quit)

	edit_show_additive.connect('activate', show_hide, (main_buttons, negative_buttons, 'add'))
	edit_show_destructive.connect('activate', show_hide, (main_buttons, negative_buttons, 'des'))

	help_about.connect('activate', run_widget, about_window)

	# misc
	project_init_window.set_default(project_init_ok)
	project_new_window.set_default(project_init_ok)
	labels_tuple = (confirm_label, ii_set_confirm_label)
	gobject.timeout_add(5000, label_hider, labels_tuple)


	gtk.main()

if __name__ == '__main__':
	main()