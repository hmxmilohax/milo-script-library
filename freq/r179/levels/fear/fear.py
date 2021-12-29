# Copyright 2000 Harmonix Music Systems.  All rights reserved.
#
# $Header: j:\\cvs/Freq/run/Levels/fear/fear.py,v 1.17 2001/09/26 03:59:18 guest Exp $
## sections:
#
# 0 chor no vox
# 1 verse1
# 2 verse1
# 3 chorus
# 4 verse2
# 5 bridge
# 6 bridge2
# 7 intro break
# 8 chorus
# 9 outtro

class fearLevel (Level):
    def __init__ (self):
        Level.__init__(self)

        self.directory_name = 'fear'
        self.track_enable_criteria = ('yes', 1, 1, 1, 1, 1, 1, 1)
        self.game_bg_criteria = ('yes','yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes','yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.fx_filt_period = (1920, 960,  1920, 480,  1920, 960,  1920, 960)
        self.fx_stt         = (120, 0)
        self.fx_volume      = 50
        self.num_laps         = [2, 4, 3, 3]
        self.freestyle_points = [6, 12, 14]
        self.section_boundaries = [8, 16, 24, 32, 44, 52, 60, 68, 76, 84]
        self.section_instances =   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 5, 6, 8, 9]
        self.materials = ("drum",
                          "drum",
                          "bass",
                          "guitar",
                          "guitar",
                          "vocal",
                          "lead",
                          "lead")

    def get_name (self):        return "Frequency"
    def get_abbrev_name (self): return "Frequency"
    def get_artist (self):      return "Fear Factory"
    def get_genre (self):       return "Industrial Rock"
    def get_tempo (self):       return "150"
    def get_description (self): return "Fear Factory returns to destroy your home gaming system with 'What is the Frequency.'  Please get your parent's permission before banging your head."
    def get_song_id (self):     return 9   # Return unique id for this song...
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
            return [90,90]               # Core 0 has delay time of 
        else:
            return [55,55]               # Core 1 has delay time of 
        
    # What is the delay time for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_delay_time (self, core):
        if core == 0:
            return 74                     # Core 0 has delay time of 35
        else:
            return 35                     # Core 1 has delay time of 74

    # What is the feedback value for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_feedback (self, core):
        if core == 0:
            return 65                   # core 0: 65
        else:
            return 25                   # core 1: 25

def get_class_name ():
    return fearLevel
