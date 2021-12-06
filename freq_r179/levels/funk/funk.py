# Copyright 2000 Harmonix Music Systems.  All rights reserved.
#
# $Header: j:\\cvs/Freq/run/Levels/funk/funk.py,v 1.10 2001/09/26 04:42:24 guest Exp $
## sections:
#
# 0 verse 1 no vox
# 1 verse 2 and bridge
# 2 chorus 1 [same as section 6]
# 3 c section
# 4 verse 3 no vox
# 5 verse 4 and bridge
# 6 chorus 1 [same as section 2]
# 7 c section
# 8 breakdown
# 9 verse 5 and bridge
# 10 chorus 2 
# 11 chorus 3

class funkLevel (Level):
    def __init__ (self):
        Level.__init__(self)

        self.directory_name = 'funk'
        self.track_enable_criteria = ('yes', 1, 1, 1, 1, 1, 1, 1)
        self.game_bg_criteria = ('yes','yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes','yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.fx_filt_period = (1920, 960,  1920, 480,  1920, 960,  1920, 960)
        self.fx_stt         = (120, 0)
        self.fx_volume      = 50
        self.stage_num      = 2
        self.num_laps         = [2, 4, 3, 3]
        self.freestyle_points = [8, 16, 18]
        self.section_boundaries = [8, 20, 28, 36, 44, 56, 64, 72, 80, 92, 100, 108]
        self.section_instances =   [0, 1, 2, 3, 4, 5, 2, 3, 8, 9, 10, 11, 3, 8, 9, 10, 11]
        self.linked_sections = [[ [1,5], [2,11] ],         #T1
                                [ [1,5], [2,11] ],         #T2
                                [ [1,5], [10,11] ],        #T3
                                [],                        #T4
                                [ [1,5] ],                 #T5
                                [],                        #T6
                                [],                        #T7
                                []]                        #T8

        self.materials = ("drum",
                          "drum",
                          "bass",
                          "vocal",
                          "guitar",
                          "synth",
                          "lead",
                          "lead")

    def get_name (self):        return "Ignition"
    def get_abbrev_name (self): return "Ignition"
    def get_artist (self):      return "Funkstar Deluxe"
    def get_genre (self):       return "Funk"
    def get_tempo (self):       return "115"
    def get_description (self): return "Funkstar De Luxe kicked in the doors all over the world when he remixed Bob Marley's \"Sun is Shining.\" To get the atmosphere just right for the recording, the studio was decorated with palm trees and all the actual work was done only when the sun was shining! www.funkstardeluxe.com"
    def get_song_id (self):     return 23
    def wacko_panning (self):   return 0
    def use_linear_song_form (self):
        return 1

    # for metagame: 1 means yes, 0 means no
    def is_avail_game(self):    return 1
    def is_avail_jam(self):   return 1

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
            return 'delay'                # Core 0 uses delay
        else:
            return 'delay'                # Core 1 uses delay

    # What volumes (left and right) should the effect be at for the given core?
    # Scale is 0-127
    def ps2_hard_effect_volumes (self, core):
        if core == 0:
            return [55, 55]              # Core 0 has delay time of 40
        else:
            return [50, 50]               # Core 1 has delay time of 35
        
    # What is the delay time for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_delay_time (self, core):
        if core == 0:
            return 70                     # Core 0 has delay time of 70
        else:
            return 55                     # Core 1 has delay time of 55

    # What is the feedback value for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_feedback (self, core):
        if core == 0:
            return 50                   # core 0: 50
        else:
            return 35                   # core 1: 35

def get_class_name ():
    return funkLevel
