# Copyright 2000 Harmonix Music Systems.  All rights reserved. 

# sections:
#
# 0 8 bar chorus
# 1 8 bar verse 1
# 2 8 bar chorus
# 3 8 bar you want it
# 4 8 bar chorus
# 5 8 bar verse 2
# 6 8 bar you want it
# 7 8 bar chorus
# 8 8 bar chorus
# 9 8 bar break
# 10 8 bar break continued with pickup note
# 11 8 bar liar section
# 12 8 bar liar without pick up note


class powerLevel (Level):
    def __init__ (self):
        Level.__init__(self)

        self.directory_name = 'power'
        self.track_enable_criteria = ('yes', 1, 2, 3, 3, 4, 3, 4)
        self.game_bg_criteria = ('yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.fx_filt_period = (1920, 960,  1920, 480,  1920, 960,  1920, 960)
        self.fx_stt         = (120, 0)
        self.fx_volume      = 50
        self.num_laps         = [2, 4, 3, 3]
        self.freestyle_points = [6, 10, 12]
        self.section_boundaries = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104]
        self.section_instances =   [0, 1, 0, 3, 4, 5, 3, 4, 8, 9, 10, 11, 12]
        self.linked_sections = [[ [1,5], [9,10], [11,12], [0,8] ],
                                [ [1,5], [9,10], [11,12], [0,8] ],
                                [ [1,5], [9,10], [11,12] ],
                                [],
                                [ [1,5], [9,10], [11,12] ],
                                [ [1,5], [9,10], [11,12] ],
                                [],
                                []]

        self.materials = ("drum",
                          "drum",
                          "bass",
                          "vocal",
                          "guitar",
                          "guitar",
                          "lead",
                          "lead")

    def get_name (self):        return "Danger is Go"
    def get_abbrev_name (self): return "Danger is Go"
    def get_artist (self):      return "PowerMan 5000"
    def get_genre (self):       return "Industrial Rock"
    def get_tempo (self):       return "156"
    def get_description (self): return "They came from Boston, a raging crux of metallic funk juice, silver alloy inlayed sonic mayhem hurling through the atmosphere skimming under the radar as an identified flying object known only by the hidden codename of Powerman 5000. www.powerman5000.com"
    def get_song_id (self):     return 22   # Return unique id for this song...
    def wacko_panning (self):   return 0
    def use_linear_song_form (self): return 1
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
            return [45, 45]               # Core 0 has delay time of 30
        else:
            return [35, 35]               # Core 1 has delay time of 20
        
    # What is the delay time for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_delay_time (self, core):
        if core == 0:
            return 90                     # Core 0 has delay time of 90
        else:
            return 30                     # Core 1 has delay time of 30

    # What is the feedback value for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_feedback (self, core):
        if core == 0:
            return 75                   # core 0: 75
        else:
            return 40                   # core 1: 40

def get_class_name ():
    return powerLevel
