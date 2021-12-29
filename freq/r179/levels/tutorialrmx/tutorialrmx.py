#******************************************************************************
#
# Copyright (c) 1995-2001 Harmonix Music Systems
# All rights reserved
#
#******************************************************************************

class TutorialGameLevel (TutorialLevel):
    def __init__ (self):
        pass

class TutorialRemixLevel (TutorialLevel):
    def __init__ (self):

        TutorialLevel.__init__(self)

        self.directory_name = 'tutorialrmx'
        
        self.section_boundaries = [8, 16, 24, 32, 76]
        self.section_instances = [0, 1, 2, 3, 4]
        
        self.track_enable_criteria = ('yes', 'yes', 'yes', 'yes', 6, 6, 6, 6)
        self.game_bg_criteria = ('yes','yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes','yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        #self.section_names =  ['A', 'B', 'C', 'D', 'E']
        self.fx_filt_period = (1920, 960,  1920, 480,  1920, 960,  1920, 960)
        self.fx_stt         = (120, 0)
        self.fx_volume      = 50

        self.jam_fx  = ['vol', 'cho', 'stt', 'ech', 'gho']

        self.materials = ("drum",
                          "bass",
                          "lead",
                          "lead",
                          "synth",
                          "synth",
                          "synth",
                          "synth")

        self.extra_pitch_time = 0

        self.hili_fx = [ -20, -235, 55, -370 ]
        self.hili_loop = [ 45, -391, 77, -418 ]
        self.goal_effect = ''
        self.last_effect = ''

        self.using_bank_swap = 1

    def use_bank_swapping (self): return self.using_bank_swap

    def get_name (self):         return "Remix Tutorial"
    def get_abbrev_name (self):  return "Remix Tutorial"
    def get_artist (self):       return "DJ Kasson"
    def get_genre (self):        return "Techno"
    def get_tempo (self):        return "130"
    def get_description (self):  return "Use this FreQ Training Program to learn the skillz necessary to become a Frequency champion."
    def get_song_id (self):      return 19  # Return unique id for this song...

    def is_avail_game (self):    return 1
    def is_avail_jam (self):     return 0

    def get_num_laps (self):
        return 1

    # Start the tutorial state machine going...
    def on_game_begin (self):
        feedback_mgr.reset_feedback_system ()
        
        if ruleset == 'jam':
            self.start_remix ()

    # When the game is over, show all of the hud items and activator again.
    def on_game_over (self):
        debug_print (' GAME OVER...  Resetting graphics and sound')
        #hx.stop_all_midi ()      # Stop any voice over that's playing...
        # Undo some game stuff that we changed throughout the tutorial
        #  These all effect the game outside of this level.
        hx.seeker (1)            # Enable the seeker and phrase thread
        hx.activator (1)         # Enable the activator
        hx.nowring (1)           # Enable the now ring
        hx.sections (1)          # Enable the section boundaries
        #hx.juice_meter (1)       # Enable the juice meter
        #hx.score_meter (1)       # Enable the score display
        #hx.progress_meter (1)    # Enable the progress meter

        # redefine any previously redefined methods with their original
        #  functionality
        self.restore_attrs ()
    
    def highlight_animate (self, mode):
        hx.highlight_snap (self.hili_center[0], self.hili_center[1],
                           self.hili_center[2], self.hili_center[3])
        hx.highlight_setshow (1)

        if mode == 'loop':
            hx.highlight_slide (self.hili_loop[0], self.hili_loop[1],
                                self.hili_loop[2], self.hili_loop[3],
                                self.hili_anim_rate)
        elif mode == 'fx_panel':
            hx.highlight_slide (self.hili_fx[0], self.hili_fx[1],
                                self.hili_fx[2], self.hili_fx[3],
                                self.hili_anim_rate)
        else:
            hx.highlight_hide ()
            return
        delay_trans ((float(self.hili_anim_rate)/1920), 'current_level.blink_item (\'hx.highlight_setshow(1)\', \'hx.highlight_setshow(0)\', 0.3, 0.1, 6, \'off\')')


    ##########################################################################
    #
    #  Functions that represent states of the remix tutorial:
    #

    ########################### LOOPING REMIX STATES #########################
    # Call with looping = 'loop' means loop mode, 'no_loop' means non-loop mode
    def pitch_test (self, looping, func_delay, func, pitch_time, note, note_length, bank):
        global next_func, next_func_delay
        debug_print (' In PITCH_TEST state')
        next_func = func
        next_func_delay = func_delay
        self.extra_pitch_time = pitch_time

        hx.input ('enable', 0, 'rpch')      # Enable catching
        self.activator_control ('enable')   # Show the activator(just in case)
        
        # Warn every feedback_time bars if no input
        self.last_feedback = feedback_mgr.setup_timed_feedback (6, note, bank, note_length)
        debug_print (self.last_feedback)

        def on_pitch (self):
            debug_print (' Pitching detected!!!')

            time_left = feedback_mgr.get_fb_note_time_left (self.last_feedback)
            feedback_mgr.cancel_timed_feedback (self.last_feedback)
            new_delay = max([time_left, self.extra_pitch_time])
            delay_trans (new_delay, 'current_level.activator_control (\'disable\')')
            delay_trans (new_delay, 'hx.input (\'disable\', 0, \'rpch\')')
            delay_trans (next_func_delay + new_delay, next_func)
            self.restore_attrs ()
        self.on_pitch = new.instancemethod (on_pitch, self, self.__class__)
    
    def loop_tool_test (self, func_delay, func, note, note_length, bank):
        global next_func, next_func_delay
        debug_print (' In LOOP_TOOL_TEST state')
        next_func = func
        next_func_delay = func_delay
        hx.input ('enable', 0, 'loop')      # Enable looping
        self.activator_control ('enable')
        # Warn every 4 bars if no input
        self.last_feedback = feedback_mgr.setup_timed_feedback (6, note, bank, note_length)
        debug_print (self.last_feedback)
        
        def on_toggle_loop (self):
            debug_print (' Toggled loop tool...  let\'s move on')
            hx.input ('disable', 0, 'loop')     # Disable looping

            time_left = feedback_mgr.get_fb_note_time_left (self.last_feedback)
            feedback_mgr.cancel_timed_feedback (self.last_feedback)
            delay_trans (next_func_delay + time_left, 'current_level.activator_control (\'disable\')')
            delay_trans (next_func_delay + time_left, next_func)
            self.restore_attrs ()
        self.on_toggle_loop = new.instancemethod (on_toggle_loop, self, self.__class__)
    
    def erase_test (self, func_delay, func, note, note_length, bank):
        global next_func, next_func_delay
        debug_print (' In ERASE_TEST state')
        next_func = func
        next_func_delay = func_delay
        self.activator_control ('enable')
        hx.input ('enable', 0, 'eras')      # Enable erasing
        # Warn every 4 bars if no input
        self.last_feedback = feedback_mgr.setup_timed_feedback (6, note, bank, note_length)
        debug_print (self.last_feedback)
        
        def on_erase (self):
            hx.input ('disable', 0, 'eras')     # Disable erasing
            time_left = feedback_mgr.get_fb_note_time_left (self.last_feedback)
            feedback_mgr.cancel_timed_feedback (self.last_feedback)
                
            debug_print (' Erased track...  let\'s move on')
            delay_trans (next_func_delay + time_left, 'current_level.activator_control (\'disable\')')
            delay_trans (next_func_delay + time_left, next_func)
            self.restore_attrs ()
        self.on_erase = new.instancemethod (on_erase, self, self.__class__)

    def effects_select_test (self, func_delay, func, effect, note, note_length, bank):
        global next_func, next_func_delay
        debug_print (' In EFFECTS_SELECT_TEST state')
        next_func = func
        next_func_delay = func_delay
        self.goal_effect = effect
        hx.input ('enable', 0, 'powy')      # Enable powerup selection
        # Warn every 4 bars if no input
        self.last_feedback = feedback_mgr.setup_timed_feedback (6, note, bank, note_length)
        debug_print (self.last_feedback)
        
        def on_choose_powerup (self, powerup):
            if powerup_nums[self.goal_effect] != powerup:
                feedback_mgr.reset_feedback_timer (self.last_feedback, 0)
                return
            
            hx.input ('disable', 0, 'powy')     # Disable powerup selection
            time_left = feedback_mgr.get_fb_note_time_left (self.last_feedback)
            feedback_mgr.cancel_timed_feedback (self.last_feedback)
                
            debug_print (' Selected a powerup...  let\'s move on')
            delay_trans (next_func_delay + time_left, next_func)
            self.restore_attrs ()
        self.on_choose_powerup = new.instancemethod (on_choose_powerup, self, self.__class__)

    def effects_deploy_test (self, func_delay, func, note, note_length, bank):
        global next_func, next_func_delay
        debug_print (' In EFFECTS_DEPLOY_TEST state')
        next_func = func
        next_func_delay = func_delay
        hx.input ('enable', 0, 'powb')      # Enable powerup deployment
        # Warn every 4 bars if no input
        self.last_feedback = feedback_mgr.setup_timed_feedback (6, note, bank, note_length)
        debug_print (self.last_feedback)
        
        def on_jam_effect (self):
            hx.input ('disable', 0, 'powb')     # Disable powerup deployment
            time_left = feedback_mgr.get_fb_note_time_left (self.last_feedback)
            feedback_mgr.cancel_timed_feedback (self.last_feedback)
                
            debug_print (' Deployed effect...  let\'s move on')
            delay_trans (next_func_delay + time_left, next_func)
            self.restore_attrs ()
        self.on_jam_effect = new.instancemethod (on_jam_effect, self, self.__class__)

    def ghost_toggle_test (self, func_delay, func, note, note_length, bank):
        global next_func, next_func_delay
        debug_print (' In GHOST_TOGGLE_TEST state')
        next_func = func
        next_func_delay = func_delay
        hx.input ('enable', 0, 'powb')      # Enable powerup deployment
        # Warn every 4 bars if no input
        self.last_feedback = feedback_mgr.setup_timed_feedback (6, note, bank, note_length)
        debug_print (self.last_feedback)
        
        def on_toggle_ghosts (self):
            hx.input ('disable', 0, 'powb')     # Disable powerup deployment
            time_left = feedback_mgr.get_fb_note_time_left (self.last_feedback)
            feedback_mgr.cancel_timed_feedback (self.last_feedback)
                
            debug_print (' Ghost notes toggled...  let\'s move on')
            delay_trans (next_func_delay+ time_left, next_func)
            self.restore_attrs ()
        self.on_toggle_ghosts = new.instancemethod (on_toggle_ghosts, self, self.__class__)

    def section_advance_test (self, func_delay, func, note, note_length, bank):
        global next_func, next_func_delay
        debug_print (' In SECTION_ADVANCE_TEST state')
        next_func = func
        next_func_delay = func_delay
        hx.input ('enable', 0, 'advn')      # Enable section advance
        # Warn every 4 bars if no input
        self.last_feedback = feedback_mgr.setup_timed_feedback (6, note, bank, note_length)
        debug_print (self.last_feedback)
        
        def on_advance_section (self):
            hx.input ('disable', 0, 'advn')     # Disable section advance
            time_left = feedback_mgr.get_fb_note_time_left (self.last_feedback)
            feedback_mgr.cancel_timed_feedback (self.last_feedback)
                
            debug_print (' Advanced section...  let\'s move on')
            delay_trans (next_func_delay+ time_left, next_func)
            self.restore_attrs ()
        self.on_advance_section = new.instancemethod (on_advance_section, self, self.__class__)

    # keep the user from rotating left from track_1 or right from track_2
    def constrain_to_tracks (self, track_1, track_2):
        self.bound_track_1 = track_1
        self.bound_track_2 = track_2
        hx.input ('enable', 0, 'rotL')
        hx.input ('enable', 0, 'rotR')
        
        def on_track_select (self, track):
            debug_print (' Selected a track')
            debug_print (track)
            if track == self.bound_track_2:
                hx.input ('disable', 0, 'rotR')     # Disable rotation right
                hx.input ('enable', 0, 'rotL')      # Enable rotation left
                debug_print (' On bound_track_2, disable rotation right')
            elif track == self.bound_track_1:
                hx.input ('disable', 0, 'rotL')     # Disable rotation left
                hx.input ('enable', 0, 'rotR')      # Enable rotation right
                debug_print (' On bound_track_1, disable rotation left')

        self.on_track_select = new.instancemethod (on_track_select, self, self.__class__)

    def release_track_constraint (self):
        self.restore_attrs ()
        hx.input ('disable', 0, 'rotL')
        hx.input ('disable', 0, 'rotR')

    ############################## SPECIAL FUNCS #############################
    def listen (self, bars, func):
        debug_print (' In LISTEN state')
        delay_trans (bars, func)

    ############################## WELCOME REMIX #############################
    def start_remix (self):
        # Midi: Welcome to Remix Mode...
        delay_trans (2, 'play_voice (12, 0)')
        debug_print (' In START_REMIX state')
        hx.set_loop_mode (0)     # Turn looping off
        hx.set_ghost_mode (0)    # Turn ghost notes off
        hx.activator (0)         # Hide the activator
        hx.nowring (0)           # Hide the now ring
        hx.seeker (0)            # Hide the seeker
        hx.select_powerup (self.jam_fx.index('gho'))  # Start on ghost notes
        #hx.display_text ('')     # Wipe out the "Loop Engaged" text
        delay_trans (4, 'current_level.welcome_1()')
        
    def welcome_1 (self):
        debug_print (' In WELCOME_1 state')
        delay_trans (2, 'current_level.pitch_1()')

    ################################ PITCHING ################################
    def pitch_1 (self):
        debug_print (' In PITCH_1 state')
        # Midi: Let us begin with the drum...
        play_voice (13, 0)
        delay_trans (4, 'current_level.pitch_test(\'no_loop\', 0, \'current_level.loop_tool_1()\', 4, 14, 2, 0)')
    
    ################################ LOOP TOOL ###############################
    def loop_tool_1 (self):
        debug_print (' In LOOP_TOOL_1 state')
        self.advance_section ()
        # Midi: Good.  Now I will introduce you to the loop tool.
        hx.input ('enable', 0, 'rpch')
        play_voice (13, 1)
        delay_trans (1, 'hx.input(\'disable\', 0, \'rpch\')')

        # Midi: Press the d-pad down now...
        delay_trans (5, 'play_voice (12, 1)')

        delay_trans (6.5, 'current_level.loop_tool_test(0, \'current_level.loop_tool_3()\', 12, 2, 1)')
        
    def loop_tool_3 (self):
        debug_print (' In LOOP_TOOL_3 state')
        # Midi: The Loop Tool is now engaged...
        play_voice (12, 2)
        self.highlight_animate ('loop')
        delay_trans (8.5, 'current_level.pitch_test(\'loop\', 0, \'current_level.loop_tool_4()\', 2, 16, 2, 3)')
    
    def loop_tool_4 (self):
        debug_print (' In LOOP_TOOL_4 state')
        # Midi: Now you can hear your...
        play_voice (13, 3)
        delay_trans (2, 'current_level.listen(2, \'current_level.over_dubbing_1()\')')
    
    ############################## OVER-DUBBING ##############################
    def over_dubbing_1 (self):
        debug_print (' In OVER-DUBBING_1 state')
        # Midi: Once you've recorded a pattern...
        play_voice (14, 3)
        delay_trans (4, 'current_level.pitch_test(\'loop\', 0, \'current_level.over_dubbing_2()\', 2, 16, 1.5, 3)')
    
    def over_dubbing_2 (self):
        debug_print (' In OVER-DUBBING_2 state')
        # Midi: Great, you have added more...
        play_voice (15, 3)
        delay_trans (4, 'current_level.erasing_1()')

    ###############################  ERASING  ################################
    def erasing_1 (self):
        debug_print (' In ERASING_1 state')
        # Midi: If you are unhappy with your performance...
        play_voice (12, 4)
        self.should_test = 1
        
        # Detect erasing before we actually test for it...
        def on_erase (self):
            debug_print (' Erased track...  let\'s move on')
            self.should_test = 0
            self.restore_attrs ()
        self.on_erase = new.instancemethod (on_erase, self, self.__class__)

        delay_trans (2, 'hx.input(\'enable\', 0, \'eras\')')
        delay_trans (8.5, 'current_level.erasing_2 ()')
        #delay_trans (8.25, 'current_level.erase_test(0, \'current_level.erasing_2()\', 23, 1.25)')

    def erasing_2 (self):
        self.restore_attrs ()         # In case we haven't gotten an erase yet.
        if self.should_test == 1:
            self.erase_test(0, 'current_level.erasing_3()', 13, 1.25, 4)
        else:
            self.erasing_3()

    def erasing_3 (self):
        debug_print (' In ERASING_3 state')
        hx.input ('enable', 0, 'eras')
        # Midi: Great, now create...
        play_voice (12, 5)
        delay_trans (1.25, 'current_level.pitch_test(\'loop\', 0, \'current_level.erasing_4()\', 0, 16, 1.5, 5)')
    
    def erasing_4 (self):
        debug_print (' In ERASING_4 state')
        # Midi: Execellent.  You can keep on erasing...
        delay_trans (2, 'play_voice (13, 5)')
        hx.input ('enable', 0, 'rpch')      # Let the user pitch for a while...
        self.activator_control ('enable')
        delay_trans (6, 'current_level.rotation_test([1], 0, \'current_level.melodic_1()\', 14, 2.5, 6, 5)')


    #########################  MELODIC INSTRUMENTS  ##########################
    def melodic_1 (self):
        hx.input ('disable', 0, 'rpch')
        self.activator_control ('disable')
        debug_print (' In MELODIC_1 state')
        # Midi: Melodic instruments, like guitar...
        play_voice (12, 6)
        delay_trans (5, 'current_level.pitch_test(\'no_loop\', 0, \'current_level.melodic_2()\', 4, 14, 2.25, 6)')

    def melodic_2 (self):
        debug_print (' In MELODIC_2 state')
        self.activator_control ('enable')
        hx.input ('enable', 0, 'rpch')
        # Midi: Ok, now let's move on.
        play_voice (13, 6)
        delay_trans (2, 'current_level.section_advance_1 ()')

    ############################# SECTION ADVANCE #############################
    def section_advance_1 (self):
        debug_print (' In SECTION_ADVANCE_1 state')
        # Midi: Each song is divided up into...
        play_voice (12, 7)
        delay_trans (6, 'current_level.section_advance_test(0, \'current_level.section_advance_2()\', 13, 2.5, 7)')
    
    def section_advance_2 (self):
        debug_print (' In SECTION_ADVANCE_2 state')
        hx.display_text ('ADVANCE TO NEXT SECTION')

        time_to_section = 8 - (hx.clock ('song_bar') % 8) - (float(hx.clock('tick') % 1920)/1920)
        print time_to_section 
        delay_trans (time_to_section, 'hx.input (\'disable\', 0, \'rpch\')')
        delay_trans (time_to_section, 'hx.input (\'disable\', 0, \'eras\')')
        delay_trans (time_to_section, 'current_level.activator_control (\'disable\')')
        # Midi: You've just passed into the next...
        delay_trans (time_to_section, 'play_voice (12, 8)')
        delay_trans (time_to_section + 9.5, 'current_level.guide_1()')

    ############################### GUIDE NOTES ###############################
    def guide_1 (self):
        debug_print (' In GUIDE_1 state')
        # Midi: If you have difficulty coming up with...
        play_voice (12, 9)
        self.should_test = 1
        delay_trans (3, 'hx.analog_stick_setmat (\'in_out\')')
        delay_trans (3, 'hx.analog_stick_setshow (1)')
        delay_trans (3, 'hx.input (\'enable\', 0, \'powb\')')

        def on_toggle_ghosts (self):
            self.should_test = 0
            hx.analog_stick_setshow (0)
            self.restore_attrs ()
        self.on_toggle_ghosts = new.instancemethod (on_toggle_ghosts, self, self.__class__)

        delay_trans (5.5, 'current_level.guide_2 ()')
        
    def guide_2 (self):
        debug_print (' In GUIDE_2 state')
        if self.should_test == 1:
            self.ghost_toggle_test(0, 'current_level.guide_3()', 13, 1.5, 9)
        else:
            self.guide_3 ()

    def guide_3 (self):
        hx.input ('enable', 0, 'rpch')
        hx.analog_stick_setshow (0)
        current_level.activator_control ('enable')
        # Midi: If you follow these guide...
        play_voice (14, 9)

        # Midi: Good, now let's put some...
        #delay_trans (6, 'play_voice (15, 9)')
        delay_trans (6, 'current_level.constrain_to_tracks (0, 1)')

        # Midi: Now move on over to the other track and match...
        delay_trans (6, 'play_voice (12, 10)')
        
        delay_trans (12, 'current_level.effects_1()')
    
    ################################  EFFECTS  ################################
    def effects_1 (self):
        debug_print (' In EFFECTS_1 state')
        # Midi: Now let's add some effects...
        play_voice (13, 10)

        # Midi: This is the effects control panel...
        delay_trans (2, 'play_voice(14, 10)')
        delay_trans (2, 'current_level.highlight_animate(\'fx_panel\')')

        # Midi: Effects let you transform the sound...
        delay_trans (4, 'play_voice(15, 10)')

        # Midi: Move the analog stick on your controller...
        delay_trans (8, 'play_voice(17, 10)')

        delay_trans (9, 'hx.analog_stick_setmat (\'up_down\')')
        delay_trans (9, 'hx.analog_stick_setshow (1)')

        self.should_test = 1
        self.last_effect = -1
        def on_choose_powerup (self, pow):
            self.last_effect = pow
        self.on_choose_powerup = new.instancemethod (on_choose_powerup, self, self.__class__)
        delay_trans (9, 'hx.input (\'enable\', 0, \'powy\')')
        delay_trans (12.5, 'current_level.effects_2()')
        
    def effects_2 (self):
        debug_print (' In EFFECTS_2 state')
        self.restore_attrs ()        # reset on_choose_powerup() 
        self.goal_effect = 'ech'
        if powerup_nums[self.goal_effect] != self.last_effect:
            debug_print (' testing effect selection')
            self.effects_select_test(0, 'current_level.effects_3()', 'ech', 17, 3, 10)
        else:
            hx.input ('disable', 0, 'powy')
            self.effects_3 ()

    def effects_3 (self):
        debug_print (' In EFFECTS_3 state')
        # Midi: To turn on an effect, push in...
        play_voice(12, 11)
        delay_trans (1, 'hx.analog_stick_setmat (\'in_out\')')

        self.should_test = 1
        def on_jam_effect (self):
            self.should_test = 0
            self.restore_attrs ()
        self.on_jam_effect = new.instancemethod (on_jam_effect, self, self.__class__)
        delay_trans (1, 'hx.input (\'enable\', 0, \'powb\')')
        delay_trans (3, 'current_level.effects_4 ()')

    def effects_4 (self):
        debug_print (' In EFFECTS_4 state')
        if self.should_test == 1:
            debug_print (' testing effect deployment')
            self.effects_deploy_test(0, 'current_level.effects_5()', 14, 1.5, 11)
        else:
            self.effects_5 ()
        
    def effects_5 (self):
        hx.analog_stick_setshow (0)
        hx.input ('enable', 0, 'powy')
        hx.input ('enable', 0, 'powb')
        self.constrain_to_tracks (0, 1)
        debug_print (' In EFFECTS_5 state')
        self.listen(2, 'current_level.effects_6()')
    
    def effects_6 (self):
        debug_print (' In EFFECTS_6 state')
        # Midi: You have now turned on the...
        play_voice (15, 11)

        # Midi: Pressing the right analog stick button...
        delay_trans (1.5, 'play_voice (12, 12)')

        # Midi: To adjust the loudness of a track...
        delay_trans (10, 'play_voice (13, 12)')
        
        # Midi: OK, let's move on...
        delay_trans (15, 'play_voice (14, 12)')
        delay_trans (16, 'current_level.scratch_axe_1()')
    
    ##############################  SCRATCH/AXE  ##############################
    def scratch_axe_1 (self):
        debug_print (' In SCRATCH_AXE_1 state')
        # Midi: Scratch and Axe tracks are...
        play_voice (15, 12)
        delay_trans (5, 'current_level.release_track_constraint ()')
        delay_trans (5, 'current_level.rotation_test([2,3], 0, \'current_level.scratch_axe_2()\', 16, 1.5, 4, 12)')
    
    def scratch_axe_2 (self):
        debug_print (' In SCRATCH_AXE_2 state')
        hx.input ('enable', 0, 'rpch')
        hx.input ('enable', 0, 'regi')
        hx.input ('enable', 0, 'axfx')
        hx.input ('disable', 0, 'powb')
        hx.input ('disable', 0, 'powy')
        self.constrain_to_tracks (2, 3)

        self.activator_control ('enable')
        delay_trans (8, 'current_level.listen(8, \'current_level.scratch_axe_3()\')')
    
    # FIXME:  do a scratching/axing test here.... 

    def scratch_axe_3 (self):
        debug_print (' In SCRATCH_AXE_3 state')
        # Midi: Excellent.  You may have noticed....
        play_voice (17, 12)
        delay_trans (4, 'current_level.listen_mode()')
    
    ##############################  LISTEN MODE  ##############################
    def listen_mode (self):
        debug_print (' In LISTEN_MODE state')
        self.release_track_constraint ()
        hx.input ('disable', 0, 'rotL')
        hx.input ('disable', 0, 'rotR')
        #hx.input ('disable', 0, 'rpch')
        #hx.input ('disable', 0, 'regi')
        #hx.input ('disable', 0, 'axfx')
        #self.activator_control ('disable')

        # Midi: Once you have completed remixing...
        play_voice (12, 13)
        delay_trans (4, 'current_level.conclusion_1()')
    
    ##############################  CONCLUSION   ##############################
    def conclusion_1 (self):
        debug_print (' In CONCLUSION_1 state')
        self.release_track_constraint ()
        # Midi: Once you are happy with your remix...
        play_voice (12, 14)

        # Midi: Remix mode is a powerful...
        delay_trans (5, 'play_voice (13, 14)')

        # Midi: This tutorial is now complete...
        delay_trans (10, 'play_voice (14, 14)')
        delay_trans (12, 'hx.stop_game ()')
    
    ###########################################################################

def get_class_name ():
    return TutorialRemixLevel
