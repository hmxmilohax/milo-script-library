# Copyright 2000 Harmonix Music Systems.  All rights reserved.

# sections:
#
# 0 intro
# 1 vox
# 2 keys/guitar/vox
# 3 = 2
# 4 spare
# 5 even sparer
# 6 = 2
# 7 = 2

class winnerLevel (Level):
    def __init__ (self):
        Level.__init__(self)

        self.directory_name = 'winner'
        self.track_enable_criteria = ('yes', 1, 1, 2, 2, 2, 2, 2)
        self.game_bg_criteria = ('yes',(1,2,3,4,5,6), (1,2,3,4,5,6), 'yes', 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes',(1,2), 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.fx_filt_period = (1920, 960,  1920, 480,  1920, 960,  1920, 960)
        self.fx_stt         = (120, 0)
        self.freestyle_points = [4, 6, 12]
        self.section_boundaries = [8, 16, 24, 32, 40, 48, 56, 64]
        self.section_instances   = [0, 1, 2, 3, 4, 5, 6, 7, 4, 5, 6, 7]
        self.linked_sections = [[ [2,3], [6,7] ],      #T1
                                [ [2,5,6], [0,3] ],    #T2
                                [ [2,3] ],             #T3
                                [ [2,6] ],             #T4
                                [ [2,6] ],             #T5
                                [],                    #T6
                                [],                    #T7
                                []]                    #T8
        self.materials = ("drum",
                          "drum",
                          "synth",
                          "bass",
                          "guitar",
                          "fx",
                          "lead",
                          "lead")

    def get_name (self):        return "The Winner"
    def get_abbrev_name (self): return "Winner"
    def get_artist (self):      return "The Crystal Method"
    def get_genre (self):       return "Big Beat"
    def get_tempo (self):       return "127"
    def get_description (self): return "Scott Kirkland and Ken Jordan aka The Crystal Method are back with their new album \"Tweekend.\" The bass-fortified, hard-rolling techno concoctions will get the club kids moving. www.thecrystalmethod.com"
    def get_song_id (self):     return 17  # Return unique id for this song...
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
            return 'delay'                # Core 0 uses delay
        else:
            return 'delay'                # Core 1 uses delay

    # What volumes (left and right) should the effect be at for the given core?
    # Scale is 0-127
    def ps2_hard_effect_volumes (self, core):
        if core == 0:
            return [65, 65]               # Core 0 has delay time of 50
        else:
            return [65, 65]               # Core 1 has delay time of 50
        
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
            return 45                   # core 0: 45
        else:
            return 55                   # core 1: 55

def get_class_name ():
    return winnerLevel
