# Copyright 2000 Harmonix Music Systems.  All rights reserved.

# sections:
#
# 0 instrumental intro
# 1 verse 1
# 2 chorus
# 3 instrumental - break at end
# 4 verse 2
# 5 chorus
# 6 chorus
# 7 bridge
# 8 chorus
# 9 chorus


class dubpistolsLevel (Level):
    def __init__ (self):
        Level.__init__(self)

        self.directory_name = 'dubpistols'
        self.track_enable_criteria = ('yes', 1, 1, 1, 1, 1, 1, 1)
        self.game_bg_criteria = ('yes',(4,6), (1,2,3,4,5,6), 'yes', 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes',(4,6), (1,2), 'yes', 'yes', 'yes', 'yes', 'yes')
        self.fx_filt_period = (1920, 960,  1920, 480,  1920, 960,  1920, 960)
        self.fx_stt         = (120, 0)
        self.fx_volume      = 50
        self.freestyle_points = [3, 4, 7]
        self.num_laps         = [2, 4, 3, 3]
        self.section_boundaries = [8, 16, 24, 32, 44, 52, 60, 68, 76, 84]
        self.section_instances =   [0, 1, 2, 3, 4, 5, 0, 1, 2, 5]
        self.linked_sections = [[],
                                [],
                                [],
                                [],
                                [],
                                [],
                                [],
                                []]
        self.materials = ("drum",
                          "drum",
                          "bass",
                          "guitar",
                          "vocal",
                          "guitar",
                          "lead",
                          "lead")

    def get_name (self):        return "Official Chemical"
    def get_abbrev_name (self): return "Official Chem"
    def get_artist (self):      return "Dub Pistols"
    def get_genre (self):       return "beats'n'rhymes"
    def get_tempo (self):       return "125"
    def get_description (self): return "The Dub Pistols' Barry Ashworth is a fearless soldier working behind the frontlines of the UK's thriving dance music scene. Barry began his musical journey by working as a club promoter and formed the Dub Pistols in 1996.  www.dubpistols.net"
    def get_song_id (self):     return 8   # Return unique id for this song...
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
            return 'echo'                # Core 1 uses delay

    # What volumes (left and right) should the effect be at for the given core?
    # Scale is 0-127
    def ps2_hard_effect_volumes (self, core):
        if core == 0:
            return [45, 45]               # Core 0 has delay time of 30
        else:
            return [45, 45]               # Core 1 has delay time of 30
        
    # What is the delay time for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_delay_time (self, core):
        if core == 0:
            return 47                     # Core 0 has delay time of 52
        else:
            return 52                     # Core 1 has delay time of 52

    # What is the feedback value for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_feedback (self, core):
        if core == 0:
            return 45                   # core 0: 45
        else:
            return 45                   # core 1: 45

def get_class_name ():
    return dubpistolsLevel
