# Copyright 2000 Harmonix Music Systems.  All rights reserved.

class FunkyDopeLevel (Level):
    def __init__ (self):
        Level.__init__(self)

        self.directory_name = 'funkydope'
        self.track_enable_criteria = ('yes', 1, 2, 3, 3, 4, 3, 4)
        self.game_bg_criteria = ((1,2),'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes',(1,2), 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.fx_filt_period = (1920, 960,  1920, 480,  1920, 960,  1920, 960)
        self.fx_stt         = (120, 0)
        self.fx_volume      = 50
        self.freestyle_points = [10, 12, 15]
        self.materials = ("drum",
                          "drum",
                          "bass",
                          "synth",
                          "fx",
                          "fx",
                          "lead",
                          "lead")

    def get_name (self):        return "Funky Dope Maneuver"
    def get_abbrev_name (self): return "Funky Dope"
    def get_artist (self):      return "Symbion Project"
    def get_genre (self):       return "Big Beat"
    def get_tempo (self):       return "140"
    def get_description (self): return "The Symbion Project is the brainchild of the electronic guru Kasson Crooker. Boogie down to the funky beatz. Check out www.symbionproject.com for more music!"
    def get_song_id (self):     return 3   # Return unique id for this song...
    def wacko_panning (self):   return 0

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
            return 'echo'                 # Core 0 uses echo
        else:
            return 'delay'                # Core 1 uses delay

    # What volumes (left and right) should the effect be at for the given core?
    # Scale is 0-127
    def ps2_hard_effect_volumes (self, core):
            return [55, 55]               # Both cores have volumes of 40
        
    # What is the delay time for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_delay_time (self, core):
        if core == 0:
            return 127                    # Core 0 has delay time of 127
        else:
            return 117                    # Core 1 has delay time of 117

    # What is the feedback value for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_feedback (self, core):
        if core == 0:
            return 25                   # core 0: 25
        else:
            return 45                   # core 1: 45

def get_class_name ():
    return FunkyDopeLevel
