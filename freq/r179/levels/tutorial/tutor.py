
import hx
import new

# globals used to maintain state when we redefine functions...
consecutive_hits = 0
consecutive_misses = 0
next_func = ''
next_func_delay = 0
bank_num = 0
goal_tracks = []

feedback_enabled = 1
feedback_buffer = 0.1

feedback_mgr = None

# Debug printing...  use print on PS2, hx.trace on PC
def debug_print (text):
    return
    #print text         # Doesn't work on PC, but does on PS2
    #hx.trace (text)    # Works on PC, but blue screen on PS2 throws off timing

# Call function 'script', after 'bars' bars have passed
def delay_trans (bars, script):
    when = bars * 1920 + hx.clock ('tick')
    hx.post_script (when, script)

# Try to swap in the next bank, then play the requested note.
#  This is set up to only work from the tutorial, and only try to swap
#  banks if bank swapping is actually turned on.
def play_voice (note, bank):
    if current_level.is_tutorial == 1:
        if current_level.using_bank_swap == 1:
            debug_print (' playing midi now...')
            hx.midi ('play', 'voice', note, 127, bank, 1)
            bars = float(1920 - (hx.clock ('tick') % 1920)) / 1920
            delay_trans (bars, 'hx.midi (\'bank_swap\', \'\', %d, 0, 0, 0)' % (bank + 1))
        else:
            hx.midi ('play', 'voice', note, 127, bank, 0)
    
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
        self.bank = 0
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
        play_voice (self.note, self.bank)
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

    def setup_timed_feedback (self, time, note, bank, note_len):
        debug_print (' Setting up timed feedback...')
        x = TimedFeedback ()
        x.time_limit = time
        x.note = note
        x.bank = bank
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

        self.hili_full = [ -27, 10, 570, -415 ]
        self.hili_center = [ 268, -190, 269, -191 ]
        self.hili_anim_rate = 480

    def get_is_tutorial (self):  return self.is_tutorial

    def get_section_boundaries (self):
        return self.section_boundaries

    def wacko_panning (self):   return 0

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
    #
    # Tutorial specific script code...
    #
    def restore_attrs (self):
        # Delete all the new 'on_*' methods attached to our own object,
        # so that further calls will get the one in the object's class.
        for k in self.__dict__.keys():
            if k[:3] == 'on_':
                delattr (self, k)

    ############################# UTILITY FUNCS ##############################

    def hide_section_boundaries (self):
        hx.sections (0)

    def show_section_boundaries (self):
        hx.sections (1)

    # Stop looping in the current section and advance to the next one
    def advance_section (self):
        hx.advance_section (hx.clock('tick'))
    
    def blink_item (self, func_on, func_off, dur_on, dur_off, num_flashes, final_state):
        period = dur_on + dur_off
        
        # post the enable item messages first
        seed = 1
        while seed < num_flashes + 1:
            delay_trans (seed * period, func_on)
            seed = seed + 1

        # post the disable item messages next
        seed = 0
        while seed < num_flashes:
            delay_trans ((seed * period) + dur_on, func_off)
            seed = seed + 1

        # Turn on or off the item before stopping based on final_state
        if final_state == 'on':
            delay_trans ((num_flashes * period) + dur_on, func_on)
        else:
            delay_trans ((num_flashes * period) + dur_on, func_off)

    # Disable and enable feedback in looping functions.  These are useful
    #  when there are important voice-over instructions playing, and we don't
    #  want to interrupt them with less meaningful messages.
    def disable_feedback_midi (self):
        debug_print (' Disabling feedback')
        self.feedback_midi = 0

    def enable_feedback_midi (self):
        debug_print (' Enabling feedback')
        self.feedback_midi = 1

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

    def highlight_animate (self, mode):
        pass
    
    # BOTH versions of the tutorial need to use this function
    #
    # Wait until the user rotates one of the correct tracks
    #  <track_list> = track numbers that the user should rotate to.
    #  <func_delay> = # of bars to wait before calling func
    #  <func> = function that should be called after passing test
    #  <play_feedback> = 0: play no midi, 1: play midi feedback
    #
    def rotation_test (self, track_list, func_delay, func, note, note_length, feedback_spacing, bank):
        global next_func, next_func_delay, goal_tracks
        next_func = func
        next_func_delay = func_delay
        goal_tracks = track_list
        debug_print (goal_tracks)
        debug_print (' In ROTATION_TEST state')

        self.activator_control ('enable')   # Show the activator
        hx.input ('enable', 0, 'rotR')      # Enable rotation right
        hx.input ('enable', 0, 'rotL')      # Enable rotation left
        self.last_feedback = feedback_mgr.setup_timed_feedback (feedback_spacing, note, bank, note_length)
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

    ###########################################################################

#    def test_bank (self, note_start, note_end, wait, bank):
#        play_voice (note_start, bank)
#        print ' Playing note ', note_start
#        if note_start == note_end:
#            return
#        s = 'current_level.test_bank(' + `(note_start+1)` + ',' + `note_end` + ',' + `wait` + ',' + bank + ')'
#        delay_trans (wait, s)


