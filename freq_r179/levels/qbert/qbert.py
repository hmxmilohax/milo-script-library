# Copyright 2000 Harmonix Music Systems.  All rights reserved.
#
# $Header: j:\\cvs/Freq/run/Levels/qbert/qbert.py,v 1.14 2001/09/26 04:50:00 guest Exp $

class qbertLevel (Level):
    def __init__ (self):

        Level.__init__(self)

        self.directory_name = 'qbert'
        self.track_enable_criteria = ('yes', 1, 2, 2, 3, 3, 3, 3)
        self.game_bg_criteria = ('yes',(1,2,3), 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes',(1,2,3), 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.fx_filt_max = (70, 45, 45, 60, 55, 65, 75, 60)
        self.fx_filt_period = (1920, 960,  1920, 480,  1920, 960,  1920, 960)
        self.section_boundaries = [8, 16, 24, 32]
        self.section_instances =   [0, 1, 2, 3, 0, 2, 3, 0, 1, 2]
        self.fx_stt         = (120, 0)
        self.fx_volume      = 50
        self.freestyle_points = [14, 20, 20]
        self.materials = ("drum",
                          "bass",
                          "drum",
                          "fx",
                          "fx",
                          "fx",
                          "lead",
                          "lead")

    def get_name (self):        return "Cosmic Assassins"
    def get_abbrev_name (self): return "Cosmic Assasins"
    def get_artist (self):      return "DJ QBert"
    def get_genre (self):       return "Turntablism"
    def get_tempo (self):       return "96"
    def get_description (self): return "DJ  QBert  is  widely  considered  the  greatest  skratch  DJ  in  the  world.   His  film  and  skratch  album  Wave  Twisters  received  international  attention  and  praise."
    def get_song_id (self):     return 16  # Return unique id for this song...

    # for metagame: 1 means yes, 0 means no
    def is_avail_game(self):    return 1
    def is_avail_jam(self):     return 1

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
            return 'echo'                   # Core 0 uses echo
        else:
            return 'studio a'               # Core 1 uses studio A

    # What volumes (left and right) should the effect be at for the given core?
    # Scale is 0-127
    def ps2_hard_effect_volumes (self, core):
        if core == 0:
            return [55, 55]             # core 0: 45 left, 45 right
        else:
            return [0, 0]             # core 1: 25 left, 25 right
        
    # What is the delay time for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_delay_time (self, core):
        if core == 0:
            return 63                  # core 0: 122
        else:
            return 0                   # core 1: 35
        
    # What is the feedback value for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_feedback (self, core):
        if core == 0:
            return 55                   # core 0: 45
        else:
            return 0                    # core 1: 0

def get_class_name ():
    return qbertLevel
