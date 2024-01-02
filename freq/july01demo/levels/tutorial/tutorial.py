#******************************************************************************
#
# Copyright (c) 1995-2001 Harmonix Music Systems
# All rights reserved
#
#******************************************************************************

import hx

# globals used to maintain state when we redefine functions...
consecutive_hits = 0
consecutive_misses = 0
next_func = ''
next_func_delay = 0
goal_tracks = []

feedback_enabled = 1
feedback_buffer = 0.1

last_note = 11

feedback_mgr = None

# Debug printing...  use print on PS2, hx.trace on PC
def debug_print (text):
    pass
    #print text         # Doesn't work on PC, but does on PS2
    #hx.trace (text)    # Works on PC, but blue screen on PS2 throws off timing

# Call function 'script', after 'bars' bars have passed
def delay_trans (bars, script):
    when = bars * 1920 + hx.clock ('tick')
    hx.post_script (when, script)

def play_voice (note):
    global last_note
    
    #debug_print ('*****play_voice - ')
    #debug_print (note)
    #hx.stop_midi ('voice', last_note)
    hx.play_midi ('voice', note, 127)
    last_note = note
    delay_trans (0.3, 'hx.stop_midi (\'voice\', last_note)')

#  This sucks...  It's a terrible hack, but the fastest way to do things now.
def set_feedback_enabled (value):
    feedback_enabled = value

###############################################################################
#
# The following classes and functions deal with timed voice feedback.
# setup_timed_feedback    causes a 'note to fire every 'time' bars
# cancel_timed_feedback   will stop the feedback
# reset_idle_time        will reset the timer, but won't stop the feedback
#
class TimedFeedback:
    def __init__ (self):
        self.note = 0
        self.time_limit = 0
        self.note_length  = 0
        self.idle_time = 0
        self.id = 0
        self.note_start_time = 0

    def reset_idle_time (self, with_feedback):
        #debug_print (' Reset the idle timer')
        if with_feedback == 0:
            self.idle_time = min(0, self.idle_time)
        elif with_feedback == 1:
            self.idle_time = 0 - self.note_length

    def play_feedback (self):
        global feedback_enabled

        feedback_enabled = 0
        delay_trans (self.note_length, 'set_feedback_enabled (1)')
        self.note_start_time = float(hx.clock ('tick')) / float(1920)
        self.reset_idle_time (1)
        play_voice (self.note)
        #current_level.disable_feedback_midi ()
        #delay_trans (self.current_level.disable_feedback_midi ()
        #debug_print (' FEEDBACK!!!')

class TimedFeedbackMgr:
    def __init__ (self):
        self.last_id = 0       # for assigning ids to timed feedback requests
        self.feedback = []     # timed feedback instances
        self.keep_time = 0     # keep track of time

    # just reinitialize our member variables...
    def reset_feedback_system (self):
        self.feedback = []
        self.last_id = 0
        self.keep_time = 0

    # Check the current time, and see if we need to keep checking time.
    def check_time (self):
        # if there are no timed feedback instances, then don't track time
        if len (self.feedback) == 0:
            self.keep_time = 0
            return
        delay_trans (0.5, 'feedback_mgr.check_time()')
        #debug_print (' Checked time...')
        for fb in self.feedback:
            #debug_print (' id,   idle_time,   time_limit')
            #debug_print (fb.id)
            #debug_print (fb.idle_time)
            #debug_print (fb.time_limit)

            if fb.idle_time > fb.time_limit:
                #debug_print ('   and it\'s over the feedback level')
                fb.play_feedback ()
            else:
                fb.idle_time = fb.idle_time + 0.5
    
    #def warn (self, feedback):

    def stop_warn (self, feedback):
        hx.stop_midi ('voice', feedback.note)

    def start_checking_time (self):
        if self.keep_time == 1:
            return
        else:
            #debug_print (' Start the check_time callback')
            self.keep_time = 1
            delay_trans (0.5, 'feedback_mgr.check_time ()')

    def stop_checking_time (self):
        #debug_print (' Stop the check_time callback')
        self.keep_time = 0

    def setup_timed_feedback (self, time, note, note_len):
        debug_print (' Setting up timed feedback...')
        x = TimedFeedback ()
        x.time_limit = time
        x.note = note
        x.note_length = note_len
        x.id = self.last_id
        self.last_id = self.last_id + 1
        x.reset_idle_time (0)
        self.feedback.append (x)
        self.start_checking_time ()
        return x.id

    def cancel_timed_feedback (self, fb_id, stop_voice = 1):
        debug_print (' Cancelling timed feedback...')
        i = 0
        for fb in self.feedback:
            if fb_id == fb.id:
                #if stop_voice == 1:
                #self.stop_warn (fb)
                del (self.feedback[i])
                break
            i = i + 1

    def get_fb_note_time_left (self, fb_id):
        for fb in self.feedback:
            if fb_id == fb.id:
                # The note_length plus the note_start_time will give us the
                #  time that the note is due to end.  From that, subtract the
                #  current time and add a small buffer to determine the 
                #  number of bars until the note will be done.
                debug_print (fb.note_length)
                debug_print (fb.note_start_time)
                debug_print (float(hx.clock('tick'))/float(1920))
                debug_print (feedback_buffer)
                result = fb.note_length + fb.note_start_time - (float(hx.clock('tick')) / float(1920)) + feedback_buffer
                # if no feedback has been played(1st case), or feedback was
                #  played, but a while ago, then the note's time to
                #  completion is 0.  Otherwise, it's the above equation's sol.
                if fb.note_start_time == 0 or result < 0:
                    return 0
                else:
                    return result

    def reset_feedback_timer (self, fb_id, with_fb):
        for fb in self.feedback:
            if fb_id == fb.id:
                fb.reset_idle_time (with_fb)

class TutorialLevel (Level):
    def __init__ (self):

        Level.__init__(self)
        global feedback_mgr
        feedback_mgr = TimedFeedbackMgr ()
        
        self.directory_name = 'Tutorial'
        self.short_name = 'tutor'
        # Not sure what other methods are necessary in here...

        self.initial_points = [ 20, 20, 20 ]
        self.max_points     = [ 20, 20, 20 ]

        self.section_boundaries = [14, 16, 24, 30, 38]
        
        self.track_enable_criteria = ('yes', 6, 6, 6, 6, 6, 6, 6)
        self.game_bg_criteria = ('yes','yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes',(1,2), 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.section_names =  ['section 0', 'section 1', 'section 2', 'section 3', 'DONE']
        self.fx_filt_period = (1920, 960,  1920, 480,  1920, 960,  1920, 960)
        self.fx_stt         = (120, 0)
        self.fx_volume      = 50
        self.stage_num      = 0
        self.num_laps       = [ 10, 10, 10, 10 ]

        self.materials = ("drum",
                          "bass",
                          "lead",
                          "lead",
                          "synth",
                          "synth",
                          "synth",
                          "synth")

        self.feedback_midi = 1
        self.toggle_miss_note = 18

        self.last_feedback = 0

        self.got_goal_action = 0

        self.act_enabled = 0
        self.act_showing = 0
        self.act_flash_rate = 0.125
        self.num_tracks_left = 0
        self.num_tracks_act = 0

        self.is_tutorial = 1
        self.should_test = 1

    def get_is_tutorial (self):  return self.is_tutorial
    def get_name (self):         return "Game Tutorial"
    def get_artist (self):       return "DJ Kasson"
    def get_genre (self):        return "Techno"
    def get_tempo (self):        return "130"
    def get_description (self):  return "Use this FreQ Training Program to learn the skillz necessary to become a Frequency champion."

    def get_section_boundaries (self):
        return self.section_boundaries

    def wacko_panning (self):   return 0

    def is_avail_game (self):    return 1
    def is_avail_jam (self):     return 0
    # Turn on a hardware effect for the given core?  1 for yes, 0 for no
    def ps2_use_hard_effect (self, core):
        return 1

    # What hardware effect to use on the given core?  Valid values are
    # 'room', 'studio a', 'studio b', 'studio c', 'hall', 'space',
    # 'echo', 'delay', 'pipe'
    def ps2_hard_effect_name (self, core):
        if core == 0:
            return 'echo'                 # Core 0 uses echo
        else:
            return 'delay'                # Core 1 uses delay

    # What volumes (left and right) should the effect be at for the given core?
    # Scale is 0-127
    def ps2_hard_effect_volumes (self, core):
            return [40, 40]               # Both cores have volumes of 40
        
    # What is the delay time for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_delay_time (self, core):
        if core == 0:
            return 127                    # Core 0 has delay time of 127
        else:
            return 117                    # Core 1 has delay time of 117

    # What is the feedback value for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_feedback (self, core):
        if core == 0:
            return 25                   # core 0: 25
        else:
            return 45                   # core 1: 45

    #**************************************************************************
    # Tutorial script code...
    #
    def restore_attrs (self):
        # Delete all the new 'on_*' methods attached to our own object,
        # so that further calls will get the one in the object's class.
        for k in self.__dict__.keys():
            if k[:3] == 'on_':
                delattr (self, k)

    # Start the tutorial state machine going...
    def on_game_begin (self):
        #self.test_bank (28, 70, 5)
        feedback_mgr.reset_feedback_system ()
        
        if ruleset == 'game':
            self.start_game ()
        elif ruleset == 'jam':
            self.start_remix ()

    # When the game is over, show all of the hud items and activator again.
    def on_game_over (self):
        debug_print (' GAME OVER...  Resetting graphics')
        # Undo some game stuff that we changed throughout the tutorial
        #  These all effect the game outside of this level.
        hx.seeker (1)            # Enable the seeker and phrase thread
        hx.activator (1)         # Enable the activator
        hx.nowring (1)           # Enable the now ring
        hx.sections (1)          # Enable the section boundaries
        hx.juice_meter (1)       # Enable the juice meter
        hx.score_meter (1)       # Enable the score display
        hx.progress_meter (1)    # Enable the progress meter
        hx.freeze_juice (0)      # Unfreeze the juice meter

        # redefine any previously redefined methods with their original
        #  functionality
        self.restore_attrs ()
    
    #*************************************************************************
    #
    #  Functions that represent states of the game tutorial:
    #

    ############################# UTILITY FUNCS ##############################

    def blink_item (self, func_on, func_off, period, duration):
        assert period < duration
        double_period = period * 2

        # post the enable item messages first
        seed_on = 0
        while seed_on < duration:
            seed_on = seed_on + double_period
            delay_trans (seed_on, func_on)

        # post the disable item messages next
        seed_off = period
        while seed_off < duration:
            seed_off = seed_off + double_period
            delay_trans (seed_off, func_off)

        # Make sure that the last thing we do is turn on the item
        if seed_off > seed_on:
            delay_trans (seed_off, func_on)
        else:
            delay_trans (seed_on, func_on)

    # Disable and enable feedback in looping functions.  These are useful
    #  when there are important voice-over instructions playing, and we don't
    #  want to interrupt them with less meaningful messages.
    def disable_feedback_midi (self):
        debug_print (' Disabling feedback')
        self.feedback_midi = 0

    def enable_feedback_midi (self):
        debug_print (' Enabling feedback')
        self.feedback_midi = 1

    def hide_section_boundaries (self):
        hx.sections (0)

    def show_section_boundaries (self):
        hx.sections (1)

    # Stop looping in the current section and advance to the next one
    def advance_section (self):
        hx.advance_section (hx.clock('tick'))
    
    # Enable and disable the activator by making it semi-transparent and
    #  flash.
    def activator_control (self, state):
        if state == 'enable':
            self.act_enabled = 1
            hx.fade_activator (1.0)
            hx.activator (1)
            
        elif state == 'disable':
            self.act_enabled = 0
            delay_trans (0, 'current_level.flash_activator()')
    
    def flash_activator (self):
        if self.act_enabled == 0:
            if self.act_showing == 1:
                self.act_showing = 0
                hx.fade_activator (0.75)
            elif self.act_showing == 0:
                self.act_showing = 1
                hx.fade_activator (0.4)
            delay_trans (self.act_flash_rate, 'current_level.flash_activator()')

    #########################  LOOPING STATES  #########################
    #  i.e. states that require specific input to move on...
    #

    #
    # Test the user's ability to catch consecutive gems on the track specified
    # If the user passes, then call func, otherwise stay here...
    #
    def catch_test (self, func_delay, func):
        global consecutive_hits, next_func, next_func_delay
        consecutive_hits = 0
        next_func = func
        next_func_delay = func_delay
        hx.input ('enable', 0, 'rpch')      # Enable catching
        # Warn every 3 bars if no input
        self.last_feedback = feedback_mgr.setup_timed_feedback (3, 19, 1)
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
                    delay_trans (0.08, 'play_voice (20)')
                debug_print (' Not enough hits yet.')
            elif consecutive_hits == 3:
                hx.input ('disable', 0, 'rpch')     # Disable catching
                time_left = feedback_mgr.get_fb_note_time_left (self.last_feedback)
                feedback_mgr.cancel_timed_feedback (self.last_feedback)
                
                # Midi: Excellent!  Let's continue.
                #debug_print (' Got the hits...  let\'s move on')
                self.activator_control ('disable')
                #debug_print (next_func_delay)
                #debug_print (time_left)
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
                # Midi: Keep trying, you'll get it... feel the beat, and...
                if self.feedback_midi == 1:
                    if self.toggle_miss_note == 17:
                        delay_trans (0.08, 'play_voice (17)')
                        self.toggle_miss_note = 18
                    else:
                        delay_trans (0.08, 'play_voice (18)')
                        self.toggle_miss_note = 17
                consecutive_misses = 0
        self.on_miss = new.instancemethod (on_miss, self, self.__class__)

        debug_print (' In CATCH_TEST state')

    
    #
    # Can the user capture a phrase???
    #
    def activation_test (self, num_tracks, func_delay, func):
        global next_func, next_func_delay
        next_func = func
        next_func_delay = func_delay
        self.num_tracks_left = num_tracks
        self.num_tracks_act = 0

        debug_print (' In ACTIVATION_TEST state')
        hx.input ('enable', 0, 'rpch')
        hx.input ('enable', 0, 'rotR')
        hx.input ('enable', 0, 'rotL')
        self.activator_control ('enable')        # Show the activator
        # Warn every 3 bars if no input
        self.last_feedback = feedback_mgr.setup_timed_feedback (3, 19, 1)
        debug_print (self.last_feedback)

        def on_miss (self):
            debug_print ('  We have a miss')
            global consecutive_phrases, consecutive_misses, consecutive_passes
            feedback_mgr.reset_feedback_timer (self.last_feedback, 0)

            consecutive_phrases = consecutive_passes = 0
            consecutive_misses = consecutive_misses + 1

            if consecutive_misses == 3:
                # Midi: Keep trying, you'll get it... feel the beat, and...
                if self.feedback_midi == 1:
                    if self.toggle_miss_note == 17:
                        delay_trans (0.08, 'play_voice (17)')
                        self.toggle_miss_note = 18
                    else:
                        delay_trans (0.08, 'play_voice (18)')
                        self.toggle_miss_note = 17
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

    #
    # Wait until the user rotates one of the correct tracks
    #  <track_list> = track numbers that the user should rotate to.
    #  <func_delay> = # of bars to wait before calling func
    #  <func> = function that should be called after passing test
    #  <play_feedback> = 0: play no midi, 1: play midi feedback
    #
    def rotation_test (self, track_list, func_delay, func, note, note_length):
        global next_func, next_func_delay, goal_tracks
        next_func = func
        next_func_delay = func_delay
        goal_tracks = track_list
        debug_print (goal_tracks)
        debug_print (' In ROTATION_TEST state')

        self.activator_control ('enable')   # Show the activator
        hx.input ('enable', 0, 'rotR')      # Enable rotation right
        hx.input ('enable', 0, 'rotL')      # Enable rotation left
        self.last_feedback = feedback_mgr.setup_timed_feedback (2, note, note_length)
        debug_print (self.last_feedback)

        def on_track_select (self, track):
            debug_print (' Selected a track')
            debug_print (track)
            feedback_mgr.reset_feedback_timer (self.last_feedback, 0)
            for i in goal_tracks:
                if track == i:
                    debug_print (' We\'re on the right track...')
                    time_left = feedback_mgr.get_fb_note_time_left (self.last_feedback)
                    feedback_mgr.cancel_timed_feedback (self.last_feedback)
                    hx.input ('disable', 0, 'rotL')     # Disable rotation left
                    hx.input ('disable', 0, 'rotR')     # Disable rotation right
                    self.activator_control ('disable')  # Hide the activator
                    #debug_print (next_func_delay)
                    #debug_print (time_left)
                    delay_trans (next_func_delay + time_left, next_func)
                    self.restore_attrs ()
        self.on_track_select = new.instancemethod (on_track_select, self, self.__class__)

    def axe_button_test (self, func, feedback_note, feedback_len):
        global next_func
        next_func = func
        debug_print (' In AXE_BUTTON_TEST state')
        #hx.input ('enable', 0, 'regi')
        #hx.input ('enable', 0, 'axfx')
        self.activator_control ('enable')        # Show the activator
        # Warn every 3 bars if no input
        self.last_feedback = feedback_mgr.setup_timed_feedback (2, feedback_note, feedback_len)

        def on_axe_stick (self):
            debug_print (' Got axe button action')
            feedback_mgr.cancel_timed_feedback (self.last_feedback, 0)
            delay_trans (0, next_func)
            self.restore_attrs ()
        self.on_axe_stick = new.instancemethod (on_axe_stick, self, self.__class__)

    def sample_button_test (self, func, feedback_note, feedback_len):
        global next_func
        next_func = func
        debug_print (' In SAMPLE_BUTTON_TEST state')
        #hx.input ('enable', 0, 'rpch')
        self.activator_control ('enable')        # Show the activator
        # Warn every 3 bars if no input
        self.last_feedback = feedback_mgr.setup_timed_feedback (3, feedback_note, feedback_len)

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

        consecutive_hits = consecutive_misses = consecutive_passes = 0
        consecutive_phrases = 0
        
        delay_trans (3.5, 'current_level.first_words()')
        hx.seeker (0)            # Disable the seeker and phrase thread
        hx.activator (0)         # Disable the activator
        hx.nowring (0)           # Disable the now ring
        hx.sections (0)          # Disable the section boundaries
        hx.juice_meter (0)       # Disable the juice meter
        hx.score_meter (0)       # Disable the score display
        hx.progress_meter (0)    # Disable the progress meter

        debug_print (' In START state')

    def first_words (self):
        # Midi: Welcome DJ... to the world of Frequency, a techno...
        play_voice (12)
        debug_print (' In FIRST_WORDS state')
        delay_trans (0.5, 'current_level.tunnel()')

    def tunnel (self):
        debug_print (' In TUNNEL state')
        hx.input ('disable', 0, 'rotL')     # Disable rotation left
        hx.input ('disable', 0, 'rotR')     # Disable rotation right
        hx.input ('disable', 0, 'rpch')     # Disable catching
        hx.input ('disable', 0, 'regi')     # 
        hx.input ('disable', 0, 'axfx')     # 
        hx.input ('disable', 0, 'advn')     # Disable advance section
        hx.input ('disable', 0, 'loop')     # Disable loop tool
        delay_trans (4.7, 'current_level.catch_1()')
        #delay_trans (4.7, 'current_level.scratch_1()')

    ##############################  CATCHING  ##############################

    def catch_1 (self):
        # Midi: On the walls of this tunnel, you will see streams of...
        play_voice (13)
        debug_print (' In CATCH_1 state.')
        delay_trans (2.75, 'current_level.activator()')

#    def catch_2 (self):
#        debug_print (' In CATCH_2 state.')
#        delay_trans (1, 'current_level.activator()')
#
    def activator (self):
        debug_print (' In ACTIVATOR state.')
        
        # Midi: This is your Frequency Activator, the modern...
        play_voice (14)
        self.advance_section ()             # advance to next section
        hx.display_text ('ACTIVATOR')
        self.blink_item ('hx.activator(1)', 'hx.activator(0)', 0.1, 1)
        hx.nowring (1)
        delay_trans (2.7, 'current_level.catch_3()')
        debug_print (' Done processing ACTIVATOR state.')

    def catch_3 (self):
        # Midi: As notes pass through the Activator....
        debug_print (' In CATCH_3 state.')
        play_voice (15)
        hx.activator_label (1)
        delay_trans (2.5, ('current_level.catch_test (0.5, \'current_level.catch_done()\')'))
        # Disable feedback until instructions are done.
        self.disable_feedback_midi ()
        delay_trans (3, 'current_level.enable_feedback_midi ()')

    def catch_done (self):
        play_voice (21)
        debug_print (' In CATCH_DONE state.')
        delay_trans (1.5, 'current_level.activation_1()')

    ##############################  ACTIVATION  ##############################

    def activation_1 (self):
        debug_print (' In ACTIVATION_1 state')
        self.advance_section ()
        # Midi: Play two bars of music in a row without...
        delay_trans (2.5, 'hx.seeker (1)') # Display the seeker in a little bit
        play_voice (22)
        delay_trans (4, 'current_level.activation_2()')

    def activation_2 (self):
        debug_print (' In ACTIVATION_2 state')
        self.advance_section ()
        delay_trans (2, 'current_level.activation_test(1, 0, \'current_level.activation_done()\')')
        # Disable feedback until instructions are done.
        self.disable_feedback_midi ()
        delay_trans (4.5, 'current_level.enable_feedback_midi ()')
        
    def activation_done (self):
        # Midi: Excellent!  You just activated the drum track...
        play_voice (23)
        hx.activator_label (0)
        hx.display_text (' DRUM TRACK ACTIVATED!')
        debug_print (' In ACTIVATION_DONE state')
        delay_trans (4, 'current_level.rotation_1()')

    ##############################  ROTATION  ##############################

    def rotation_1 (self):
        # Midi: Now that you've activated the drums, we can...
        play_voice (24)
        debug_print (' In ROTATION_1 state')
        delay_trans (2.7, 'current_level.rotation_2()')

    def rotation_2 (self):
        hx.track_ctrl ('enable', 1)      # enable the 2nd track 
        debug_print (' In ROTATION_2 state')
        delay_trans (1.0, 'current_level.rotation_3()')

    def rotation_3 (self):
        # Midi: Each wall of the tunnel is a different musical...
        play_voice (25)
        debug_print (' In ROTATION_3 state')
        #self.activator_control ('enable')
        delay_trans (3.1, 'hx.display_text (\'MOVE TO THE BASS TRACK\')')
        delay_trans (3.1, 'current_level.rotation_test([1], 0, \'current_level.rotation_4()\', 26, 5)')

    # rotation test here.

    def rotation_4 (self):
        debug_print (' In ROTATION_4 state')
        #self.activator_control ('disable')
        # Midi: You are now on the bass track.  Try to play...
        play_voice (27)
        delay_trans (2.3, 'current_level.activation_test(1, 0, \'current_level.rotation_done()\')')
        # Disable feedback until instructions are done.
        self.disable_feedback_midi ()
        delay_trans (3.2, 'current_level.enable_feedback_midi ()')

    def rotation_done (self):
        # Midi: Excellent, you just activated the bass track! Let's...
        play_voice (28)
        hx.display_text ('BASS TRACK ACTIVATED!')
        debug_print (' In ROTATION_DONE state')
        delay_trans (3, 'current_level.section_1()')

    ##############################  SECTIONS  ##############################

    def section_1 (self):
        #self.advance_section ()
        # Midi: Songs in Frequency are separated into different...
        play_voice (29)
        self.deal_with_sections (1)              # 2nd section is section 1
        self.disable_feedback_midi ()
        debug_print (' In SECTION_1 state')
        # FIXME: May want to wait for the next section...
        delay_trans (4, 'current_level.section_3()')


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
            delay_trans (next_sec_start - 1, 'current_level.activation_test(2, 0, \'current_level.section_6()\')')
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
            delay_trans (cur_sec_size + next_sec_start - 1, 'current_level.activation_test(2, 0, \'current_level.section_6()\')')
    
    #    def section_2 (self):
    #hx.sections (1)
    #debug_print (' In SECTION_2 state')
    #delay_trans (2, 'current_level.section_3()')

    def section_3 (self):
        # Midi: New sections contain new music.  Rotate around and...
        play_voice (30)
        debug_print (' In SECTION_3 state')
        delay_trans (3, 'current_level.section_5()')

    def section_5 (self):
        debug_print (' In SECTION_5 state')
        delay_trans (0.8, 'current_level.enable_feedback_midi ()')

    # activation test performed here...

    def section_separator (self):
        debug_print (' In SECTION_SEPARATOR state')
        hx.display_text ("TRACK CAPTURED,\nROTATE TO NEXT TRACK")
        delay_trans (0, 'current_level.rotation_test([0], 0, \'current_level.section_separator_2()\', 50, 2.0)')

    # rotation test performed here...

    def section_separator_2 (self):
        debug_print (' In SECTION_SEPARATOR state')
        delay_trans (0, 'current_level.activation_test(1, 0, \'current_level.section_6()\')')

    # another activation test performed here...

    def section_6 (self):
        debug_print (' In SECTION_6 state')
        delay_trans (1.0, 'current_level.section_done()')

    def section_done (self):
        # Midi: Excellent, you're in total control.  A few more things...
        play_voice (32)
        hx.input ('disable', 0, 'rotL')
        hx.input ('disable', 0, 'rotR')
        debug_print (' In SECTION_DONE state')
        delay_trans (1.5, 'current_level.hud_1()')

    ##############################  HUD  ##############################

    def hud_1 (self):
        debug_print (' In HUD_1 state')
        hx.add_juice (20)          # Add a bunch of juice before showing meter
        # Midi: Now I shall turn on your Heads Up Display.
        play_voice (34)
        delay_trans (1.7, 'current_level.hud_2()')
        
    def hud_2 (self):
        debug_print (' In HUD_2 state')
        self.blink_item ('hx.juice_meter(1)', 'hx.juice_meter(0)', 0.1, 1.5)
        # Midi: This is your energy meter.  Your energy is constantly...
        play_voice (35)
        delay_trans (4.5, 'current_level.hud_3()')

    def hud_3 (self):
        debug_print (' In HUD_3 state')
        hx.freeze_juice (1)
        self.blink_item ('hx.progress_meter(1)', 'hx.progress_meter(0)',
                         0.1, 1.5)
        # Midi: This icon tells you your location within...
        play_voice (36)
        delay_trans (5.5, 'current_level.hud_4()')

    def hud_4 (self):
        debug_print (' In HUD_4 state')
        self.blink_item ('hx.score_meter(1)', 'hx.score_meter(0)', 0.1, 1)
        # Midi: This is you score display...
        play_voice (37)
        delay_trans (4.5, 'current_level.hud_done()')

    def hud_done (self):
        debug_print (' In HUD_DONE state')
        # Midi: These are the basic instructions of Freq...
        play_voice (38)
        delay_trans (3, 'current_level.scratch_1()')

    #############################  SCRATCH TRACK  ############################

    def scratch_1 (self):
        debug_print (' In SCRATCH_1 state')
        # Midi: On freestyle tracks, there are...
        play_voice (39)
        delay_trans (2.6, 'current_level.scratch_2()')

    def scratch_2 (self):
        debug_print (' In SCRATCH_2 state')
        hx.track_ctrl ('enable', 2)        # Enable the 3rd track 
        delay_trans (1, 'current_level.scratch_3()')

    def scratch_3 (self):
        debug_print ('In SCRATCH_3 state')
        delay_trans (1, 'hx.display_text (\'MOVE TO FREESTYLE TRACK\')')
        #self.activator_control ('enable')
        delay_trans (1, 'current_level.rotation_test([2], 0, \'current_level.scratch_4()\', 50, 2.0)')

    # rotation test here...

    def scratch_4 (self):
        debug_print (' In SCRATCH_4 state')
        # Midi: This type of freestyle track is called a Scratch...
        play_voice (40)
        hx.input ('enable', 0, 'rpch')
        hx.input ('enable', 0, 'axfx')
        hx.input ('enable', 0, 'regi')
        hx.display_text ('FREESTYLE: SCRATCH')
        self.blink_item ('hx.activator(1)', 'hx.activator(0)', 0.1, 3)
        delay_trans (4, 'current_level.scratch_5()')

    def scratch_5 (self):
        # Midi: You can scratch on this track just like on a turntable
        #hx.set_volume ('score', 2, 60)
        play_voice (41)
        debug_print (' In SCRATCH_5 state')
        self.activator_control ('enable')
        self.disable_feedback_midi ()
        delay_trans (3.5, 'current_level.enable_feedback_midi()')
        delay_trans (1, 'current_level.axe_button_test (\'current_level.scratch_wait()\', 41, 3)')

    # axe button test

    def scratch_wait (self):
        debug_print (' In SCRATCH_WAIT state')
        # Using 3.5 here so that the previous vocal has time to finish...
        delay_trans (3.5, 'current_level.scratch_6 ()')

    def scratch_6 (self):
        # Midi: Press the buttons on the controller to...
        play_voice (48)
        debug_print (' In SCRATCH_6 state')
        delay_trans (2, 'current_level.scratch_done()')
        #delay_trans (1, 'current_level.sample_button_test (\'current_level.scratch_done ()\', 48, 1.5)')

    def scratch_done (self):
        #hx.set_volume ('score', 2, 127)
        debug_print (' In SCRATCH_DONE state')
        delay_trans (4, 'current_level.axe_1()')
    
    ##############################  AXE TRACK  ##############################

    def axe_1 (self):
        debug_print (' In AXE_1 state')
        # Midi: There's one more type of freestyle track, ...
        #hx.set_volume ('score', 2, 60)
        play_voice (42)
        delay_trans (2, 'current_level.axe_2 ()')

    def axe_2 (self):
        debug_print (' In AXE_2 state')
        hx.track_ctrl ('enable', 3)        # enable the 4th track
        hx.enable_freestyle (0, 10000000)  # Rest of the game does it this way
        delay_trans (1.8, 'current_level.rotation_test([3], 0, \'current_level.axe_3()\', 50, 2.0)')

    # rotation test here...

    def axe_3 (self):
        debug_print (' In AXE_3 state')
        # Midi: Notice again that the Activator has been replaced...
        hx.set_volume ('score', 2, 80)       # Lower scratch volume
        play_voice (43)
        hx.display_text ('FREESTYLE: AXE')

        def on_axe_stick (self):
            debug_print (' Got axe button action')
            self.should_test = 0
            self.restore_attrs ()
        self.on_axe_stick = new.instancemethod (on_axe_stick, self, self.__class__)
        delay_trans (2.75, 'current_level.axe_4()')

    def axe_4 (self):
        # Midi: Hold down any one of...
        debug_print (' In AXE_4 state')
        play_voice (49)
        delay_trans (4, 'current_level.axe_5()')

    def axe_5 (self):
        debug_print (' In AXE_5 state')
        delay_trans (2, 'current_level.axe_6()')

    def axe_6 (self):
        debug_print (' In AXE_6 state')
        # Midi: Move the left analog stick left and right...
        #hx.set_volume ('score', 3, 40)
        play_voice (44)
        if (self.should_test == 0):
            delay_trans (3, 'current_level.axe_7()')
        else:
            self.should_test = 1
            delay_trans (3, 'current_level.axe_button_test(\'current_level.axe_7()\', 44, 2)')

    def axe_7 (self):
        debug_print (' In AXE_7 state')
        delay_trans (2, 'current_level.axe_done()')

    #def axe_8 (self):
    #debug_print (' In AXE_8 state')
    # Midi: Whenever you see a freestyle track..
    #hx.set_volume ('score', 3, 40)
    #play_voice (46)
    #delay_trans (2, 'current_level.axe_done()')

    def axe_done (self):
        #hx.set_volume ('score', 2, 127)
        #hx.set_volume ('score', 3, 127)
        delay_trans (2, 'current_level.last_word()')

    ################################ FINISH UP ###############################
    def last_word (self):
        debug_print (' In LAST_WORD state')
        #hx.set_volume ('score', 2, 60)
        #hx.set_volume ('score', 3, 40)
        play_voice (47)
        delay_trans (2, 'hx.display_text (\'TUTORIAL COMPLETED!\')')
        delay_trans (4, 'current_level.tutorial_done()')

    def tutorial_done (self):
        debug_print (' In TUTORIAL_DONE state')
        #hx.input ('disable', 0, 'rpch')
        #hx.input ('disable', 0, 'regi')
        #hx.input ('disable', 0, 'axfx')
        hx.stop_game ()

    ##########################################################################
    #
    #  Functions that represent states of the remix tutorial:
    #

    ########################### LOOPING REMIX STATES #########################
    # Call with looping = 'loop' means loop mode, 'no_loop' means non-loop mode
    def pitch_test (self, looping, func_delay, func):
        global next_func, next_func_delay
        debug_print (' In PITCH_TEST state')
        next_func = func
        next_func_delay = func_delay
        hx.input ('enable', 0, 'rpch')      # Enable catching
        
        if looping == 'loop':
            feedback_note = 15
            feedback_time = 2
            feedback_length = 3
        elif looping == 'no_loop':
            feedback_note = 16
            feedback_time = 4
            feedback_length = 2
        # Warn every feedback_time bars if no input
        self.last_feedback = feedback_mgr.setup_timed_feedback (feedback_time, feedback_note, feedback_length)
        debug_print (self.last_feedback)

        def on_hit (self):
            feedback_mgr.reset_feedback_timer (self.last_feedback, 0)
            
            hx.input ('disable', 0, 'rpch')     # Disable catching
            feedback_mgr.cancel_timed_feedback (self.last_feedback)
            
            debug_print (' Pitching detected!!!')
            delay_trans (next_func_delay, next_func)
        self.on_hit = new.instancemethod (on_hit, self, self.__class__)
    
    def loop_tool_test (self, func_delay, func):
        global next_func, next_func_delay
        debug_print (' In LOOP_TOOL_TEST state')
        next_func = func
        next_func_delay = func_delay
        hx.input ('enable', 0, 'loop')      # Enable looping
        # Warn every 3 bars if no input
        self.last_feedback = feedback_mgr.setup_timed_feedback (3, 15, 1)
        debug_print (self.last_feedback)
        
        def on_toggle_loop (self):
            hx.input ('disable', 0, 'loop')     # Disable looping
            feedback_mgr.cancel_timed_feedback (self.last_feedback)
                
            debug_print (' Toggled loop tool...  let\'s move on')
            delay_trans (next_func_delay, next_func)
        self.on_toggle_loop = new.instancemethod (on_toggle_loop, self, self.__class__)
    
    def erase_test (self, func_delay, func):
        global next_func, next_func_delay
        debug_print (' In ERASE state')
        next_func = func
        next_func_delay = func_delay
        hx.input ('enable', 0, 'eras')      # Enable erasing
        # Warn every 3 bars if no input
        self.last_feedback = feedback_mgr.setup_timed_feedback (3, 15, 1)
        debug_print (self.last_feedback)
        
        def on_erase (self):
            hx.input ('disable', 0, 'eras')     # Disable looping
            feedback_mgr.cancel_timed_feedback (self.last_feedback)
                
            debug_print (' Erased track...  let\'s move on')
            delay_trans (next_func_delay, next_func)
        self.on_erase = new.instancemethod (on_erase, self, self.__class__)

    def effects_select_test (self, func_delay, func):
        global next_func, next_func_delay
        debug_print (' In EFFECTS_SELECT_TEST state')
        next_func = func
        next_func_delay = func_delay
        hx.input ('enable', 0, 'powx')      # Enable erasing
        # Warn every 3 bars if no input
        self.last_feedback = feedback_mgr.setup_timed_feedback (3, 15, 1)
        debug_print (self.last_feedback)
        
        def on_choose_powerup (self):
            hx.input ('disable', 0, 'powx')     # Disable looping
            feedback_mgr.cancel_timed_feedback (self.last_feedback)
                
            debug_print (' Selected a powerup...  let\'s move on')
            delay_trans (next_func_delay, next_func)
        self.on_choose_powerup = new.instancemethod (on_choose_powerup, self, self.__class__)

    def effects_deploy_test (self, func_delay, func):
        global next_func, next_func_delay
        debug_print (' In EFFECTS_DEPLOY_TEST state')
        next_func = func
        next_func_delay = func_delay
        hx.input ('enable', 0, 'powb')      # Enable erasing
        # Warn every 3 bars if no input
        self.last_feedback = feedback_mgr.setup_timed_feedback (3, 15, 1)
        debug_print (self.last_feedback)
        
        def on_deploy_powerup (self):
            hx.input ('disable', 0, 'powb')     # Disable looping
            feedback_mgr.cancel_timed_feedback (self.last_feedback)
                
            debug_print (' Deployed powerup...  let\'s move on')
            delay_trans (next_func_delay, next_func)
        self.on_deploy_powerup = new.instancemethod (on_deploy_powerup, self, self.__class__)

    def section_advance_test (self, func_delay, func):
        global next_func, next_func_delay
        debug_print (' In SECTION_ADVANCE_TEST state')
        next_func = func
        next_func_delay = func_delay
        hx.input ('enable', 0, 'advn')      # Enable erasing
        # Warn every 3 bars if no input
        self.last_feedback = feedback_mgr.setup_timed_feedback (3, 15, 1)
        debug_print (self.last_feedback)
        
        def on_advance_section (self):
            hx.input ('disable', 0, 'advn')     # Disable looping
            feedback_mgr.cancel_timed_feedback (self.last_feedback)
                
            debug_print (' Advanced section...  let\'s move on')
            delay_trans (next_func_delay, next_func)
        self.on_advance_section = new.instancemethod (on_advance_section, self, self.__class__)

    ############################## SPECIAL FUNCS #############################
    def listen (self, bars, func):
        debug_print (' In LISTEN state')
        delay_trans (bars, func)

    ############################## WELCOME REMIX #############################
    def start_remix (self):
        # Midi: Now that you've got the basics of Frequency's Game...
        #play_voice ()
        debug_print (' In START_REMIX state')
        delay_trans (4, 'current_level.welcome_1()')

    def welcome_1 (self):
        # Midi: Remix Mode isn't a game at all...
        #play_voice ()
        hx.input ('disable', 0, 'rotL')
        hx.input ('disable', 0, 'rotR')
        hx.input ('disable', 0, 'rpch')
        hx.input ('disable', 0, 'regi')
        hx.input ('disable', 0, 'axfx')
        hx.input ('disable', 0, 'powx')
        hx.input ('disable', 0, 'powb')
        hx.input ('disable', 0, 'advn')
        hx.input ('disable', 0, 'loop')
        #hx.input ('disable', 0, 'a')
        debug_print (' In WELCOME_1 state')
        delay_trans (1, 'current_level.welcome_2()')

    def welcome_2 (self):
        debug_print (' In WELCOME_2 state')
        # Midi: In Remix Mode, every track is a freestyle track...
        #play_voice ()
        delay_trans (1, 'current_level.pitch_1()')

    ################################ PITCHING ################################
    def pitch_1 (self):
        debug_print (' In PITCH_1 state')
        # Midi: You can think of the three Activator buttons...
        #play_voice ()
        delay_trans (1, 'current_level.pitch_2()')
    
    def pitch_2 (self):
        debug_print (' In PITCH_2 state')
        # Midi: Let's start with the drums...
        #play_voice ()
        delay_trans (1, 'current_level.pitch_test(\'no_loop\', 0, \'current_level.loop_tool_1()\')')
    
    ################################ LOOP TOOL ###############################
    def loop_tool_1 (self):
        debug_print (' In LOOP_TOOL_1 state')
        self.restore_attrs ()
        # Midi: 
        #play_voice ()
        delay_trans (1, 'current_level.loop_tool_2()')
    
    def loop_tool_2 (self):
        debug_print (' In LOOP_TOOL_2 state')
        # Midi: 
        #play_voice ()
        delay_trans (1, 'current_level.loop_tool_test(0, \'current_level.loop_tool_3()\')')
    
    def loop_tool_3 (self):
        debug_print (' In LOOP_TOOL_3 state')
        self.restore_attrs ()
        # Midi: 
        #play_voice ()
        delay_trans (1, 'current_level.pitch_test(\'loop\', 0, \'current_level.loop_tool_4()\')')
    
    def loop_tool_4 (self):
        debug_print (' In LOOP_TOOL_4 state')
        self.restore_attrs ()
        # Midi: 
        #play_voice ()
        delay_trans (1, 'current_level.listen(2, \'current_level.over_dubbing_1()\')')
    
    ############################## OVER-DUBBING ##############################
    def over_dubbing_1 (self):
        debug_print (' In OVER-DUBBING_1 state')
        # Midi: 
        #play_voice ()
        delay_trans (1, 'current_level.pitch_test(\'loop\', 0, \'current_level.over_dubbing_2()\')')
    
    def over_dubbing_2 (self):
        debug_print (' In OVER-DUBBING_2 state')
        self.restore_attrs ()
        # Midi: 
        #play_voice ()
        delay_trans (1, 'current_level.listen(2, \'current_level.erasing_1()\')')

    ###############################  ERASING  ################################
    def erasing_1 (self):
        debug_print (' In ERASING_1 state')
        # Midi: 
        #play_voice ()
        delay_trans (1, 'current_level.erasing_2()')
        ## The erase test isn't working, maybe because we don't have
        ##  remix data yet.
        #delay_trans (1, 'current_level.erase_test(0, \'current_level.erasing_2()\')')
    
    def erasing_2 (self):
        debug_print (' In ERASING_2 state')
        # Midi: 
        #play_voice ()
        delay_trans (1, 'current_level.pitch_test(\'loop\', 0, \'current_level.erasing_3()\')')
    
    def erasing_3 (self):
        debug_print (' In ERASING_3 state')
        self.restore_attrs ()
        # Midi: 
        #play_voice ()
        delay_trans (1, 'current_level.erasing_4()')
    
    def erasing_4 (self):
        debug_print (' In ERASING_4 state')
        # Midi: 
        #play_voice ()
        delay_trans (1, 'current_level.rotation_test([1], 0, \'current_level.multitrack_1()\', 50, 1.5)')

    ############################## MULTITRACKING ##############################
    def multitrack_1 (self):
        debug_print (' In MULTITRACK_1 state')
        self.restore_attrs ()
        # Midi: 
        #play_voice ()
        delay_trans (1, 'current_level.pitch_test(\'no_loop\', 0, \'current_level.multitrack_2()\')')
    
    def multitrack_2 (self):
        debug_print (' In MULTITRACK_2 state')
        self.restore_attrs ()
        # Midi: 
        #play_voice ()
        delay_trans (1, 'current_level.pitch_test(\'loop\', 0, \'current_level.multitrack_3()\')')
    
    def multitrack_3 (self):
        debug_print (' In MULTITRACK_3 state')
        self.restore_attrs ()
        # Midi: 
        #play_voice ()
        delay_trans (1, 'current_level.listen(2, \'current_level.effects_1()\')')
    
    ################################  EFFECTS  ################################
    def effects_1 (self):
        debug_print (' In EFFECTS_1 state')
        # Midi: 
        #play_voice ()
        delay_trans (1, 'current_level.effects_2()')
    
    def effects_2 (self):
        debug_print (' In EFFECTS_2 state')
        # Midi: 
        #play_voice ()
        delay_trans (1, 'current_level.effects_3()')
    
    def effects_3 (self):
        debug_print (' In EFFECTS_3 state')
        # Midi: 
        #play_voice ()
        delay_trans (1, 'current_level.effects_select_test(0, \'current_level.effects_4()\')')
    
    def effects_4 (self):
        debug_print (' In EFFECTS_4 state')
        self.restore_attrs ()
        # Midi: 
        #play_voice ()
        ## Can't deploy powerups right now, probably because we aren't really
        ##  able to play a remix yet.
        #delay_trans (1, 'current_level.effects_deploy_test(0, \'current_level.effects_5()\')')
        delay_trans (1, 'current_level.effects_5()')
        
    def effects_5 (self):
        debug_print (' In EFFECTS_5 state')
        self.restore_attrs ()
        # Midi: 
        #play_voice ()
        delay_trans (1, 'current_level.listen(2, \'current_level.effects_done()\')')
    
    def effects_done (self):
        debug_print (' In EFFECTS_DONE state')
        # Midi: 
        #play_voice ()
        delay_trans (1, 'current_level.scratch_axe_1()')
    
    ##############################  SCRATCH/AXE  ##############################
    def scratch_axe_1 (self):
        debug_print (' In SCRATCH_AXE_1 state')
        # Midi: 
        #play_voice ()
        delay_trans (1, 'current_level.scratch_axe_2()')
    
    def scratch_axe_2 (self):
        debug_print (' In SCRATCH_AXE_2 state')
        # Midi: 
        #play_voice ()
        delay_trans (1, 'current_level.rotation_test([2,3], 0, \'current_level.scratch_axe_3()\', 50, 1.5)')
    
    def scratch_axe_3 (self):
        debug_print (' In SCRATCH_AXE_3 state')
        self.restore_attrs ()
        hx.input ('enable', 0, 'rpch')
        hx.input ('enable', 0, 'regi')
        hx.input ('enable', 0, 'axfx')
        hx.input ('enable', 0, 'rotL')
        hx.input ('enable', 0, 'rotR')
        
        def on_track_select (self, track):
            debug_print (' Selected a track')
            debug_print (track)
            if track == 3:
                hx.input ('disable', 0, 'rotR')     # Disable rotation right
                hx.input ('enable', 0, 'rotL')      # Enable rotation left
                debug_print (' On track 3, disable rotation right')
            elif track == 2:
                hx.input ('disable', 0, 'rotL')     # Disable rotation left
                hx.input ('enable', 0, 'rotR')      # Enable rotation right
                debug_print (' On track 2, disable rotation left')

        self.on_track_select = new.instancemethod (on_track_select, self, self.__class__)
        delay_trans (0, 'current_level.listen(8, \'current_level.scratch_axe_done()\')')
    
    def scratch_axe_done (self):
        debug_print (' In SCRATCH_AXE_DONE state')
        self.restore_attrs ()
        # Midi: 
        #play_voice ()
        hx.input ('disable', 0, 'rpch')
        hx.input ('disable', 0, 'regi')
        hx.input ('disable', 0, 'axfx')
        delay_trans (1, 'current_level.section_advance_1()')
    
    ############################# SECTION ADVANCE #############################
    def section_advance_1 (self):
        debug_print (' In SECTION_ADVANCE_1 state')
        # Midi: 
        #play_voice ()
        delay_trans (1, 'current_level.section_advance_test(0, \'current_level.section_advance_2()\')')
    
    def section_advance_2 (self):
        debug_print (' In SECTION_ADVANCE_2 state')
        self.restore_attrs ()
        # Midi: 
        #play_voice ()
        delay_trans (1, 'current_level.section_advance_3()')

    def section_advance_3 (self):
        debug_print (' In SECTION_ADVANCE_3 state')
        # Midi: 
        #play_voice ()
        delay_trans (1, 'current_level.listen_mode()')

    ##############################  LISTEN MODE  ##############################
    def listen_mode (self):
        debug_print (' In LISTEN_MODE state')
        # Midi: 
        #play_voice ()
        delay_trans (1, 'current_level.conclusion_1()')
    
    ##############################  CONCLUSION   ##############################
    def conclusion_1 (self):
        debug_print (' In CONCLUSION_1 state')
        # Midi: 
        #play_voice ()
        delay_trans (1, 'current_level.conclusion_2()')
    
    def conclusion_2 (self):
        debug_print (' In CONCLUSION_2 state')
        # Midi: 
        #play_voice ()
        delay_trans (1, 'current_level.tutorial_done()')

    ###########################################################################

    def test_bank (self, note_start, note_end, wait):
        play_voice (note_start)
        print ' wait: ', wait, '  new_wait: '
        if note_start == note_end:
            pass
        s = 'current_level.test_bank(' + `(note_start+1)` + ',' + `note_end` + ',' + `wait` + ')'
        delay_trans (wait, s)


def get_class_name ():
    return TutorialLevel
