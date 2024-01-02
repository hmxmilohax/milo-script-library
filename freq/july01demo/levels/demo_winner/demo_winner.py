# Copyright 2000 Harmonix Music Systems.  All rights reserved.
#
# $Header: j:\\cvs/Freq/run/Levels/demo_winner/demo_winner.py,v 1.2.2.1 2001/07/19 13:52:14 jon Exp $
#
# $Log: demo_winner.py,v $
# Revision 1.2.2.1  2001/07/19 13:52:14  jon
# change from Josh
#
# Revision 1.2  2001/06/12 18:29:03  kasson
# added BG enable text
#
# Revision 1.1  2001/06/12 16:11:54  kasson
# *** empty log message ***
#
# Revision 1.15  2001/06/11 17:19:26  kasson
# trying out a new axe
#
# Revision 1.14  2001/06/05 16:49:44  kasson
# level 4
#
# Revision 1.13  2001/06/05 16:17:00  kasson
# level 5
#
# Revision 1.12  2001/06/05 15:26:47  kasson
# now a level stage 3
#
# Revision 1.11  2001/05/16 16:36:34  anon
# even shorter
#
# Revision 1.10  2001/05/16 15:51:05  anon
# shortened
#
# Revision 1.9  2001/05/16 15:02:27  dfan
# Rearranged sections so player wouldn't see empty ones for so long in a row
#
# Revision 1.8  2001/05/10 17:44:21  kasson
# shortened song by 4 sections
#
# Revision 1.7  2001/05/09 21:58:28  kasson
# now a level stage 2 for E3
#
# Revision 1.6  2001/05/08 19:17:12  kasson
# new bg_enable values
#
# Revision 1.5  2001/05/08 18:43:40  anon
# enabled jam mode
#
# Revision 1.4  2001/05/06 20:49:12  anon
# fixed
#
# Revision 1.3  2001/05/06 20:16:58  robotkid
# updated ctm bio
#
# Revision 1.2  2001/04/30 19:59:33  anon
# fixed bug
#
# Revision 1.1  2001/04/30 19:29:31  kasson
# *** empty log message ***
#

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

        self.directory_name = 'demo_winner'
        self.short_name = 'winner'
        self.track_enable_criteria = ('yes', 1, 2, 3, 3, 4, 3, 4)
        self.game_bg_criteria = ('yes',(1,2,3,4,5,6), (1,2,3,4,5,6), 'yes', 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes',(1,2), 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.fx_filt_period = (1920, 960,  1920, 480,  1920, 960,  1920, 960)
        self.fx_stt         = (120, 0)
        self.section_boundaries = [8, 16, 24, 32, 40, 48, 56, 64]
        # self.section_instances = [0, 1, 2, 3, 4, 5, 6, 7, 0, 2, 5, 7]
        self.section_instances   = [0, 1, 2, 2, 4, 5, 6, 6, 4, 5, 7, 7]
        self.stage_num      = 4
        self.materials = ("drum",
                          "drum",
                          "synth",
                          "bass",
                          "guitar",
                          "fx",
                          "lead",
                          "lead")

    def get_name (self):        return "The Winner"
    def get_artist (self):      return "The Crystal Method"
    def get_genre (self):       return "Big Beat"
    def get_tempo (self):       return "127"
    def get_description (self): return "The Crystal Method are back with 'Tweekend,' the follow-up to their debut album, 'Vegas.' www.thecrystalmethod.com"
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
            return [50, 50]               # Core 0 has delay time of 50
        else:
            return [50, 50]               # Core 1 has delay time of 50
        
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
