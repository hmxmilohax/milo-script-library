# Copyright 2000 Harmonix Music Systems.  All rights reserved.

class ControlYourBodyLevel (Level):
    def __init__ (self):
        Level.__init__(self)

        self.directory_name = 'controlyourbody'
        self.track_enable_criteria = ('yes', 1, 2, 3, 3, 4, 3, 4)
        self.game_bg_criteria = ('yes',(4,6), (1,3), 'yes', 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes',(1,2,3,4,5,6), (1,2,3,4,5,6), (1,2,3,4,5,6), (1,2,3,4,5,6), (1,2,3,4,5,6), 'yes', 'yes')
        self.fx_filt_period = (1920, 960,  1920, 480,  1920, 960,  1920, 960)
        self.fx_stt         = (120, 0)
        self.section_boundaries = [8, 16, 24, 32, 40, 48]
        self.section_instances = [0, 1, 2, 3, 4, 5, 0, 3, 2, 4, 0, 1, 2, 3, 4, 5]
        self.fx_volume      = 50
        self.freestyle_points = [10, 10, 10]
        self.materials = ("drum",
                          "bass",
                          "drum",
                          "synth",
                          "fx",
                          "synth",
                          "lead",
                          "lead")

    def get_name (self):        return "Control Your Body"
    def get_abbrev_name (self): return "ControlYourBody"
    def get_artist (self):      return "Komputer Kontroller"
    def get_genre (self):       return "hard house"
    def get_tempo (self):       return "144"
    def get_description (self): return "Komputer Kontroller controls your body with his latest hard house anthem. You will not be able to resist his funky beats or thumping bass. You are now under kontrol!"
    def get_song_id (self):     return 1   # Return unique id for this song...
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
            return 'delay'                 # Core 0 uses echo
        else:
            return 'echo'                # Core 1 uses delay

    # What volumes (left and right) should the effect be at for the given core?
    # Scale is 0-127
    def ps2_hard_effect_volumes (self, core):
        if core == 0:
            return [75, 75]               # Core 0 has delay time of 35
        else:
            return [55, 55]               # Core 1 has delay time of 50
        
    # What is the delay time for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_delay_time (self, core):
        if core == 0:
            return 60                     # Core 0 has delay time of 60
        else:
            return 60                     # Core 1 has delay time of 60

    # What is the feedback value for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_feedback (self, core):
        if core == 0:
            return 55                   # core 0: 25
        else:
            return 25                   # core 1: 55

def get_class_name ():
    return ControlYourBodyLevel
