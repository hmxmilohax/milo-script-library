##############################################################################
#
# Copyright 2000 Harmonix Music Systems.  All rights reserved.
#
# $Header: j:\\cvs/Freq/run/Global/defaults.py,v 1.191 2001/10/12 14:01:56 dfan Exp $
#
##############################################################################

import os
import os.path
import types
import whrandom
from types import *

level_list = {}                         # dict: level name -> instance
arena_list = {}                         # dict: arena name -> instance
current_level = None                    # An instance of the current level
current_arena = None                    # An instance of the current arena

# Call when leaving a level
def reset_current_level ():
    current_level = None
    current_arena = None
    global remix_playback
    remix_playback = 0
    
def current_level_exists ():
    return (current_level != None)

def global_execfile (f) :
    execfile (f, globals())

# Return the absolute pathname of the given script that can be found in the
# subdirectory 'where' of the FreQ tree.
#
def get_script (name, where):
    return get_script_with_suffix (name, '', where)

# Return the absolute pathname of the given script that can be found in the
# subdirectory 'where' of the FreQ tree.
#
def get_script_with_suffix (name, suffix, where):
    return get_absolute_path ("%s/%s/%s%s.py" % (where, name, name, suffix))

# Helper function for get_level_scripts
#
def full_level_path (name):
    return os.path.join (root, get_script (name, 'levels'))

def full_arena_path (name):
    return os.path.join (root, get_script (name, 'arenas'))

def get_stage_beatval (stagenum, difficulty):
   return beat_stages_lookup[stagenum][difficulty]

def get_secret_levels():
   return secret_levels

# LevelOverride is a class containing the user's customizations
# to the way levels work.  The default implementation of LevelOverride
# overrides nothing.  Define your own in autoexec.py if you want to
# override anything.

class LevelOverride:
    def __init__(self): pass            # Dummy constructor

# Create and return an instance of a custom class that multiply derives from
# LevelOverride and cl.

def make_level (cl, script_file):
    assert isinstance (cl, types.ClassType)

    # Make a new class that inherits from LevelOverride (first, so that its
    # attributes will be checked first) and cl
    class NewClass (LevelOverride, cl): pass

    # Make an instance of that class, and call constructors by hand
    level = NewClass()
    cl.__init__(level)
    LevelOverride.__init__(level)
    level.file_name = script_file
    
    return level

# Run every level script file and create an instance of a custom
# class that multiply derives from LevelOverride and that level.
# This instance then goes into level_list, indexed by level name.

def load_level_scripts ():
    for (_name, _stage, _order) in levels_database:
        script = full_level_path (_name)
        global_execfile (script)
        inst = make_level (get_class_name(), script)
        level_list[inst.directory_name] = inst
        inst.stage = _stage
        inst.order = _order


def load_arena_scripts ():
    for (_name, _order) in arenas_database:
        script = full_arena_path (_name)
        global_execfile (script)
        inst = get_arena_class_name() ()
        arena_list[inst.directory_name] = inst
        inst.order = _order

# For a standard game level, just remove instances of the tutorials from the
# level_list and call the desired level's make_current method.  For a tutorial
# level, we need to reexecute its python script and add a new instance of that
# class to the level_list.  The other tutorial level's instancd should be
# removed from the level list also... 
def set_current_level (level_name):
    global level_list
    if level_name != 'tutorialrmx' and level_name != 'tutorial':
        try:
            del level_list['tutorial']
            del level_list['tutorialrmx']
        except KeyError:
            pass
        #try:
        #except KeyError:
        
        level_list[level_name].make_current ()
        return None
    elif level_name == 'tutorial':
        full_name = full_level_path (level_name)
        bad_name = full_level_path ('tutorialrmx')
    else:
        full_name = full_level_path (level_name)
        bad_name = full_level_path ('tutorial')

    global_execfile (full_name)
    inst = make_level (get_class_name(), full_name)
    level_list[inst.directory_name] = inst
    level_list[inst.directory_name].make_current ()

## Does a level with the given name and the given suffix exist?

#def level_exists (name, suffix):
#    return os.path.exists (get_script_with_suffix (name, suffix, 'levels'))

## Return a string-list of levels
#
def get_levels ():
    names = map (lambda x: x.directory_name, level_list.values())
    return names

## Return a string-list of arenas for a game community
#
def get_arenas (com):
    global arena_list
    out = []
    for a in arena_list.values():
        if a.available_in (com):
            out.append(a.directory_name)
    return out


# This procedure is invoked just before InitInstance() returns. The default
# implementation does nothing, but redefining the procedure enables code to 
# run automatically at application start up.

def autoexec ():
    pass

# Do an execfile of the file NAME, if it exists.
# It is loaded into the global namespace.

def exec_if_exists (name):
    if os.path.exists (name):
        global_execfile (name)
        return 1
    else:
        return 0

# Use attract mode or not
def use_attract_mode ():
    return 1

# How many seconds to idle before diving into attract mode
def idle_secs_before_attract ():
    return 90

which_recording = -1
def choose_random_recording ():
    global which_recording
    which_recording += 1
    if which_recording >= len(recording_files):
        which_recording -= len(recording_files)
    return recording_files[which_recording]


##################################################
#
#  Expansion pack support
#

album_song_list = {}                     # Dict of song name -> song id
album_arena_list = {}                    # Dict of arena name -> arena id

def init_album_song_list ():
    if len(level_list) == 0:
        raise RuntimeError, "Couldn't get song_list from album"
    for level in level_list.keys():
        # Fill in a map using the songs' directory name and unique id
        #print level, '  ', level_list[level].get_song_id()
        album_song_list[level] = level_list[level].get_song_id()

def init_album_arena_list ():
    if len(arena_list) == 0:
        raise RuntimeError, "Couldn't get arena_list from album"
    for arena in arena_list.keys():
        # Fill in a map using the arenas' directory name and unique id
        album_arena_list[arena] = arena_list[arena].get_arena_id()

# To initialize a new album, we need to reload album.py.  We then dump the
#  old level instances from level_list and load the new ones.  The same is
#  done for arenas...
def init_new_album ():
    hx.clear_album_cache ()
    global_execfile (get_absolute_path ('levels/album.py'))

    # Get rid of old levels, load new ones...
    if len(level_list) != 0:
        level_list.clear ()
    load_level_scripts ()
    init_album_song_list ()

    # Get rid of old arenas, load new ones...
    if len(arena_list) != 0:
        arena_list.clear ()
    load_arena_scripts ()
    init_album_arena_list ()

# Check for a level's presence on a disc.  If it's in the album_song_list
#  then it's present and we return 1, otherwise it isn't and we return 0.
def is_level_on_album (level_name):
    return album_song_list.has_key(level_name)

# Check for an arena's presence on a disc.  If it's in the album_song_list
#  then it's present and we return 1, otherwise it isn't and we return 0.
def is_arena_on_album (arena_name):
    return album_arena_list.has_key(arena_name)


######################################################################


###################
#
# Global functions

# Return the name of the screen driver to use for rendering the main view.
def get_screen_driver ():
#   return "rgdgl5"                                       # Open GL
#   return "rgdrw5"                                       # RenderWare
#   return "rgdd3d5"                                      # Direct 3D
    return "rgdglide35"                                   # 3DFX Glide
#   return "rgdnull5"                                     # Null Driver

# Return the preferred display resolution as a structure consisting of the
# components: {width height bits-per-pixel refresh-rate}.The last 2 values
# can each be 0, in which case the current Windows desktop values are used.
def get_screen_config ():  return (640, 480, 16, 1)


def show_timers ():
    return 0
    
def show_stats ():
    return 0
    
# change desktop to 800x600 before running game?
def show_gui_fullscreen ():
    return 1

# splash screen
def show_splash_screen ():
    return 1

# Get 2 players happening on a single machine. Good for testing pitching &
# catching on a single machine.
def two_player_local ():
    return 0

# return a string that represents the synth we should use.
# values may be "seer", "midiout"
def get_global_synth ():
    return "seer"


# if this returns true, we never load the metagame and instead play the level
# described by default_game_params. Hit gamepad "X" to start that game
def skip_metagame () : return 0

# if we skip the metagame, use these game params to figure out which game to play
# (<level-name>, <ruleset>, <skill-level>, <num-players>, '<arena-name>)
default_game_params = ['Funky Dope Maneuver', 'game', 0, 1, 'Blue']


# hx::input add <player> <evt> <evt-data> <dev> <dev-num> <key/button>
#           disable <player> <evt>
#           enable <player> <evt>
# 
# <device-type> can be "mouse", "key", or "joy"
# <event> can be "rotL", "rotR", (rotate left/right)
#                "rpch", "rswg" (pitch, swing)
# <event-data> is required only for rpch

# PSX Controller Button ID's:
#
#    5                     6		Bottom Triggers
# 
#    7                     8		Top Triggers
# 
# 
#    13                    1		
# 
# 16 >< 14    9   10    4  x  2		D-Pad, Action Buttons
# 
#    15                    3
# 
# 
#   (2)                   (4)		Thumbsticks
#    |                     |
# ---12--(1)            ---11--(3)
#    |                     |
#    |                     |

JOY_TRIANGLE = 1
JOY_CIRCLE   = 2
JOY_X        = 3
JOY_SQUARE   = 4
JOY_L2       = 5
JOY_R2       = 6
JOY_L1       = 7
JOY_R1       = 8
JOY_SELECT   = 9
JOY_START    = 10
JOY_RTHUMB   = 11
JOY_LTHUMB   = 12
JOY_UP       = 13
JOY_RIGHT    = 14
JOY_DOWN     = 15
JOY_LEFT     = 16

JOY_LTHUMB_X = 1
JOY_LTHUMB_Y = 2
JOY_RTHUMB_X = 3
JOY_RTHUMB_Y = 4


# Define this function to do whatever you want based on a key down msg sent
# to the game.
def on_key_down (key):
    pass

# if using "seer", show the seer player while the game is running?
def show_seerplayer ():
    return 0

# if using "midiout", which device number to use?
def get_midi_device ():
    return 0

community = 'Undefined'
ruleset = 'Undefined'
gem_difficulty = 'Undefined'
num_players = None
remix_playback = 0                      # Are we playing back a remix?

# Sets the community-type for this level: solo, local, net
def set_community (name):
    global community
    community = name
   
# Sets the ruleset for this level: game, jam
def set_ruleset (name):
    global ruleset
    ruleset = name

# Sets the value of remix_playback for this level
def set_remix_playback (val):
    global remix_playback
    remix_playback = val

# Sets the difficulty for this level: 0, 1, or 2
# 0==easy, 1==medium, 2==hard
def set_gem_difficulty (num):
    global gem_difficulty
    gem_difficulty = num

# sets the number of players for this level: 1,2,3,4
def set_num_players (num):
    global num_players
    num_players = num

def call_handler (func, *args):
    if (current_level):
        try: apply (getattr (current_level, func), args)
        except AttributeError: pass

        try: apply (getattr (current_arena, func), args)
        except AttributeError: pass

# converts track enablement criteria to a format that is easy for code to understand
def massage_criteria (criteria):
    if criteria == 'yes':
        return []
    elif type(criteria) is IntType:
        return (criteria,)
    else:
        return criteria

# Important note: This name table must be identical to the c++ enum found in
# GsPowerupTypes.h
powerup_nums = { 'neu':0,  'crp':1,  'fre':2,  'aut':3,  'bum':4,
                 'vol':5,  'wah':6,  'stt':7,  'ech':8,
                 'flg':9,  'cho':10, 'gho':11, 'mul':12 }

def powerup_num (name):
    try:
        return powerup_nums[name]
    except KeyError:
        raise KeyError ('Not a valid powerup name:%s' % name)

class MetagameBankCycler:
    def __init__ (_, num_banks):
        _.num_banks = num_banks
        _.bank = 1
        _.provided_bank = 0
        _.provided_header = 0

    def update_bank (_):
        if _.provided_bank and _.provided_header:
            _.provided_bank = 0
            _.provided_header = 0
            _.bank += 1
            if _.bank > _.num_banks:
                _.bank = 1

    def get_bank (_):
        b = _.bank
        _.provided_bank = 1
        _.update_bank()
        return b

    def get_header (_):
        b = _.bank
        _.provided_header = 1
        _.update_bank()
        return b

bank_cycler = MetagameBankCycler(10)

def get_ps2_metagame_hard_bank (cd=0):
   s = get_absolute_path ("MetaGame/Sounds/sfx_meta_bank_%d.bd" % bank_cycler.get_bank())
   return s

def get_ps2_metagame_hard_bank_header (cd=0):
   s = get_absolute_path ("MetaGame/Sounds/sfx_meta_bank_%d.hd" % bank_cycler.get_header())
   return s

def get_effects_bank ():
    return get_absolute_path ("global/gamefx.bd")

def get_effects_bank_header ():
    return get_absolute_path ("global/gamefx.hd")

# Keep in sync with /usr/local/sce/common/include/sdmacro.h (SD_REV_MODE_ROOM et al)
ps2_hard_effect_table = {
    'room' : 1,
    'studio a' : 2,
    'studio b' : 3,
    'studio c' : 4,
    'hall' : 5,
    'space' : 6,
    'echo' : 7,
    'delay' : 8,
    'pipe' : 9,
    }

# Keep in sync with src/ps2utl/softfx_main.h
ps2_soft_effect_table = {
    'delay' : 0,
    'reverb' : 1,
    'dist' : 2
    }

###################

def enable_all_tracks ():
    for i in range(8):
        hx.track_ctrl ('enable', i)


###################

# The key is the string that identifies the cheat
# The first item in the value's list is the sequence of buttons that
#    triggers the cheat.
# The second is the python function to execute when the cheat triggers.
# The third is whether the cheat applies in the metagame or the gamesystem.
#    Permissible values are "gs" and "meta".

# May be unused at this point.
def add_powerups_to_all (pow):
    for pl in (0,1,2,3) :
        hx.add_powerup (pl, powerup_num (pow))

def cheat_activatelistenmode() :
    if community == 'solo' :
        hx.activate_listen_mode()

def cheat_activatepracticemode() :
    if community == 'solo' :
        hx.activate_practice_mode()

def cheat_activateallaccessmode() :
    hx.activate_all_access_mode()

def cheat_enableteamfreqs() :
    hx.enable_team_freqs()

# This bool keeps track of whether powerup cheats are enabled or not.
powerup_cheats_enabled = 0

# Sigh. Since we don't know which is our current screen in Python, we
# have to call hx.enable_powerup_cheats() to test whether we're on the
# logo screen and if so, it calls this function to toggle the Python variable
# powerup_cheats_enabled.
def toggle_powerup_cheats_enabled() :
    global powerup_cheats_enabled
    if powerup_cheats_enabled :
        powerup_cheats_enabled = 0
    else :
        powerup_cheats_enabled = 1

def cheat_enablepowerupcheats() :
    hx.enable_powerup_cheats()

def cheat_autocatcher() :
    global powerup_cheats_enabled
    if powerup_cheats_enabled :
        hx.add_powerup( cheater_player_num, powerup_num('aut') )
        hx.do_powerup_cheat()

def cheat_freestyle() :
    global powerup_cheats_enabled
    if powerup_cheats_enabled :
        if community == 'local' :
            hx.add_powerup( cheater_player_num, powerup_num('fre') )
            hx.do_powerup_cheat()

def cheat_multiplier() :
    global powerup_cheats_enabled
    if powerup_cheats_enabled :
        if community == 'solo' :
            hx.add_powerup( cheater_player_num, powerup_num('mul') )
            hx.do_powerup_cheat()

def cheat_neutralizer() :
    global powerup_cheats_enabled
    if powerup_cheats_enabled :
        if community == 'local' :
            hx.add_powerup( cheater_player_num, powerup_num('neu') )
            hx.do_powerup_cheat()

def cheat_crippler() :
    global powerup_cheats_enabled
    if powerup_cheats_enabled :
        if community == 'local' :
            hx.add_powerup( cheater_player_num, powerup_num('crp') )
            hx.do_powerup_cheat()

def cheat_bumper() :
    global powerup_cheats_enabled
    if powerup_cheats_enabled :
        if community == 'local' :
            hx.add_powerup( cheater_player_num, powerup_num('bum') )
            hx.do_powerup_cheat()

def cheat_winwithpoints( points ) :
    if community == 'solo' :
        hx.do_win_with_points_cheat( points )

def cheat_enablealltracks() :
    if community == 'solo' :
        hx.do_enable_all_tracks_cheat()

def cheat_arenastatecycle() :
    if community == 'solo' :
        hx.do_arena_state_cycle_cheat()

def cheat_expansionpacktoggle() :
    hx.do_expansion_pack_toggle_cheat()

newcheats = {
    "activatelistenmode":        [cheat_activatelistenmode],
    "activatepracticemode":      [cheat_activatepracticemode],
    "activateallaccessmode":     [cheat_activateallaccessmode],
    "enableteamfreqs":           [cheat_enableteamfreqs],
    "enablepowerupcheats":       [cheat_enablepowerupcheats],
    "autocatcher":               [cheat_autocatcher],
    "freestyle":                 [cheat_freestyle],
    "multiplier":                [cheat_multiplier],
    "neutralizer":               [cheat_neutralizer],
    "crippler":                  [cheat_crippler],
    "bumper":                    [cheat_bumper],
    "biggem":                    [hx.crates],
    "nolattice":                 [hx.nolattice],
    "lsdmode":                   [hx.lsdmode],
    "winwith300":                [cheat_winwithpoints, 300],
    "winwith1200":               [cheat_winwithpoints, 1200],
    "enablealltracks":           [cheat_enablealltracks],
    "arenastatecycle":           [cheat_arenastatecycle],
    "expansionpacktoggle":       [cheat_expansionpacktoggle]
}


#    "debugmode":          [cheat_debugmode],
#    "teamfreqs":          [cheat_teamfreqs], # last of legit cheats
#    "cheatwin":           [hx.cheat_win, 1], # first of dev cheats
#    "unlockstages":       [hx.cheat_unlockstages, 1],
#    "memlogterm":         [hx.memlog_term, 1]

# C++ sets this variable to the player number of the person who is doing the
# cheats. The actual cheat Python functions above use this. The player nums
# should be base-0.
cheater_player_num = -1;

def do_cheat( cheatname, playernum ) :
    global cheater_player_num
    cheater_player_num = playernum
    # Use the dictionary to look up the string name of the cheat and
    # then do the associated action.
    if newcheats.has_key( cheatname ):
        data = newcheats[cheatname]
        if len(data) == 1:
            apply (data[0], ())
        else:
            apply (data[0], data[1:])


###################

# A dictionary of button -> [cheat function, arg1, arg2, ...]
cheats = {
    JOY_UP:       [hx.clock, 'step', 10],
    JOY_DOWN:     [hx.clock, 'start'],
    JOY_X:        [hx.test_arena],
    JOY_RTHUMB:   [hx.save_rnd],
    JOY_R1:       [hx.memlog_term]
#    JOY_R1:       [hx.zone_dump, 1] # Rex, uncomment this for zone_dumps
#    JOY_START:    [hx.screen_dump, 0], # needs special build;
                                        # leave uncommented
    }

#    JOY_TRIANGLE: [hx.freeze_juice, 1],
#    JOY_SQUARE:   [enable_all_tracks],
#    JOY_SELECT:   [hx.cheat_win, 1],
#    JOY_R2:       [hx.cheat_unlockstages, 1],
# JOY_R1:       [hx.synth_cmd, 0],

def on_debug_pad_down (butt) :
    if cheats.has_key (butt):
        data = cheats[butt]
        if len(data) == 1:
            apply (data[0], ())
        else:
            apply (data[0], data[1:])

            
###############################################################################
#
# Various force feedback types and their settings...  The PS2 controller has
#  two motors, one large and one small, that can generate feedback.
#  The small motor can only be turned on or off, while the large motor can
#  be set to a variety of intensities.  So, the valid constants in the below
#  feedback settings are:
#      small motor setting -> 0 = off, 1 = on
#      large motor setting -> 0 = off, 255 = maximum vibration
#      all durations(except the metronome's) are in song ticks...

# Turn on or off force feedback from here.  1 = on, 0 = off...
def get_fb_enabled ():
    return 1

# The force feedback settings for the time-based metronome type feedback...
#  [ small motor, duration(in milliseconds), # ticks per bar ]
def get_metro_fb_info ():
    return [ 1, 70, 4 ]

# The settings for the kick drum force feedback
#  [ large motor, duration(in milliseconds) ]
def get_kick_fb_info ():
    return [ 200, 120 ]

# The force feedback settings for a player who is crippled.
#  [ small motor, large motor, duration, # of pulses ]
def get_crippled_fb_info ():
    return [ 1, 255, 1920, 1 ]

# The force feedback settings for a player who is neutralized.
#  [ small motor, large motor, duration, # of pulses ]
def get_neutralized_fb_info ():
    return [ 0, 0, 1920, 1]

# The force feedback settings for a player who deploys an autocatcher???
#  [ small motor, large motor, duration, # of pulses ]
def get_autocatch_fb_info ():
    return [ 0, 0, 120, 1 ]

# The force feedback settings for a player who gets bumped.
#  [ small motor, large motor, duration, # of pulses ]
def get_bump_fb_info ():
    return [ 1, 0, 480, 1]

# The force feedback settings for a player who has caught a powerup.
#  For now, this fires 2 quick pulses(each lasting 'duration' song ticks) 
#  [ small motor, large motor, duration, # of pulses ]
def get_caught_pow_fb_info ():
    return [ 0, 175, 240, 1 ]

###################

# You get 'points' for catching gems in various positions in a bar.
#
#                              These positions are:
points_per_period = [4,      # beat 1
                     5,      # beat 3
                     6,      # beat 2 and 4
                     7,      # off-beat eighth notes
                     8,      # sixteenth notes
                     9]      # anything else

# The score you get for a whole bar is determined by adding up all of
# the points, as above, and then looking up the total in this table:
#
#                   Points     Score
score_boundaries = [ 0,      # 1
                    16,      # 2
                    24,      # 3
                    32,      # 4
                    40,      # 5
                    48,      # 6
                    56,      # 7
                    64,      # 8
                    72,      # 9
                    80]      # 10

###################

class Level:

    def __init__ (self):
        self.file_name = None
        self.enable_all = 0

        self.jam_bg_criteria  = ('yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.game_bg_criteria = ('yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.section_boundaries = [8, 16, 24, 32]
        self.section_names =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S' ]
        self.section_instances = [0, 1, 2, 3]
        self.linked_sections = [[], [], [], [], [], [], [], []]

        # each set is for [easy, medium, hard]
        self.slop             = [80, 80, 70]
        self.catch_points     = [5, 4, 3]
        self.freestyle_points = [5, 7, 9]
        self.initial_points   = [18, 16, 12]
        self.max_points       = [20, 20, 20]

        self.game_powerups = ['aut', 'neu', 'crp', 'fre']
        
        self.jam_fx  = ['cho', 'stt', 'ech', 'gho', 'vol']

        self.fx_filt_max    = (127,  127,  127,  127,  127,  127,  127,  127)
        self.fx_filt_period = (1920, 960,  1920, 960,  1920, 960,  1920, 960)
        self.fx_stt         = (240, 0)
        self.fx_volume      = 50

        # How much to attenuate non-current tracks, on a scale of
        # 0--127, indexed by how many tracks are on (starting at 0).
        # So for [0, 20, 40], if there are two tracks that have been
        # turned on, then all non-current tracks are attenuated 40.
        self.track_attenuations = [0, 8, 16, 24, 30, 35, 38, 43]

	# for local mode
        self.loc_top_flip   = 1
        self.loc_cam_offset = -1100
        self.loc_cam_fov    = 40
        self.loc_splitscreen = 1

        # for metagame
        self.stage = 0    # means no stage
        self.order = 0

        # for force feedback [ note number,
        #                      midi channel (0 - 15),
        #                      large motor = 0(off) - 255(full power),
        #                      duration(in song ticks) ]
        #self.kick_note = [0, 0, 0, 0]    # default = no kick feedback

    # This function can be removed in a shipping release
#      def verify_linked_sections (self):
#          if len(self.linked_sections) != 8:
#              raise "linked_sections does not have 8 elements!"
#          for track in self.linked_sections:
#              used_sections = []
#              for link in track:
#                  last_section = -1
#                  size = 0
#                  for section in link:
#                      if section >= len (self.section_boundaries):
#                          raise "in linked sections, section %d does not exist!" % section
#                      if section <= last_section:
#                          raise "in linked_sections, %d comes after %d!" % (section, last_section)
#                      if section in used_sections:
#                          raise "in linked_sections, section %d occurs twice on a single track!" % section

#                      if section == 0:
#                          section_size = self.section_boundaries[0]
#                      else:
#                          section_size = self.section_boundaries[section] - \
#                                         self.section_boundaries[section-1]
#                      if size == 0:
#                          size = section_size
#                      else:
#                          if size != section_size:
#                              raise "in linked_sections, section %d is size %d, should be %d!\n" % (section, section_size, size)
                        
#                      last_section = section
#                      used_sections.append (section)

    # for metagame: 1 means yes, 0 means no
    def is_avail_game(self):    return 0
    def is_avail_jam(self):   return 0

    # allow a level to override which synth is used
    def get_synth (self):
        return get_global_synth()

    # Show diagnostic information? (track/bar/capturing percentage)
    def show_diagnostics (self):
        return 0
    
    # True if you want to see meters
    def get_show_meters (self):
        return 0
    
    # horizon: how far ahead (in bars) in the tunnel we can see data
    def get_horizon (self):
        return 5
    
    # Return how much MIDI volume to subtract for the non-current track.
    def boost_volume (self):
        return 90
    
    # Should we do wacko panning? (pan track left/right based on shuttle position)
    def wacko_panning (self):
        return 0
    
    # We can select a set of gems from a gem track (based on octave).
    # values should be 0, 1, 2
    def get_gem_difficulty (self):
        global gem_difficulty
        return gem_difficulty
    
    # 'true' if in jam mode, we should force all quantization to 16th notes.
    def get_jam_16ths (self):
        return 1
    
    # Return the number laps to go around the tunnel before the game ends.
    def get_num_laps (self):
        if self.use_linear_song_form():
            return 1
        else:
            return 3
        
    # number of tracks in a level (keep this at 8)
    def get_num_tracks (self): return 8

    # Numbered from 1 to 8
    def get_starting_track (self): return 1

    # Return the control-change number used for the Axe FX axis.
    def get_axe_fx_ctrl (self): return 1
    
    # Return the length of the intro in units of ticks.
    def get_intro_length (self): return 4 * 1920
    
    # Return whether a given catching track is "early" (the whole song
    # turns on once you capture any of it).
    def is_early_track (self, track): return 0
    
    # Track enablement criteria. Enable a track based on other tracks
    # being owned or not.
    def get_track_enablement_criteria (self, track):
        if self.enable_all:
            return []
        if ruleset == 'jam':
            return []
        if ruleset == 'game':
            return massage_criteria (self.track_enable_criteria[track-1])
        raise 'Bad ruleset: %s' % `ruleset`

    def get_backing_track_criteria (self, track):
        global ruleset
        if (ruleset == 'game'):
            return massage_criteria (self.game_bg_criteria[track-1])
        else:
            return massage_criteria (self.jam_bg_criteria[track-1])
        
    def get_linked_sections (self, track):
#        if track == 0:
#            self.verify_linked_sections() # only do this once
        return self.linked_sections[track]

    # How far off you can be from a gem and still catch it, in milliseconds
    # The old value was around 60 for a 120bpm song
    def get_slop (self):
        return self.slop[self.get_gem_difficulty()]
     
    # How many bars to credit the player with when he catches a phrase?
    def get_catch_points (self):
        return self.catch_points[self.get_gem_difficulty()]

    # How many points does the player get per freestyle bar?
    def get_freestyle_points (self):
        return self.freestyle_points[self.get_gem_difficulty()]
    
    # How many bars credit does the player start with?
    def get_initial_points (self):
        return self.initial_points[self.get_gem_difficulty()]
    
    # How many bars does the juice meter cap at?
    def get_max_points (self):
        return self.max_points[self.get_gem_difficulty()]

    # how many bars does the autocatcher catch?
    def get_autocatch_bars (self):
        return 4
    
    # how many bars does the neutralizer neutralize
    def get_neutralize_bars (self):
        return 4
    
    # which powerups to display in the mfd overlay:
    def get_mfd_powerups (self):
        if ruleset == 'game':
            return map (powerup_num, self.game_powerups)
        elif ruleset == 'jam':
            return map (powerup_num, self.jam_fx)
    
    # where sections go in the song. Last section is also the song length
    def get_section_boundaries (self):
        return self.section_boundaries
    
    def use_linear_song_form (self):
        return 0

    def use_bank_swapping (self):
        return 0

    def get_section_instances (self):
        return self.section_instances * self.get_num_laps()

    def get_bitmap (self):
        return get_absolute_path ("levels/%s/%s.bmp" % (self.directory_name, self.directory_name))
    
    def ruleset_suffix (self):
        suffix = 'F1'
        # if it's a game an remix_playback, read from pitching file
        if ruleset == 'game' and remix_playback == 0:
            suffix += '_c'
        else:
            suffix += '_p'
        return suffix
        
    def get_seermusic_bank (self):
        return get_absolute_path ("levels/%s/%s.seermusic" %
                                  (self.directory_name, self.directory_name))

    def get_seermusic_bank_by_ruleset (self):
        return get_absolute_path ("levels/%s/%s%s.seermusic" %
                                  (self.directory_name, self.directory_name,
                                   self.ruleset_suffix()))

    ### PS2 hardware synth
    #

    def bank_suffix_of_first_section_instance (self, swapping):
        if swapping:
            suffix = "_%d" % (self.section_instances[0] + 1)
        else:
            suffix = ""
        return suffix

    def get_ps2_hard_bank (self, swapping, cd=0):
        suffix = self.bank_suffix_of_first_section_instance (swapping)
        return get_absolute_path ("levels/%s/%s%s.bd" %
                                  (self.directory_name, self.directory_name, suffix))

    def get_ps2_hard_bank_header (self, swapping, cd=0):
        suffix = self.bank_suffix_of_first_section_instance (swapping)
        return get_absolute_path ("levels/%s/%s%s.hd" %
                                  (self.directory_name, self.directory_name, suffix))

    def get_soundbank_movie (self):
        return get_absolute_path ("levels/%s/%s.mmv" %
                                  (self.directory_name, self.directory_name))
    
    # Note that these all take a 'core' argument which can be 0 or 1

    def ps2_use_hard_effect (self, core):
        return 0

    def ps2_hard_effect_name (self, core):
        return 'delay'

    def ps2_hard_effect_volumes (self, core):
        return [1.0, 1.0]               # [left, right]

    def ps2_hard_delay_time (self, core):
        return 127

    def ps2_hard_feedback (self, core):
        return 127

    # Helper function, don't override this one
    def ps2_hard_effect_id (self, core):
        return ps2_hard_effect_table[self.ps2_hard_effect_name (core)]

    # Hardware synth "effects"
    # which midi channels dont pause when you pause the game
    def ps2_heff_nopause_channels(self):
        return 0x8000

    # in ms, for L and R
    def ps2_heff_chorus_rate(self):
        return [200,300]

    # in 128th of a step for L and R
    # [?? should we switch this to cents ??]
    def ps2_heff_chorus_depth(self):
        return [40, 30]

    # currently ignored, but might be waveform shape
    def ps2_heff_chorus_shape(self):
        return [0, 0]

    # config for the stutter... step size, algorithim, cutoff to try HW smooth
    def ps2_heff_stt(self):    
        return [0x400, 6, 0x1800, 0]
    # dc local - [0x100, 3, 0x800, 0]

    def ps2_hsyn_error_file(self):
        return ""
    # use this if you want error reporting for this level
      # return "%s.her"%self.directory_name

    ###

    def get_midi_file (self):
        return get_absolute_path ("levels/%s/%s%s.mid" %
                                  (self.directory_name, self.directory_name,
                                   self.ruleset_suffix()))

    def get_version (self, irule):
        global ruleset
        tmp = ruleset
        ruleset = irule
        v = str (os.path.getsize (self.get_midi_file ()))
        v = v + str (os.path.getsize (self.file_name))
        ruleset = tmp
        return v

    def mode_supported (self, community, ruleset):
        return 1

    def on_key_down(self, key):
        pass

    def get_is_tutorial (self):
        return 0

    #def get_kick_note (self):
    #    return self.kick_note
    
    #***********************************************************************
    # lvl::on_ handlers: let python get a chance to do stuff when msgs are sent to the
    # tunnel
   
   
    # game begin:
    def on_game_begin (self):
        pass
        
    # game over:
    def on_game_over (self):
        pass
    
    # called repeatedly for each section boundary at startup
    def on_section (self, tick):
        pass
    
    # called when the user rotates to a new track
    def on_track_select (self, track):
        pass
    
    # called when axe juice changes
    def on_juice_amount (self, amount, can_axe):
        pass
    
    # user caught a gem successfully
    def on_hit (self):
        pass
    
    # user missed while attempting to catch a gem
    def on_miss (self):
        pass
    
    # a gem passed by. Player did not attempt to catch at all
    def on_pass (self):
        pass
    
    # user pitched in remix mode/or on an axe track
    def on_pitch (self):
        pass
    
    # user tried to catch on an inactive track
    def on_invalid_pitch (self):
        pass
    
    # user successfully caught a phrase
    def on_phrase_capture (self, track):
        pass
    
    # user failed to capture a phrase because...
    def on_score_too_low (self, track):
        pass
    
    def on_error_too_high (self, track):
        pass
    
    def on_toggle_loop (self):
        pass

    def on_erase (self):
        pass
    
    def on_advance_section (self):
        pass
    
    def on_axe_stick (self):
        pass

    def on_axe_button (self):
        pass

    def on_choose_powerup (self, powerup):
        pass

    def on_jam_effect (self):
        pass

    def on_toggle_ghosts (self):
        pass

    def make_current (self):
        global current_level
        current_level = self

#########################################
# default arena:

class Arena:

    def __init__ (self):
        pass

    def on_key_down(self, key):
        pass

    def on_game_begin (self):
        pass
        
    def on_game_over (self):
        pass
    
    def on_section (self, tick):
        pass
    
    def on_track_select (self, track):
        pass
    
    def on_juice_amount (self, amount, can_axe):
        pass
    
    def on_hit (self):
        pass
    
    def on_miss (self):
        pass
    
    def on_pass (self):
        pass
    
    def on_pitch (self):
        pass
    
    def on_phrase_capture (self, track):
        pass
    
    def on_toggle_loop (self):
        pass
    
    def on_erase (self):
        pass

    def available_in (self, community):
        if (community == 'local'):
            return 0
        else:
            return 1

    def make_current (self):
        global current_arena
        current_arena = self


##############################################
# Initialization stuff


#try autoexec.py in cwd. Otherwise, try in absolute path (with root)
if (not exec_if_exists ('autoexec.py')):
    exec_if_exists (get_absolute_path ('autoexec.py'))

init_new_album ()                        # Load new levels, arenas, etc...

#load_localusers()                       # Initialize localusers

global_execfile (get_absolute_path ('metagame/met_strings.py'))
