# Copyright 2000 Harmonix Music Systems.  All rights reserved.
#
# $Header: j:\\cvs/Freq/run/Levels/akro/akro.py,v 1.20 2001/10/10 20:51:07 anon Exp $
#

# sections:
#
# 0 8 bar verse 1
# 1 8 bar verse 2 
# 2 8 bar verse 3
# 3 8 bar half verse/chorus
# 4 8 bar half chorus/half verse
# 5 8 bar verse 4
# 6 8 bar verse 5
# 7 8 bar chorus2
# 8 8 bar beatbox1
# 9 8 bar beatbox2


class akroLevel (Level):
    def __init__ (self):
        Level.__init__(self)

        self.directory_name = 'akro'
        self.track_enable_criteria = ('yes', 1, 1, 1, 2, 2, 1, 1)
        self.game_bg_criteria = ('yes', (1,2,3), 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes', (1,2,3), 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.fx_filt_period = (1920, 960, 1920, 480, 1920, 960, 1920, 960)
        self.fx_stt         = (120, 0)
        self.fx_volume      = 50
        self.stage_num      = 2
        self.num_laps         = [2, 4, 3, 3]
        self.freestyle_points = [2, 3, 6]
        self.section_boundaries = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]
        self.section_instances =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.linked_sections = [[ [0,5], [2,4,6] ],	#T1 drums1
                                [ [0,2,5], [1,6] ],       #T2 bass
                                [ [0,5], [2,4,6] ],              #T3 drums2
                                [ [0,2], [1,9] ],		        #T4 synth1
                                [ [3,7], [2,8] ],                     #T5 synth2
                                [ [3,7], [8,9] ],		        #T6 vocals
                                [],
                                []]
        self.materials = ("drum",
                          "bass",
                          "drum",
                          "synth",
                          "synth",
                          "vocal",
                          "lead",
                          "lead")

    def get_name (self):        return "Exterminator"
    def get_abbrev_name (self): return "Exterminator"
    def get_artist (self):      return "Akrobatik"
    def get_genre (self):       return "hip-hop"
    def get_tempo (self):       return "96"
    def get_description (self): return "Boston born and raised, MC & producer Akrobatik is best known for his underground classics, \"Say Yes Say Word\" and \"Internet MC's.\" His self-titled EP on Detonator Records further solidifies his position as one of hip-hop's brightest new talents.  www.detonatorrecords.com"
    def get_song_id (self):     return 24   # Return unique id for this song...
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
            return 'delay'               # Core 0 uses delay
        else:
            return 'delay'              # Core 1 uses delay

    # What volumes (left and right) should the effect be at for the given core?
    # Scale is 0-127
    def ps2_hard_effect_volumes (self, core):
        if core == 0:
            return [60, 60]               # Core 0 has delay time of 40
        else:
            return [0, 0]                 # Core 1 has delay time of 60

    # What is the delay time for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_delay_time (self, core):
        if core == 0:
            return 60                     # Core 0 has delay time of 60
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
    return akroLevel
