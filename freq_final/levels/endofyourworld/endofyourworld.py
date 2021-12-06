# Copyright 2000 Harmonix Music Systems.  All rights reserved.

class EndOfYourWorldLevel (Level):
    def __init__ (self):

        Level.__init__(self)

        self.directory_name = "endofyourworld"
        self.track_enable_criteria = ('yes', 1, 1, 2, 2, 3, 1, 1)
        self.game_bg_criteria = ('yes',(1,2,3,4,5,6), 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes',(1,2,3,4,5,6), 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.fx_filt_max = (55, 65, 80, 60, 65, 65, 78, 127)
        self.fx_filt_period = (1920, 3840,  1920, 480,  1920, 960,  1920, 960)
        self.fx_stt         = (120, 0)
        self.fx_volume      = 50
        self.freestyle_points = [6, 8, 10]
        self.section_boundaries = [8, 16, 24, 32, 40, 48]
        self.section_instances =   [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]
        self.materials = ("drum",
                          "drum",
                          "bass",
                          "synth",
                          "vocal",
                          "fx",
                          "lead",
                          "lead")

    def get_name (self):        return "End Of Your World"
    def get_abbrev_name (self): return "EndofYourWorld"
    def get_artist (self):      return "Robotkid vs Inter:sekt"
    def get_genre (self):       return "bionic sonic beats"
    def get_tempo (self):       return "160"
    def get_description (self): return "Robotkid and Inter:sekt duke it out on the dancefloor with \"End of Your World.\"  Put on your stompin' boots and get on down.  Remixed by Symbion Project.  www.robotkid.com"
    def get_song_id (self):     return 2   # Return unique id for this song...

    # for metagame: 1 means yes, 0 means no
    def is_avail_game(self):    return 1
    def is_avail_jam(self):   return 1

    def use_linear_song_form (self):
        return 1

    # Turn on a hardware effect for the given core?  1 for yes, 0 for no
    def ps2_use_hard_effect (self, core):
        return 1

    # What hardware effect to use on the given core?  Valid values are
    # 'room', 'studio a', 'studio b', 'studio c', 'hall', 'space',
    # 'echo', 'delay', 'pipe'
    def ps2_hard_effect_name (self, core):
        if core == 0:
            return 'echo'               # Core 0 uses delay
        else:
            return 'delay'                # Core 1 uses echo

    # What volumes (left and right) should the effect be at for the given core?
    # Scale is 0-127
    def ps2_hard_effect_volumes (self, core):
        if core == 0:
            return [60, 60]               # Core 0 has delay time of 60
        else:
            return [65, 65]               # Core 1 has delay time of 00
        
    # What is the delay time for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_delay_time (self, core):
        if core == 0:
            return 87                     # Core 0 has delay time of 90
        else:
            return 40                     # Core 1 has delay time of 00

    # What is the feedback value for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_feedback (self, core):
        if core == 0:
            return 55                   # core 0: 40
        else:
            return 30                    # core 1: 0


def get_class_name ():
    return EndOfYourWorldLevel


