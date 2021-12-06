#********** Copyright © 2000-2000  Harmonix Music Systems  All rights reserved

class XLR8RLevel (Level):
    def __init__ (self):

        Level.__init__(self)

        self.directory_name = 'xlr8r'
        self.track_enable_criteria = ('yes', 1, 2, 3, 4, 5, 3, 3)
        self.game_bg_criteria = ('yes',(2,3,4,6),(1,2,3,4,5,6), (2,3,4), (1,6), 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes','yes','yes','yes', 'yes', 'yes', 'yes', 'yes')
        self.fx_filt_max = (65, 65, 65, 55, 65, 65, 127, 127)
        self.fx_filt_period = (1920, 1920,  960, 480,  1920, 960,  1920, 480)
        self.section_boundaries = [8, 16, 24, 32, 40, 48, 56, 64]
        self.section_instances =  [0, 1, 2, 3, 4, 5, 2, 3, 0, 1, 6, 7, 4, 5, 6, 7]
        self.fx_stt         = (120, 0)
        self.freestyle_points = [3, 5, 8]
        self.fx_volume      = 50
        self.materials = ("drum",
                          "bass",
                          "guitar",
                          "guitar",
                          "vocal",
                          "drum",
                          "lead",
                          "lead")

    def get_name (self):        return "XLR8R"
    def get_abbrev_name (self): return "XLR8R"
    def get_artist (self):      return "Orbit"
    def get_genre (self):       return "rock'n'roll"
    def get_tempo (self):       return "135"
    def get_description (self): return "Orbit's signature sound combines driving, dynamic bass and guitar lines with passionate vocal melodies. Their hit song \"Medicine\" from 1997's 'Libido Speedway' earned them a spot on the Lollapalooza tour and all the usual hype.  www.orbitband.com"
    def get_song_id (self):     return 7  # Return unique id for this song...
    def use_linear_song_form (self): return 1
    def use_bank_swapping (self): return 1

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
            return 'delay'                  # Core 0 uses delay
        else:
            return 'delay'                  # Core 1 uses delay

    # What volumes (left and right) should the effect be at for the given core?
    # Scale is 0-127
    def ps2_hard_effect_volumes (self, core):
        if core == 0:
            return [50, 50]             # core 0: 52 left, 52 right
        else:
            return [70, 70]             # core 1: 55 left, 55

    # What is the delay time for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_delay_time (self, core):
        if core == 0:
            return 64                   # core 0: 35
        else:
            return 127                  # core 1: 127
        
    # What is the feedback value for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_feedback (self, core):
        if core == 0:
            return 40                   # core 0: 30
        else:
            return 50                   # core 1: 50

def get_class_name ():
    return XLR8RLevel

