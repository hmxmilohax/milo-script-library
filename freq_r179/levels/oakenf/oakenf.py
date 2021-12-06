# Copyright 2000 Harmonix Music Systems.  All rights reserved.

class oakenfLevel (Level):
    def __init__ (self):

        Level.__init__(self)

        self.directory_name = 'oakenf'
        self.track_enable_criteria = ('yes', 1, 2, 3, 3, 2, 4, 1)
        self.game_bg_criteria = ('yes','yes', (1,5), (1,2,3,4,5), 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes','yes', (1,5), 'yes', 'yes', 'yes', 'yes', 'yes')
        self.fx_filt_max = (70, 45, 45, 60, 55, 65, 75, 60)
        self.fx_filt_period = (1920, 960,  1920, 480,  1920, 960,  1920, 960)
        self.fx_stt         = (120, 0)
        self.freestyle_points = [8, 12, 19]
        self.fx_volume      = 50
        self.materials = ("drum",
                          "bass",
                          "synth",
                          "vocal",
                          "drum",
                          "synth",
                          "fx",
                          "fx")

    def get_name (self):        return "See It"
    def get_abbrev_name (self): return "See It"
    def get_artist (self):      return "Paul Oakenfold"
    def get_genre (self):       return "Trance"
    def get_tempo (self):       return "135"
    def get_description (self): return "Paul Oakenfold is the world's number one DJ. No one else can claim such a seismic role in everything from the Balearic house explosion and the re-invention of British club culture to the birth of 'Madchester' and the high impact collision of dance and rock. www.pauloakenfold.com"
    def get_song_id (self):     return 14   # Return unique id for this song...

    # for metagame: 1 means yes, 0 means no
    def is_avail_game(self):    return 1
    def is_avail_jam(self):   return 1

    # Turn on a hardware effect for the given core?  1 for yes, 0 for no
    def ps2_use_hard_effect (self, core):
        return 1

    # What hardware effect to use on the given core?  Valid values are
    # 'room', 'studio a', 'studio b', 'studio c', 'hall', 'space',
    # 'echo', 'delay', 'pipe'
    def ps2_hard_effect_name (self, core):
        if core == 0:
            return 'echo'                   # Core 0 uses echo
        else:
            return 'delay'                  # Core 1 uses delay

    # What volumes (left and right) should the effect be at for the given core?
    # Scale is 0-127
    def ps2_hard_effect_volumes (self, core):
        if core == 0:
            return [45, 45]             # core 0: 25 left, 25 right
        else:
            return [65, 65]             # core 1: 45 left, 45 right
        
    # What is the delay time for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_delay_time (self, core):
        if core == 0:
            return 41                  # core 0: 41
        else:
            return 127                 # core 1: 127
        
    # What is the feedback value for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_feedback (self, core):
        if core == 0:
            return 25                   # core 0: 25
        else:
            return 50                   # core 1: 50

def get_class_name ():
    return oakenfLevel

#    if os.name == 'ps2':
#       self.jam_bg_criteria  = ((1,2,6), 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
#    else:
#       self.jam_bg_criteria  = ('yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')

