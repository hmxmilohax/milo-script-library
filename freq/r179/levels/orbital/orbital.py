# Copyright 2000 Harmonix Music Systems.  All rights reserved.
#
# $Header: j:\\cvs/Freq/run/Levels/orbital/orbital.py,v 1.14 2001/09/26 04:48:25 guest Exp $
## sections:
#
# 0 8 breakdown chorus
# 1 8 build up chorus
# 2 8 bar 303 sect
# 3 8 bar 303 sect
# 4 chor sect1
# 5 chor sect2
# 6 chor sect3
# 7 8 bar 303 section

class orbitalLevel (Level):
    def __init__ (self):
        Level.__init__(self)

        self.directory_name = 'orbital'
        self.track_enable_criteria = ('yes', 1, 1, 1, 1, 1, 1, 1)
        self.game_bg_criteria = ('yes','yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes','yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.fx_filt_period = (1920, 960,  1920, 480,  1920, 960,  1920, 960)
        self.fx_stt         = (120, 0)
        self.fx_volume      = 50
        self.num_laps         = [2, 4, 3, 3]
        self.freestyle_points = [8, 16, 20]
        self.section_boundaries = [8, 16, 24, 32, 40, 48, 56, 64]
        self.section_instances =   [0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7]
        self.materials = ("drum",
                          "bass",
                          "synth",
                          "vocal",
                          "synth",
                          "drum",
                          "lead",
                          "lead")

    def get_name (self):        return "Funny Break-Weekend Ravers Mix"
    def get_abbrev_name (self): return "Funny Break"
    def get_artist (self):      return "Orbital"
    def get_genre (self):       return "Techno"
    def get_tempo (self):       return "130"
    def get_description (self): return "Orbital is manned by Phil and Paul Hartnoll. Ever since their first top 20 single in 1990, Chime, the brothers have been at the vanguard of dance music and have been responsible for some of the most beautiful machine- assisted music ever recorded.  www.loopz.co.uk"
    def get_song_id (self):     return 15  # Return unique id for this song...
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
            return 'delay'                 # Core 0 uses delay
        else:
            return 'hall'                  # Core 1 uses hall

    # What volumes (left and right) should the effect be at for the given core?
    # Scale is 0-127
    def ps2_hard_effect_volumes (self, core):
        if core == 0:
            return [70, 70]               # Core 0 has delay time of 55
        else:
            return [65, 65]               # Core 1 has delay time of 50
        
    # What is the delay time for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_delay_time (self, core):
        if core == 0:
            return 86                     # Core 0 has delay time of 86
        else:
            return 90                     # Core 1 has delay time of 90

    # What is the feedback value for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_feedback (self, core):
        if core == 0:
            return 40                   # core 0: 40
        else:
            return 65                   # core 1: 65

def get_class_name ():
    return orbitalLevel
