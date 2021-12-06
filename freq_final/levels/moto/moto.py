# Copyright 2000 Harmonix Music Systems.  All rights reserved.

class motoLevel (Level):
    def __init__ (self):
        Level.__init__(self)

        self.directory_name = 'moto'
        self.track_enable_criteria = ('yes', 1, 2, 3, 3, 4, 3, 4)
        self.game_bg_criteria = ('yes',(1,2,3,4), (1,2), (1), (1), 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes',(4,6), (1,2), 'yes', 'yes', 'yes', 'yes', 'yes')
        self.fx_filt_period = (1920, 960,  1920, 480,  1920, 960,  1920, 960)
        self.fx_stt         = (120, 0)
        self.fx_volume      = 50
        self.num_laps         = [3, 4, 3, 3]
        self.freestyle_points = [5, 7, 10]
        self.section_boundaries = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96]
        self.section_instances =   [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 6, 10, 11]
        self.linked_sections = [[ [0,6], [4,10] ],         #T1 drums
                                [ [5,11] ],         #T2 drums2
                                [ [0,6], [4,10] ],         #T3 bass
                                [ [5,11] ],         #T4 synth1
                                [ [0,6], [4,10] ],         #T5 synth2
                                [ [5,11] ],         #T6 synth3
                                [],                    #T7
                                []]                    #T8
 
        self.materials = ("drum",
                          "drum",
                          "bass",
                          "synth",
                          "synth",
                          "synth",
                          "lead",
                          "lead")

    def get_name (self):        return "Motomatic"
    def get_abbrev_name (self): return "Motomatic"
    def get_artist (self):      return "Tony Trippi"
    def get_genre (self):       return "hard electro"
    def get_tempo (self):       return "135"
    def get_description (self): return "Old school computer game composer Tony Trippi crashes through your living room wall with his high-octane jam, \"Motomatic.\" Since 1988, Tony has been droppin' the grooves that make the video kids freak. Get behind the wheel and get your groove on yo!  www.tonytrippi.com"
    def get_song_id (self):     return 13  # Return unique id for this song...
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
            return [40, 40]               # Core 0 has delay depth of 40
        else:
            return [55, 55]               # Core 1 has delay depth of 50
        
    # What is the delay time for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_delay_time (self, core):
        if core == 0:
            return 65                     # Core 0 has delay time of 65
        else:
            return 45                     # Core 1 has delay time of 45

    # What is the feedback value for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_feedback (self, core):
        if core == 0:
            return 30                   # core 0: 30
        else:
            return 45                   # core 1: 45

def get_class_name ():
    return motoLevel
