# Copyright 2000 Harmonix Music Systems.  All rights reserved.

# sections:
# 0 8 bar intro
# 1 8 bar verse 1
# 2 12 bar filt drums
# 3 12 bar section
# 4 break
# 5 chorus
# 6 chorus

class MbmLevel (Level):
    def __init__ (self):
        Level.__init__(self)

        self.directory_name = 'mbm'
        self.track_enable_criteria = ('yes', 1, 2, 3, 3, 4, 3, 4)
        self.game_bg_criteria = ('yes',(4,6), (1,2,3,4,5,6), 'yes', 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes',(4,6), (1,2), 'yes', 'yes', 'yes', 'yes', 'yes')
        self.fx_filt_period = (1920, 960,  1920, 480,  1920, 960,  1920, 960)
        self.fx_stt         = (120, 0)
        self.fx_volume      = 50
        self.num_laps         = [2, 4, 3, 3]
        self.freestyle_points = [18, 20, 20]
        self.section_boundaries = [8, 16, 28, 40, 48, 56, 64]
        self.section_instances =   [0, 1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 6]
        self.linked_sections = [[],                    #T1
                                [],                    #T2
                                [],                    #T3
                                [],                    #T4
                                [],                    #T5
                                [],                    #T6
                                [],                    #T7
                                []]                    #T8
        self.materials = ("drum",
                          "drum",
                          "bass",
                          "synth",
                          "fx",
                          "fx",
                          "lead",
                          "lead")

    def get_name (self):        return "Dynamyte Fresh"
    def get_abbrev_name (self): return "Dynamyte Fresh"
    def get_artist (self):      return "Meat Beat Manifesto"
    def get_genre (self):       return "Beats in Space"
    def get_tempo (self):       return "134"
    def get_description (self): return "Meat Beat Manifesto is Jack Dangers - widely acknowledged for his sonic inventions in the realm of electronic music as recording artist, producer and remixer. Recent works include his guise as co-creator of Tino, performed live as Tino Corp.  www.tinocorp.com"
    def get_song_id (self):     return 18   # Return unique id for this song...
    def wacko_panning (self):   return 0
    def use_linear_song_form (self):
        return 1

    def use_bank_swapping (self): return 1

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
            return [75, 75]               # Core 0 has delay time of 60
        else:
            return [00, 00]               # Core 1 has delay time of 00
        
    # What is the delay time for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_delay_time (self, core):
        if core == 0:
            return 90                     # Core 0 has delay time of 90
        else:
            return 00                     # Core 1 has delay time of 00

    # What is the feedback value for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_feedback (self, core):
        if core == 0:
            return 40                   # core 0: 40
        else:
            return 0                    # core 1: 0

def get_class_name ():
    return MbmLevel
