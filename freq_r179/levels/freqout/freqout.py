# Copyright 2000 Harmonix Music Systems.  All rights reserved.

class freqoutLevel (Level):
    def __init__ (self):
        Level.__init__(self)

        self.directory_name = 'freqout'
        self.track_enable_criteria = ('yes', 1, 2, 3, 4, 5, 6, 7)
        self.game_bg_criteria = ('yes','yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes','yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.fx_filt_period = (1920, 960,  1920, 480,  1920, 960,  1920, 960)
        self.fx_stt         = (120, 0)
        self.fx_volume      = 50
        self.freestyle_points = [12, 15, 20]
        self.num_laps         = [2, 4, 3, 3]
        self.section_boundaries = [8, 16, 24, 32, 40, 48]
        self.section_instances =  [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]
        self.materials = ("drum",
                          "fx",
                          "synth",
                          "drum",
                          "bass",
                          "synth",
                          "lead",
                          "lead")

    def get_name (self):        return "Freq Out"
    def get_abbrev_name (self): return "FreQouT"
    def get_artist (self):      return "Symbion Project"
    def get_genre (self):       return "Hard Breakz"
    def get_tempo (self):       return "155"
    def get_description (self): return "Symbion Project hitz you one last time with an aggressive breakbeat masterpiece. This one is going to wear you down. visit www.symbionproject.com"
    def get_song_id (self):     return 10   # Return unique id for this song...
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
            return 'delay'                # Core 1 uses delay

    # What volumes (left and right) should the effect be at for the given core?
    # Scale is 0-127
    def ps2_hard_effect_volumes (self, core):
        if core == 0:
            return [40, 40]               # Core 0 has delay depth of 25
        else:
            return [65, 65]               # Core 1 has delay depth of 50
        
    # What is the delay time for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_delay_time (self, core):
        if core == 0:
            return 90                     # Core 0 has delay time of 90
        else:
            return 127                    # Core 1 has delay time of 127

    # What is the feedback value for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_feedback (self, core):
        if core == 0:
            return 35                   # core 0: 35
        else:
            return 50                   # core 1: 50

def get_class_name ():
    return freqoutLevel
