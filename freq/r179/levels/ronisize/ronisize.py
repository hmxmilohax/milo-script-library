# Copyright 2000 Harmonix Music Systems.  All rights reserved.
#
# $Header: j:\\cvs/Freq/run/Levels/Ronisize/Ronisize.py,v 1.18 2001/09/26 04:50:35 guest Exp $
#

# sections:
#
# 0 8 bar verse
# 1 8 bar verse 2 
# 2 8 bar verse 3
# 3 8 bar
# 4 
# 5 
# 6 
# 7 
# 8 
# 9 


class RonisizeLevel (Level):
    def __init__ (self):
        Level.__init__(self)

        self.directory_name = 'ronisize'
        self.track_enable_criteria = ('yes', 1, 2, 3, 1, 2, 1, 1)
        self.game_bg_criteria = ('yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.fx_filt_period = (1920, 960, 1920, 480, 1920, 960, 1920, 960)
        self.fx_stt         = (240, 0)
        self.fx_volume      = 50
        self.freestyle_points = [6, 9, 12]
        self.num_laps         = [2, 4, 3, 3]
        self.section_boundaries = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]
        #[original ordering] self.section_instances =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.section_instances =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.linked_sections = [[ [0,4,9] ],           #T1
                                [ [4,9], [3,5] ],      #T2
                                [],                    #T3
                                [],                    #T4
                                [ [1,3,9], [2,4], [5,7], [6,8] ],      #T5
                                [ [1,4], [2,6], [3,7], [8,9] ],        #T6
                                [],                    #T7
                                []]                    #T8
        self.materials = ("bass",
                          "drum",
                          "synth",
                          "vocal",
                          "drum",
                          "drum",
                          "lead",
                          "lead")

    def get_name (self):        return "Railing Pt.2"
    def get_abbrev_name (self): return "Railing Pt.2"
    def get_artist (self):      return "Roni Size & Reprazent"
    def get_genre (self):       return "Drum & Bass"
    def get_tempo (self):       return "175"
    def get_description (self): return "Roni Size is probably the most successful and innovative producer to have emerged from the UK Drum'n'Bass explosion. Roni has both his own underground label (Full Cycle) plus his group Reprazent with collaborators Krust, Die, Suv and Dynamite MC. www.ronisize.com"
    def get_song_id (self):     return 19   # Return unique id for this song...
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
            return 'echo'               # Core 0 uses echo
        else:
            return 'delay'              # Core 1 uses delay

    # What volumes (left and right) should the effect be at for the given core?
    # Scale is 0-127
    def ps2_hard_effect_volumes (self, core):
        if core == 0:
            return [55, 55]               # Core 0 has delay time of 40
        else:
            return [0, 0]                 # Core 1 has delay time of 60

    # What is the delay time for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_delay_time (self, core):
        if core == 0:
            return 60                     # Core 0 has delay time of 60
        else:
            return 0                      # Core 1 has delay time of 70

    # What is the feedback value for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_feedback (self, core):
        if core == 0:
            return 30                   # core 0: 30
        else:
            return 0                    # core 1: 45

def get_class_name ():
    return RonisizeLevel
