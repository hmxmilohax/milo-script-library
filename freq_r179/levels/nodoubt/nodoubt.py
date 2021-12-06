# Copyright 2000 Harmonix Music Systems.  All rights reserved.

# 0 4bar chorus/4 bar break
# 1 8 bar verse1
# 2 8 bar chorus
# 3 8 bar verse2
# 4 8 bar chorus2 [same as chor1]
# 5 8 bar break/beginning of verse3
# 6 12 bar verse/rap
# 7 8 chorus3 [held vocals at end]
# 8 8 tekno break down [playable vocals]
# 9 8 bar chorus [same as sect2 and 4]

class nodoubtLevel (Level):
    def __init__ (self):
        Level.__init__(self)

        self.directory_name = 'nodoubt'
        self.short_name = 'nodoubt'
        self.track_enable_criteria = ('yes', 1, 2, 2, 3, 3, 3, 3)
        self.game_bg_criteria = ('yes',(6), 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes',(6), 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.fx_filt_period = (1920, 960,  1920, 480,  1920, 960,  1920, 960)
        self.fx_stt         = (120, 0)
        self.fx_volume      = 50
        self.num_laps         = [3, 4, 3, 3]
        self.freestyle_points = [8, 20, 20]
        self.section_boundaries = [8, 16, 24, 32, 40, 48, 60, 68, 76, 84]
        self.section_instances =   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 7]
        self.linked_sections = [[ [1,3], [2,4], [7,8] ],          #T1 drums
                                [ [1,3], [2,4] ],                 #T3 bass
                                [ [4,9] ],                        #T4 synth
                                [ [7,8], [4,9] ],                 #T2 vocals
                                [ [1,3], [2,4] ],                 #T5 guitar
                                [ [1,3], [2,4], [7,8] ],          #T6 drums2
                                [],                        #T7
                                []]                        #T8

        self.materials = ("drum",
                          "bass",
                          "synth",
                          "vocals",
                          "guitar",
                          "drum",
                          "lead",
                          "lead")

    def use_bank_swapping (self): return 1

    def get_name (self):        return "Ex-Girlfriend"
    def get_abbrev_name (self): return "Ex-Girlfriend"
    def get_artist (self):      return "No Doubt"
    def get_genre (self):       return "Electronic Rock"
    def get_tempo (self):       return "100"
    def get_description (self): return "Formed in Anaheim, California in 1987, No Doubt deliver a signature mix of rock, reggae, and new-wave musical styles. Their most widely known works include Tragic Kingdom and Return of Saturn. www.nodoubt.com"
    def get_song_id (self):     return 29   # Return unique id for this song...
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
            return [20, 20]                 # Core 0 has delay depth of 5
        else:
            return [45, 45]                 # Core 1 has delay depth of 30
        
    # What is the delay time for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_delay_time (self, core):
        if core == 0:
            return 25                     # Core 0 has delay time of 25
        else:
            return 40                     # Core 1 has delay time of 40

    # What is the feedback value for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_feedback (self, core):
        if core == 0:
            return 15                   # core 0: 15
        else:
            return 40                   # core 1: 40

def get_class_name ():
    return nodoubtLevel
