# Copyright 2000 Harmonix Music Systems.  All rights reserved.
#
# $Header: j:\\cvs/Freq/run/Levels/luge/luge.py,v 1.6 2001/09/26 04:44:42 guest Exp $
#

# sections:
#
# 0 8 bar verse 1
# 1 8 bar chorus 1 
# 2 8 bar verse 2
# 3 8 bar verse 1
# 4 8 bar break
# 5 8 bar chorus
# 6 8 bar verse 3



class lugeLevel (Level):
    def __init__ (self):
        Level.__init__(self)

        self.directory_name = 'luge'
        self.track_enable_criteria = ('yes', 1, 1, 1, 2, 2, 1, 1)
        self.game_bg_criteria = ('yes', (1,2,3), 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.fx_filt_period = (1920, 960, 1920, 480, 1920, 960, 1920, 960)
        self.fx_stt         = (240, 0)
        self.fx_volume      = 50
        self.stage_num      = 5
        self.num_laps         = [2, 4, 3, 3]
        self.freestyle_points = [12, 15, 20]
        self.section_boundaries = [8, 16, 24, 32, 40, 48, 56]
        self.section_instances =  [0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6]
        self.linked_sections = [[ [0,2], [1,5], [3,6] ],	#T1 synth
                                [ [0,6], [1,5] ],	        #T2 synth
                                [ [0,2], [1,5], [3,6] ],         #T3 drums1
                                [ [0,6], [1,5] ],		#T4 bass
                                [ [0,6] ],		        #T5 drums2
                                [ ],		                #T6 synth
                                [],
                                []]
        self.materials = ("synth",
                          "synth",
                          "drum",
                          "bass",
                          "drum",
                          "synth",
                          "lead",
                          "lead")

    def get_name (self):        return "Luge Crash"
    def get_abbrev_name (self): return "Luge Crash"
    def get_artist (self):      return "Mix Mistro Greg"
    def get_genre (self):       return "Germanik Tekno"
    def get_tempo (self):       return "120"
    def get_description (self): return "A true pioneer of the darkly bright Germanik tekno sound, Mix Mistro Greg lets the music take you for a ride. Just be careful you don't crash..."
    def get_song_id (self):     return 28   # Return unique id for this song...
    def wacko_panning (self):   return 0
    def use_bank_swapping (self): return 1
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
            return 'delay'               # Core 0 uses echo
        else:
            return 'delay'              # Core 1 uses delay

    # What volumes (left and right) should the effect be at for the given core?
    # Scale is 0-127
    def ps2_hard_effect_volumes (self, core):
        if core == 0:
            return [85, 85]               # Core 0 has delay time of 40
        else:
            return [0, 0]                 # Core 1 has delay time of 60

    # What is the delay time for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_delay_time (self, core):
        if core == 0:
            return 50                     # Core 0 has delay time of 60
        else:
            return 0                      # Core 1 has delay time of 70

    # What is the feedback value for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_feedback (self, core):
        if core == 0:
            return 45                   # core 0: 30
        else:
            return 0                    # core 1: 45

def get_class_name ():
    return lugeLevel
