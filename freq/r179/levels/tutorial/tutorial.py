#******************************************************************************
#
# Copyright (c) 1995-2001 Harmonix Music Systems
# All rights reserved
#
#******************************************************************************

class TutorialRemixLevel (TutorialLevel):
    def __init__ (self):
        pass

class TutorialGameLevel (TutorialLevel):
    def __init__ (self):

        TutorialLevel.__init__(self)
        
        self.section_boundaries = [14, 16, 24, 30, 38, 76]
        self.section_instances = [0, 1, 2, 3, 4, 5]
        
        self.directory_name = 'tutorial'

        self.track_enable_criteria = ('yes', 6, 6, 6, 6, 6, 6, 6)
        self.game_bg_criteria = ('yes','yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes',(1,2), 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.section_names =  ['A', 'B', 'C', 'D', 'E', 'F']
        self.fx_filt_period = (1920, 960,  1920, 480,  1920, 960,  1920, 960)
        self.fx_stt         = (120, 0)
        self.fx_volume      = 50

        self.materials = ("drum",
                          "bass",
                          "lead",
                          "lead",
                          "synth",
                          "synth",
                          "synth",
                          "synth")

        self.hili_energy = [ 0, -170, 28, -300 ]
        self.hili_progress = [ 532, 5, 552, -420]
        self.hili_score = [ 65, 9, 145, 0 ]
        self.hili_activ = [ 200, -340, 340, -370 ]

        self.try_note = 0
        self.using_bank_swap = 1

    def use_bank_swapping (self): return self.using_bank_swap

    def get_name (self):         return "Game Tutorial"
    def get_abbrev_name (self):  return "Game Tutorial"
    def get_artist (self):       return "DJ Kasson"
    def get_genre (self):        return "Techno"
    def get_tempo (self):        return "130"
    def get_description (self):  return "Use this FreQ Training Program to learn the skillz necessary to become a Frequency champion."
    def get_song_id (self):      return 18  # Return unique id for this song...

    def is_avail_game (self):    return 1
    def is_avail_jam (self):     return 0

    def get_num_laps (self):
        return 1

    # Start the tutorial state machine going...
    def on_game_begin (self):
        feedback_mgr.reset_feedback_system ()
        self.start_game ()

    # When the game is over, show all of the hud items and activator again.
    def on_game_over (self):
        debug_print (' GAME OVER...  Resetting graphics')
        # Undo some game stuff that we changed throughout the tutorial
        #  These all effect the game outside of this level.
        hx.sections (1)          # Enable the section boundaries
        hx.freeze_juice (0)      # Unfreeze the juice meter

        # redefine any previously redefined methods with their original
        #  functionality
        self.restore_attrs ()
    
    def highlight_animate (self, mode):
        hx.highlight_snap (self.hili_center[0], self.hili_center[1],
                           self.hili_center[2], self.hili_center[3])
        hx.highlight_setshow (1)

        if mode == 'energy':
            hx.highlight_slide (self.hili_energy[0], self.hili_energy[1],
                                self.hili_energy[2], self.hili_energy[3],
                                current_level.hili_anim_rate)
        elif mode == 'progress':
            hx.highlight_slide (self.hili_progress[0], self.hili_progress[1],
                                self.hili_progress[2], self.hili_progress[3],
                                current_level.hili_anim_rate)
        elif mode == 'score':
            hx.highlight_slide (self.hili_score[0], self.hili_score[1],
                                self.hili_score[2], self.hili_score[3],
                                current_level.hili_anim_rate)
        elif mode == 'activator':
            hx.highlight_slide (self.hili_activ[0], self.hili_activ[1],
                                self.hili_activ[2], self.hili_activ[3],
                                current_level.hili_anim_rate)
        else:
            hx.highlight_hide ()
            return
        delay_trans ((float(current_level.hili_anim_rate)/1920), 'current_level.blink_item (\'hx.highlight_setshow(1)\', \'hx.highlight_setshow(0)\', 0.3, 0.1, 6, \'off\')')


    #*************************************************************************
    #
    #  Functions that represent states of the game tutorial:
    #

    #########################  LOOPING STATES  #########################
    #  i.e. states that require specific input to move on...
    #

    #
    # Test the user's ability to catch consecutive gems on the track specified
    # If the user passes, then call func, otherwise stay here...
    #  bank == the bank to get feedback samples from
    #
    def catch_test (self, func_delay, func, bank):
        global consecutive_hits, next_func, next_func_delay, bank_num
        consecutive_hits = 0
        next_func = func
        next_func_delay = func_delay
        bank_num = bank
        hx.input ('enable', 0, 'rpch')      # Enable catching
        # Warn every 3 bars if no input
        self.last_feedback = feedback_mgr.setup_timed_feedback (3, 19, bank, 1)
        self.activator_control ('enable')   # Show the activator
        debug_print (self.last_feedback)

        def on_hit (self):
            debug_print ('  We have a hit')
            global consecutive_hits, consecutive_misses, consecutive_passes

            consecutive_misses = consecutive_passes = 0  # reset these
            consecutive_hits = consecutive_hits + 1      # got another hit
            feedback_mgr.reset_feedback_timer (self.last_feedback, 0)

            if consecutive_hits < 3:
                # Midi: Correct!
                if self.feedback_midi == 1 and feedback_enabled == 1:
                    delay_trans (0.08, 'play_voice (20, %d)' % bank_num)
                debug_print (' Not enough hits yet.')
            elif consecutive_hits == 3:
                hx.input ('disable', 0, 'rpch')     # Disable catching
                time_left = feedback_mgr.get_fb_note_time_left (self.last_feedback)
                feedback_mgr.cancel_timed_feedback (self.last_feedback)
                self.activator_control ('disable')
                delay_trans (next_func_delay + time_left, next_func)
                self.restore_attrs ()
        self.on_hit = new.instancemethod (on_hit, self, self.__class__)

        def on_miss (self):
            debug_print ('  We have a miss')
            global consecutive_hits, consecutive_misses, consecutive_passes

            consecutive_hits = consecutive_passes = 0
            consecutive_misses = consecutive_misses + 1
            feedback_mgr.reset_feedback_timer (self.last_feedback, 0)

            if consecutive_misses == 3:
                # Midi: Try again...
                if self.feedback_midi == 1:
                    delay_trans (0.08, 'play_voice (17, %d)' % bank_num)
                consecutive_misses = 0
        self.on_miss = new.instancemethod (on_miss, self, self.__class__)

        debug_print (' In CATCH_TEST state')

    
    #
    # Can the user capture a phrase???
    #
    def activation_test (self, num_tracks, func_delay, func, note, note_len, bank, try_note):
        global next_func, next_func_delay, bank_num
        next_func = func
        next_func_delay = func_delay
        bank_num = bank
        self.num_tracks_left = num_tracks
        self.num_tracks_act = 0
        self.try_note = try_note

        debug_print (' In ACTIVATION_TEST state')
        hx.input ('enable', 0, 'rpch')
        hx.input ('enable', 0, 'rotR')
        hx.input ('enable', 0, 'rotL')
        self.activator_control ('enable')        # Show the activator
        # Warn every 3 bars if no input
        self.last_feedback = feedback_mgr.setup_timed_feedback (3, note, bank, note_len)
        debug_print (self.last_feedback)

        def on_miss (self):
            debug_print ('  We have a miss')
            global consecutive_phrases, consecutive_misses, consecutive_passes
            feedback_mgr.reset_feedback_timer (self.last_feedback, 0)

            consecutive_phrases = consecutive_passes = 0
            consecutive_misses = consecutive_misses + 1

            if consecutive_misses == 3:
                # Midi: Try again...
                if self.feedback_midi == 1:
                    delay_trans (0.08, 'play_voice (current_level.try_note, %d)' % bank_num)
                consecutive_misses = 0
        self.on_miss = new.instancemethod (on_miss, self, self.__class__)

        def on_hit (self):
            feedback_mgr.reset_feedback_timer (self.last_feedback, 0)
            global consecutive_phrases, consecutive_misses, consecutive_passes
            consecutive_phrases = consecutive_misses = consecutive_passes = 0
        self.on_hit = new.instancemethod (on_hit, self, self.__class__)

        def on_phrase_capture (self, track):
            debug_print (' Caught a phrase!!!  Yeah!')

            self.num_tracks_act = self.num_tracks_act + 1
            if self.num_tracks_act == self.num_tracks_left:
                feedback_mgr.cancel_timed_feedback (self.last_feedback)
                hx.input ('disable', 0, 'rpch')
                hx.input ('disable', 0, 'rotL')
                hx.input ('disable', 0, 'rotR')
                self.activator_control ('disable')
                delay_trans (next_func_delay, next_func)
                self.restore_attrs ()
            else:
                hx.display_text ("TRACK CAPTURED,\nROTATE TO NEXT TRACK")
        self.on_phrase_capture = new.instancemethod (on_phrase_capture, self, self.__class__)

        def on_track_select (self, track):
            debug_print (' Selected a track')
            feedback_mgr.reset_feedback_timer (self.last_feedback, 0)
        self.on_track_select = new.instancemethod (on_track_select, self, self.__class__)


    def axe_button_test (self, func, feedback_note, feedback_len, bank):
        global next_func
        next_func = func
        debug_print (' In AXE_BUTTON_TEST state')
        self.activator_control ('enable')        # Show the activator
        # Warn every 3 bars if no input
        self.last_feedback = feedback_mgr.setup_timed_feedback (2, feedback_note, bank, feedback_len)

        def on_axe_stick (self):
            debug_print (' Got axe button action')
            feedback_mgr.cancel_timed_feedback (self.last_feedback, 0)
            delay_trans (0, next_func)
            self.restore_attrs ()
        self.on_axe_stick = new.instancemethod (on_axe_stick, self, self.__class__)

    def sample_button_test (self, func, feedback_note, feedback_len, bank):
        global next_func
        next_func = func
        debug_print (' In SAMPLE_BUTTON_TEST state')
        self.activator_control ('enable')        # Show the activator
        # Warn every 3 bars if no input
        self.last_feedback = feedback_mgr.setup_timed_feedback (3, feedback_note, bank, feedback_len)

        # Should be something else here...
        def on_axe_stick (self):
            debug_print (' Got sample button press')
            feedback_mgr.cancel_timed_feedback (self.last_feedback, 0)
            delay_trans (0, next_func)
            self.restore_attrs ()
        self.on_axe_stick = new.instancemethod (on_axe_stick, self, self.__class__)


    ##############################  WELCOME GAME  #############################

    def start_game (self):
        global consecutive_hits, consecutive_misses, consecutive_passes
        global consecutive_phrases
        debug_print (' In START state')

        consecutive_hits = consecutive_misses = consecutive_passes = 0
        consecutive_phrases = 0
        
        hx.seeker (0)            # Disable the seeker and phrase thread
        hx.activator (0)         # Disable the activator
        hx.sections (0)          # Disable the section boundaries
        hx.freeze_juice (1)      # Freeze the juice meter

        # Midi: Welcome DJ... to the world of Frequency, a techno...
        delay_trans (3.5, 'play_voice (12, 0)')
        delay_trans (4, 'current_level.tunnel()')

    def tunnel (self):
        debug_print (' In TUNNEL state')

        # Midi: On the walls of this tunnel, you will see streams of...
        delay_trans (4.7, 'play_voice (13, 0)')
        delay_trans (7.45, 'current_level.activator()')

    ##############################  CATCHING  ##############################

    def activator (self):
        debug_print (' In ACTIVATOR state.')
        
        # Midi: This is your Frequency Activator, the modern...
        play_voice (14, 0)
        self.advance_section ()             # advance to next section
        hx.display_text ('ACTIVATOR')
        self.highlight_animate ('activator')
        #self.blink_item ('hx.activator(1)', 'hx.activator(0)', 0.1, 1, 'on')
        #hx.nowring (1)
        delay_trans (2.7, 'current_level.catch_3()')
        debug_print (' Done processing ACTIVATOR state.')

    def catch_3 (self):
        # Midi: As notes pass through the Activator....
        debug_print (' In CATCH_3 state.')
        play_voice (15, 0)
        hx.activator_label (1)
        delay_trans (2.5, ('current_level.catch_test (0.5, \'current_level.catch_done()\', 0)'))
        # Disable feedback until instructions are done.
        self.disable_feedback_midi ()
        delay_trans (3, 'current_level.enable_feedback_midi ()')

    def catch_done (self):
        # Excellent...
        play_voice (21, 0)
        debug_print (' In CATCH_DONE state.')
        delay_trans (1.5, 'current_level.activation_1()')

    ##############################  ACTIVATION  ##############################

    def activation_1 (self):
        debug_print (' In ACTIVATION_1 state')
        self.advance_section ()
        # Midi: Play two bars of music in a row without...
        play_voice (12, 1)
        delay_trans (2, 'hx.seeker (1)') # Display the seeker and phrase thread
        delay_trans (4, 'current_level.activation_2()')

    def activation_2 (self):
        debug_print (' In ACTIVATION_2 state')
        self.advance_section ()
        #delay_trans (2, 'current_level.activation_done ()')
        delay_trans (2, 'current_level.activation_test(1, 0, \'current_level.activation_done()\', 19, 1.5, 1, 16)')
        # Disable feedback until instructions are done.
        #self.disable_feedback_midi ()
        #delay_trans (4.5, 'current_level.enable_feedback_midi ()')
        
    def activation_done (self):
        # Midi: Excellent!  You just activated the drum track...
        play_voice (13, 1)
        hx.activator_label (0)
        hx.display_text (' DRUM TRACK ACTIVATED!')
        debug_print (' In ACTIVATION_DONE state')
        delay_trans (4, 'current_level.rotation_1()')

    ##############################  ROTATION  ##############################

    def rotation_1 (self):
        # Midi: Now that you've activated the drums, we can...
        play_voice (14, 1)
        debug_print (' In ROTATION_1 state')

        delay_trans (2.7, 'hx.track_ctrl (\'enable\', 1)') # enable 2nd track 

        # Midi: Use the d-pad now to rotate...
        delay_trans (3.7, 'play_voice (15, 1)')
        delay_trans (6.8, 'hx.display_text (\'MOVE TO THE BASS TRACK\')')
        delay_trans (6.8, 'current_level.rotation_test([1], 0, \'current_level.rotation_4()\', 15, 3, 3, 1)')

    # rotation test here.

    def rotation_4 (self):
        debug_print (' In ROTATION_4 state')
        # Midi: You are now on the bass track.  Try to play...
        play_voice (12, 2)
        delay_trans (2.3, 'current_level.activation_test(1, 0, \'current_level.rotation_done()\', 19, 1.5, 2, 18)')
        # Disable feedback until instructions are done.
        self.disable_feedback_midi ()
        delay_trans (3.2, 'current_level.enable_feedback_midi ()')

    def rotation_done (self):
        # Midi: Excellent, you just activated the bass track! Let's...
        play_voice (13, 2)
        hx.display_text ('BASS TRACK ACTIVATED!')
        debug_print (' In ROTATION_DONE state')
        delay_trans (3, 'current_level.section_1()')

    ##############################  SECTIONS  ##############################

    def section_1 (self):
        # Midi: Songs in Frequency are separated into different...
        play_voice (14, 2)
        self.deal_with_sections (1)              # 2nd section is section 1
        self.disable_feedback_midi ()
        debug_print (' In SECTION_1 state')
        # FIXME: May want to wait for the next section...
        delay_trans (4, 'current_level.section_2()')


    # This is an atrocious hack to deal with timing the section boundaries...
    def deal_with_sections (self, cur_section):
        assert cur_section < 4

        song_bar = hx.clock ('song_bar')
        for i in self.section_boundaries:
            if song_bar < i:
                next_sec_start = i - song_bar
                break
            j = i

        cur_sec_size = i - j
        debug_print (" Song bar,    Cur sec size,    Next sec start ")
        debug_print (song_bar)
        debug_print (cur_sec_size)
        debug_print (next_sec_start)

        if next_sec_start > 2:
            debug_print (' 3 or more bars to next boundary.')
            self.disable_feedback_midi ()
            self.advance_section ()
            self.show_section_boundaries ()
            delay_trans (next_sec_start + 1,
                         'current_level.hide_section_boundaries ()')
            delay_trans (next_sec_start, 'current_level.enable_feedback_midi ()')
            delay_trans (next_sec_start - 1, 'current_level.activation_test(2, 1, \'current_level.section_done()\', 19, 1.5, 2, 18)')
        else:
            debug_print (' less than 3 bars to next boundary, waiting...')
            debug_print (next_sec_start + 1)
            self.disable_feedback_midi ()
            delay_trans (next_sec_start + 1,
                         'current_level.advance_section ()')
            delay_trans (next_sec_start + 1,
                         'current_level.show_section_boundaries ()')
            delay_trans (cur_sec_size + next_sec_start + 1,
                         'current_level.hide_section_boundaries ()')
            delay_trans (cur_sec_size + next_sec_start, 'current_level.enable_feedback_midi ()')
            delay_trans (cur_sec_size + next_sec_start - 1, 'current_level.activation_test(2, 1, \'current_level.section_done()\', 19, 1.5, 2, 18)')
    
    def section_2 (self):
        # Midi: New sections contain new music.  Rotate around and...
        play_voice (15, 2)
        debug_print (' In SECTION_2 state')
        delay_trans (3.8, 'current_level.enable_feedback_midi ()')

    def section_done (self):
        # Midi: Excellent, you're in total control.  A few more things...
        play_voice (17, 2)
        hx.input ('disable', 0, 'rotL')
        hx.input ('disable', 0, 'rotR')
        debug_print (' In SECTION_DONE state')
        delay_trans (1.5, 'current_level.hud_1()')

    ##############################  HUD  ##############################

    def hud_1 (self):
        debug_print (' In HUD_1 state')
        hx.add_juice (20)          # Add a bunch of juice before showing meter
        # Midi: Now I shall turn on your Heads Up Display.
        play_voice (13, 3)
                
        delay_trans (1.7, 'hx.freeze_juice (0)')
        delay_trans (1.7, 'current_level.highlight_animate (\'energy\')')
        # Midi: This is your energy meter.
        delay_trans (1.7, 'play_voice (14, 3)')

        delay_trans (6.2, 'hx.freeze_juice (1)')
        delay_trans (6.2, 'current_level.highlight_animate (\'progress\')')
        # Midi: This icon tells you your location within...
        delay_trans (6.2, 'play_voice (15, 3)')

        delay_trans (11.7, 'current_level.highlight_animate (\'score\')')
        # Midi: This is you score display...
        delay_trans (11.7, 'play_voice (16, 3)')

        # Midi: These are the basic instructions of Freq...
        delay_trans (16.2, 'play_voice (12, 4)')
        delay_trans (19.2, 'current_level.scratch_1()')

    #############################  SCRATCH TRACK  ############################

    def scratch_1 (self):
        debug_print (' In SCRATCH_1 state')
        # Midi: On freestyle tracks, there are...
        play_voice (13, 4)
        
        delay_trans (2.6, 'hx.track_ctrl (\'enable\', 2)')  # Enable 3rd track 

        delay_trans (4.6, 'hx.display_text (\'MOVE TO FREESTYLE TRACK\')')
        delay_trans (4.6, 'current_level.rotation_test([2], 0, \'current_level.scratch_2()\', 14, 2, 3, 4)')

    # rotation test here...

    def scratch_2 (self):
        debug_print (' In SCRATCH_2 state')
        # Midi: This type of freestyle track is called a Scratch...
        play_voice (15, 4)
        hx.input ('enable', 0, 'rpch')
        hx.input ('enable', 0, 'axfx')
        hx.input ('enable', 0, 'regi')
        hx.display_text ('FREESTYLE: SCRATCH')
        #self.blink_item ('hx.activator(1)', 'hx.activator(0)', 0.1, 3, 'on')
        delay_trans (4, 'current_level.scratch_3()')

    def scratch_3 (self):
        # Midi: You can scratch on this track just like on a turntable
        play_voice (16, 4)
        debug_print (' In SCRATCH_3 state')
        self.activator_control ('enable')
        self.disable_feedback_midi ()
        delay_trans (3.5, 'current_level.enable_feedback_midi()')
        delay_trans (1, 'current_level.axe_button_test (\'current_level.scratch_wait()\', 16, 3, 4)')

    # axe button test

    def scratch_wait (self):
        debug_print (' In SCRATCH_WAIT state')
        # Using 3.5 here so that the previous vocal has time to finish...

        # Midi: Press the buttons on the controller to...
        delay_trans (3.5, 'play_voice (17, 4)')
        delay_trans (9.5, 'current_level.axe_1()')

    ##############################  AXE TRACK  ##############################

    def axe_1 (self):
        debug_print (' In AXE_1 state')
        # Midi: This is one more type of freestyle track, ...
        play_voice (12, 5)
        
        delay_trans (2, 'hx.track_ctrl (\'enable\', 3)')     # enable 4th track
        # The rest of the game enables freestyle tracks for this amount of time
        delay_trans (2, 'hx.enable_freestyle (0, 10000000)')
        delay_trans (3.8, 'current_level.rotation_test([3], 0, \'current_level.axe_2()\', 13, 2, 3, 5)')

    # rotation test here...

    def axe_2 (self):
        debug_print (' In AXE_2 state')
        # Midi: Notice again that the Activator has been replaced...
        play_voice (14, 5)
        hx.set_volume ('score', 2, 80)       # Lower scratch volume
        hx.display_text ('FREESTYLE: AXE')

        def on_axe_stick (self):
            debug_print (' Got axe button action')
            self.should_test = 0
            self.restore_attrs ()
        self.on_axe_stick = new.instancemethod (on_axe_stick, self, self.__class__)

        delay_trans (6, 'current_level.axe_3()')

    def axe_3 (self):
        debug_print (' In AXE_3 state')
        # Midi: Move the left analog stick left and right...
        play_voice (15, 5)
        if self.should_test == 0:
            delay_trans (3, 'current_level.axe_done()')
        else:
            self.should_test = 1
            delay_trans (3, 'current_level.axe_button_test(\'current_level.axe_done()\', 15, 2, 5)')

    def axe_done (self):
        debug_print (' In AXE_done state')
        delay_trans (2, 'current_level.last_word()')

    ################################ FINISH UP ###############################
    def last_word (self):
        debug_print (' In LAST_WORD state')
        play_voice (12, 6)
        delay_trans (2, 'hx.display_text (\'TUTORIAL COMPLETED!\')')
        delay_trans (4, 'current_level.tutorial_done()')

    def tutorial_done (self):
        debug_print (' In TUTORIAL_DONE state')
        hx.stop_game ()

    ###########################################################################

def get_class_name ():
    return TutorialGameLevel
