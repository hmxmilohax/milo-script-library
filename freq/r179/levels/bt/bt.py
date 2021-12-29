# Copyright 2000 Harmonix Music Systems.  All rights reserved.
#
# $Header: j:\\cvs/Freq/run/Levels/BT/BT.py,v 1.13 2001/09/25 03:16:59 kasson Exp $
#

# sections:
#
# 0 8 bar verse
# 1 8 bar verse 2 
# 2 8 bar verse 3
# 3 8 bar chorus
# 4 8 bar verse 4
# 5 
# 6 
# 7 
# 8 8 bar break 
# 9 8 bar chorus


class BTLevel (Level):
    def __init__ (self):
        Level.__init__(self)

        self.directory_name = 'BT'
        self.track_enable_criteria = ('yes', 1, 1, 1, 2, 2, 1, 1)
        self.game_bg_criteria = ('yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.fx_filt_period = (1920, 960, 1920, 480, 1920, 960, 1920, 960)
        self.fx_stt         = (240, 0)
        self.fx_volume      = 50
        self.num_laps         = [2, 4, 3, 3]
        self.freestyle_points = [14, 20, 20]
        self.section_boundaries = [8, 16, 24, 32, 40, 48, 56, 64, 72]
        self.section_instances =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 2, 3, 4, 7, 8]
        self.materials = ("durm",
                          "drum",
                          "bass",
                          "guitar",
                          "guitar",
                          "vocal",
                          "lead",
                          "lead")

    def get_name (self):        return "Smartbomb"
    def get_abbrev_name (self): return "Smartbomb"
    def get_artist (self):      return "BT"
    def get_genre (self):       return "Big Beatz"
    def get_tempo (self):       return "100"
    def get_description (self): return "Artist,Producer, Composer, & Remixer BT has been busy. Not only is he working on a follow-up to his album, Movement in Still Life, but he has also produced N'SYNC's hit single \"Pop\", remixed tracks for Sarah McLaghlan, Tori Amos, Madonna, and Seal. www.btmusic.com"
    def get_song_id (self):     return 20   # Return unique id for this song...
    def wacko_panning (self):   return 0
    def use_linear_song_form (self): return 1
    def use_bank_swapping (self): return 1

    # for metagame: 1 means yes, 0 means no
    def is_avail_game(self):    return 1
    def is_avail_jam(self):   return 1

    def get_seermusic_bank (self):
        return self.get_seermusic_bank_by_ruleset ()

    # Turn on a hardware effect for the given core?  1 for yes, 0 for no
    def ps2_use_hard_effect (self, core):
        return 0

    # What hardware effect to use on the given core?  Valid values are
    # 'room', 'studio a', 'studio b', 'studio c', 'hall', 'space',
    # 'echo', 'delay', 'pipe'
    def ps2_hard_effect_name (self, core):
        if core == 0:
            return 'echo'               # Core 0 uses echo
        else:
            return 'delay'              # Core 1 uses delay

    # What volumes (left and right) should the effect be at for the given core?
    # Scale is 0-127
    def ps2_hard_effect_volumes (self, core):
        if core == 0:
            return [0, 0]               # Core 0 has delay time of 40
        else:
            return [0, 0]                 # Core 1 has delay time of 60

    # What is the delay time for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_delay_time (self, core):
        if core == 0:
            return 0                     # Core 0 has delay time of 60
        else:
            return 0                      # Core 1 has delay time of 70

    # What is the feedback value for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_feedback (self, core):
        if core == 0:
            return 0                   # core 0: 30
        else:
            return 0                    # core 1: 45

def get_class_name ():
    return BTLevel
