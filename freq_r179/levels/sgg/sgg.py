# Copyright 2000 Harmonix Music Systems.  All rights reserved.
#
# $Header: j:\\cvs/Freq/run/Levels/sgg/sgg.py,v 1.15 2001/09/26 04:34:23 guest Exp $
## sections:
#
# 0 intro A
# 1 verse 1 B
# 2 chorus 1 [same as section 5] C
# 3 intro 2 [same as section 0] D
# 4 verse 2 E
# 5 chorus 2 [same as section 2] F
# 6 bridge G
# 7 verse 3 H
# 8 chorus 3 I
# 9 chorus 3 with tag end J

class sggLevel (Level):
    def __init__ (self):
        Level.__init__(self)

        self.directory_name = 'sgg'
        self.track_enable_criteria = ('yes', 1, 1, 1, 1, 1, 1, 1)
        self.game_bg_criteria = ('yes','yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes','yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.fx_filt_period = (1920, 960,  1920, 480,  1920, 960,  1920, 960)
        self.fx_stt         = (120, 0)
        self.fx_volume      = 50
        self.stage_num      = 2
        self.freestyle_points = [5, 10, 12]
        self.num_laps         = [2, 4, 3, 3]
        self.section_boundaries = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]
        self.section_instances =   [0, 1, 2, 4, 5, 6, 7, 8, 0, 1, 2, 4, 5, 6 ,7, 8]
        self.linked_sections = [ [],                      #T1
                                [],                        #T2
                                [],                        #T3
                                [],                        #T4
                                [],                        #T5
                                [],                        #T6
                                [],                        #T7
                                []]                        #T8

        self.materials = ("drum",
                          "drum",
                          "bass",
                          "synth",
                          "synth",
                          "vocal",
                          "vocal",
                          "lead")

    def get_name (self):        return "Science Genius Girl"
    def get_abbrev_name (self): return "Science Genius Girl"
    def get_artist (self):      return "Freezepop"
    def get_genre (self):       return "Synthpop"
    def get_tempo (self):       return "137"
    def get_description (self): return "Freezepop is a trio of fashionable gad-abouts from Boston with an infectious flair for synthpop songs about robots, and love, and loving robots. Look for their full length album and other goodies at www.freezepop.net"
    def get_song_id (self):     return 25
    def wacko_panning (self):   return 0
    def use_linear_song_form (self):
        return 1

    # for metagame: 1 means yes, 0 means no
    def is_avail_game(self):    return 1
    def is_avail_jam(self):   return 1

    def use_bank_swapping (self): return 1

    def get_seermusic_bank (self):
        return self.get_seermusic_bank_by_ruleset ()

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
        if core == 0:
            return [55, 55]              # Core 0 has delay time of 45
        else:
            return [96, 96]              # Core 1 has delay time of 86
        
    # What is the delay time for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_delay_time (self, core):
        if core == 0:
            return 80                     # Core 0 has delay time of 80
        else:
            return 21                     # Core 1 has delay time of 21

    # What is the feedback value for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_feedback (self, core):
        if core == 0:
            return 35                   # core 0: 35
        else:
            return 65                   # core 1: 65

def get_class_name ():
    return sggLevel
