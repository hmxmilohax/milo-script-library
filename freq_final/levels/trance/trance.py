# Copyright 2000 Harmonix Music Systems.  All rights reserved.

class TranceLevel (Level):
    def __init__ (self):
        Level.__init__(self)

        self.directory_name = 'trance'
        self.track_enable_criteria = ('yes',1,2,3,3,4,4,1)
        self.game_bg_criteria = ('yes',(1,2,3,4,5,6), (2), 'yes', (3,5,6), 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes', 'yes', (1,2,3,4,5,6), 'yes', 'yes', 'yes', 'yes', 'yes')
        self.fx_filt_max = (70, 45, 45, 60, 55, 65, 75, 60)
        self.fx_filt_period = (1920, 960,  1920, 960,  1920, 960,  1920, 960)
        self.fx_stt         = (120, 0)
        self.freestyle_points = [8, 9, 10]
        self.fx_volume      = 50
        self.materials = ("drum",
                          "bass",
                          "synth",
                          "vocal",
                          "synth",
                          "synth",
                          "drum",
                          "lead")
        self.section_boundaries = [8, 16, 24, 32]
        self.section_instances = [0, 1, 2, 3, 1, 2, 0, 1, 2, 3, 3]

    def get_name (self):        return "Ibiza Dreamz"
    def get_abbrev_name (self): return "Ibiza Dreamz"
    def get_artist (self):      return "DJ HMX"
    def get_genre (self):       return "trance"
    def get_tempo (self):       return "144"
    def get_description (self): return "Superstar DJ HMX returns from his world tour to deliver the smash hit \"Ibiza Dreamz.\"  Let the synth waves wash over you as HMX takes you to a higher level."
    def get_song_id (self):     return 6  # Return unique id for this song...

    # for metagame: 1 means yes, 0 means no
    def is_avail_game(self):    return 1
    def is_avail_jam(self):   return 1

    def use_linear_song_form (self): return 1

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
            return 'hall'                   # Core 1 uses hall

    # What volumes (left and right) should the effect be at for the given core?
    # Scale is 0-127
    def ps2_hard_effect_volumes (self, core):
        if core == 0:
            return [60, 60]             # core 0: 45 left, 45 right
        else:
            return [70, 70]             # core 1: 55 left, 55 right
        
    # What is the delay time for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_delay_time (self, core):
        if core == 0:
            return 60                   # core 0: 60
        else:
            return 85                   # core 1: 85
        
    # What is the feedback value for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_feedback (self, core):
        if core == 0:
            return 30                   # core 0: 30
        else:
            return 30                   # core 1: 30

def get_class_name ():
    return TranceLevel

