# Copyright 2000 Harmonix Music Systems.  All rights reserved. 

# sections:
# 0 8 bar intro     A
# 1 8 bar verse1    B
# 2 8 bar verse2    B
# 3 8 bar chorus1   C
# 4 8 bar chorus2   C
# 5 8 bar verse3    B
# 6 8 bar verse4    B
# 7 8 bar verse5    B
# 8 8 bar chorus3 [synths differs from chorus1]  C
# 9 8 bar chorus4 [synths differs from chorus1]  C
# 10 8 bar breakdown  D
# 11 8 bar verse 1b [different music]  B
# 12 8 bar chorus5  C
# 13 8 bar chorus6  C
# 14 8 bar verse 1c B

class jungleLevel (Level):
    def __init__ (self):
        Level.__init__(self)

        self.directory_name = 'jungle'
        self.track_enable_criteria = ('yes', 1, 1, 1, 1, 1, 1, 1)
        self.game_bg_criteria = ('yes','yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes','yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.fx_filt_period = (1920, 960,  1920, 480,  1920, 960,  1920, 960)
        self.fx_stt         = (120, 0)
        self.fx_volume      = 50
        self.num_laps         = [2, 4, 3, 3]
        self.freestyle_points = [10, 12, 18]
        self.section_boundaries = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120]
        self.section_instances =   [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 10, 11, 12, 13, 14, 12, 13]
        self.linked_sections = [[ [1,2], [3,4], [5,6], [0,10], [11,14], ],         #T1 drums
                                [ [1,2], [3,4], [5,6], [0,10], [11,14] ],         #T2 drums2
                                [ [1,2], [3,4], [5,6], [11,14] ],          #T3 bass
                                [ [0,10], [5,7], [11,14] ],         #T4 synth1
                                [ [1,2], [5,7] ],         #T5 synth2
                                [ [3,4] ],                    #T6 vocals
                                [],                    #T7
                                []]                    #T8
        self.materials = ("drum",
                          "drum",
                          "bass",
                          "synth",
                          "synth",
                          "vocal",
                          "lead",
                          "lead")

    def get_name (self):        return "What's the Five O"
    def get_abbrev_name (self): return "What's the Five O"
    def get_artist (self):      return "Jungle Brothers"
    def get_genre (self):       return "Drum & Bass"
    def get_tempo (self):       return "172"
    def get_description (self): return "Hip-hop pioneers the Jungle Brothers, Mike G & Afrika, have always pushed the boundaries of hip-hop. From founding the Afrocentric Native Tongues movement through to the smash hit Drum & Bass sound of \"Jungle Brother\" (UrbanTakeover Mix)."
    def get_song_id (self):     return 27   # Return unique id for this song...
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
            return [45, 45]               # Core 0 has delay time of 30
        else:
            return [95, 95]               # Core 1 has delay time of 87
        
    # What is the delay time for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_delay_time (self, core):
        if core == 0:
            return 40                     # Core 0 has delay time of 40
        else:
            return 65                     # Core 1 has delay time of 65

    # What is the feedback value for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_feedback (self, core):
        if core == 0:
            return 30                   # core 0: 30
        else:
            return 70                   # core 1: 70

def get_class_name ():
    return jungleLevel
