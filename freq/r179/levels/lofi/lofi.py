# Copyright 2000 Harmonix Music Systems.  All rights reserved.


# 8 bar inst chorus - 0 - bank1
# 8 bar verse 1 - 16 bars - 1 - bank2
# 8 bar breakdown - 2 - bank3
# 8 bar chorus 1A - 16 bars -  3 - bank4
# 8 bar verse 2A - 4
# 8 bar verse 2B - 4
# 8 bar chorus 2A [extra vox] - 5
# 8 bar chorus 2B [extra vox] - 6
# 8 bar chorus with talkbox [different solo vox] - 7
# 8 bar chorus with talkbox B {different solo vox] - 8

class lofiLevel (Level):
    def __init__ (self):
        Level.__init__(self)

        self.directory_name = 'lofi'
        self.track_enable_criteria = ('yes', 1, 2, 2, 3, 3, 3, 3)
        self.game_bg_criteria = ('yes',(1,2), 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes',(1,2), 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.fx_filt_period = (1920, 960,  1920, 480,  1920, 960,  1920, 960)
        self.fx_stt         = (120, 0)
        self.fx_volume      = 50
        self.num_laps         = [3, 4, 3, 3]
        self.freestyle_points = [5, 12, 14]
        self.section_boundaries = [8, 24, 32, 48, 64, 72, 80, 88, 96]
        self.section_instances =   [0, 1, 2, 5, 6, 7, 2, 5, 6, 7]
        self.materials = ("drum",
                          "drum",
                          "bass",
                          "synth",
                          "vocals",
                          "synth",
                          "lead",
                          "lead")

    def use_bank_swapping (self): return 1

    def get_name (self):        return "LoFis In Ibiza"
    def get_abbrev_name (self): return "LoFis In Ibiza"
    def get_artist (self):      return "LoFi Allstars"
    def get_genre (self):       return "Disco House"
    def get_tempo (self):       return "129"
    def get_description (self): return "The LoFis are in the house!"
    def get_song_id (self):     return 21
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
            return 'delay'               # Core 0 uses delay
        else:
            return 'delay'               # Core 1 uses delay

    # What volumes (left and right) should the effect be at for the given core?
    # Scale is 0-127
    def ps2_hard_effect_volumes (self, core):
        if core == 0:
            return [45, 45]               # Core 0 has delay depth of 30
        else:
            return [55, 55]               # Core 1 has delay depth of 40
        
    # What is the delay time for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_delay_time (self, core):
        if core == 0:
            return 40                     # Core 0 has delay time of 40
        else:
            return 27                     # Core 1 has delay time of 27

    # What is the feedback value for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_feedback (self, core):
        if core == 0:
            return 30                   # core 0: 30
        else:
            return 45                   # core 1: 45

def get_class_name ():
    return lofiLevel
