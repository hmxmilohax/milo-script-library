# Copyright 2000 Harmonix Music Systems.  All rights reserved.

class ScratchotronicLevel (Level):
    def __init__ (self):

        Level.__init__(self)

        self.directory_name = 'scratchotronic'
        self.short_name = 'scratch'
        self.track_enable_criteria = ('yes', 1, 2, 3, 3, 2, 4, 1)
        self.game_bg_criteria = ((1,2,5,6,7),(1,2,5,6,7), 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ((1,2,6), 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.fx_filt_max = (70, 45, 45, 60, 55, 65, 75, 60)
        self.fx_filt_period = (1920, 960,  1920, 480,  1920, 960,  1920, 960)
        self.fx_stt         = (120, 0)
        self.fx_volume      = 50
        self.materials = ("drum",
                          "bass",
                          "synth",
                          "guitar",
                          "fx",
                          "drum",
                          "fx",
                          "fx")

    def get_name (self):        return "Scratchotronic"
    def get_abbrev_name (self): return "Scratchotronic"
    def get_artist (self):      return "Kareem Caines"
    def get_genre (self):       return "Hip Hop"
    def get_tempo (self):       return "92"
    def get_description (self): return "Straight out of the Bronx comes Kareem Caines, proclaiming “HipHop is my Life.”  Look for his new album next summer."
    def get_song_id (self):     return 5  # Return unique id for this song...

    # for metagame: 1 means yes, 0 means no
    def is_avail_game(self):    return 1
    def is_avail_jam(self):   return 1

    # Turn on a hardware effect for the given core?  1 for yes, 0 for no
    def ps2_use_hard_effect (self, core):
        return 1

    # What hardware effect to use on the given core?  Valid values are
    # 'room', 'studio a', 'studio b', 'studio c', 'hall', 'space',
    # 'echo', 'delay', 'pipe'
    def ps2_hard_effect_name (self, core):
        if core == 0:
            return 'echo'                   # Core 0 uses echo
        else:
            return 'studio a'               # Core 1 uses studio A

    # What volumes (left and right) should the effect be at for the given core?
    # Scale is 0-127
    def ps2_hard_effect_volumes (self, core):
        if core == 0:
            return [45, 45]             # core 0: 45 left, 45 right
        else:
            return [25, 25]             # core 1: 25 left, 25 right
        
    # What is the delay time for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_delay_time (self, core):
        if core == 0:
            return 122                  # core 0: 122
        else:
            return 35                   # core 1: 35
        
    # What is the feedback value for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_feedback (self, core):
        if core == 0:
            return 45                   # core 0: 45
        else:
            return 0                    # core 1: 0

def get_class_name ():
    return ScratchotronicLevel

    if os.name == 'ps2':
       self.jam_bg_criteria  = ((1,2,6), 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
    else:
       self.jam_bg_criteria  = ('yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')

