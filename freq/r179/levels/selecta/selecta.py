# Copyright (c) 2000-2000  Harmonix Music Systems  All rights reserved

class SelectaLevel (Level):
    def __init__ (self):

        Level.__init__(self)

        self.directory_name = 'selecta'
        self.track_enable_criteria = ('yes', 1, 1, 1, 1, 1, 6, 6)
        self.game_bg_criteria = ('yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria =  ('yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.fx_filt_max = (64, 63, 70, 64, 65, 75, 65, 127)
        self.fx_filt_period = (1920, 1920,  960, 480,  1920, 960,  1920, 480)
        self.fx_stt         = (240, 0)
        self.fx_volume      = 50
        self.freestyle_points = [4, 9, 12]
        self.section_boundaries = [8, 16, 24, 32, 40]
        self.section_instances =   [0, 1, 2, 3, 4, 1, 0, 4, 3, 2, 0, 1, 2, 3, 4]
        self.materials = ("drum",
                          "bass",
                          "drum",
                          "synth",
                          "synth",
                          "fx",
                          "lead",
                          "lead")

    def get_name (self):        return "Selecta"
    def get_abbrev_name (self): return "Selecta"
    def get_artist (self):      return "Ethan Eves"
    def get_genre (self):       return "Drum & Bass"
    def get_tempo (self):       return "180"
    def get_description (self): return "Ethan E Eves has been producing energetic electronic music since 1996 in various groups and collaborations around the United States.  His most recent endeavors have been in Southern California producing Jungle and Drum'n'Bass.  www.e3-music.com"
    def get_song_id (self):     return 4  # Return unique id for this song...
    def use_linear_song_form (self):
        return 1

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
        return 'delay'                   # Both cores use delay

    # What volumes (left and right) should the effect be at for the given core?
    # Scale is 0-127
    def ps2_hard_effect_volumes (self, core):
        if core == 0:
            return [45, 45]             # core 0: 30 left, 30 right
        else:
            return [55, 55]             # core 1: 40 left, 40 right
        
    # What is the delay time for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_delay_time (self, core):
        return 127                       # 127 on both cores
        
    # What is the feedback value for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_feedback (self, core):
        if core == 0:
            return 15                   # core 0: 15
        else:
            return 50                   # core 1: 50

    
def get_class_name ():
    return SelectaLevel


