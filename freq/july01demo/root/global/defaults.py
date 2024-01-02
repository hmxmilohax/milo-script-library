
##############################################################################
#
# Copyright 2000 Harmonix Music Systems.  All rights reserved.
#
# $Header: j:\\cvs/Freq/run/Global/defaults.py,v 1.80.2.5 2001/06/28 15:35:04 christine Exp $
#
##############################################################################

import glob
import new
import os
import os.path
import types
import pickle
import shutil
from types import *

level_list = {}                         # dict: level name -> instance
arena_list = {}                         # dict: arena name -> instance
current_level = None                    # An instance of the current level
current_arena = None                    # An instance of the current arena

# Call when leaving a level
def reset_current_level ():
    current_level = None
    current_arena = None
    
def current_level_exists ():
    return (current_level != None)

# script_cache is used to spoof "global_execfile". When we play back a
# recording, we can sneak in a recorded file (ie, a string) instead of the file
# itself. Make sure we do not wipe away script_cache in a reload

if (not globals().has_key ('script_cache')):
    script_cache = {}

def clear_script_cache ():
    global script_cache
    script_cache = {}

def set_autoexec (str):
    global script_cache
    script_cache['autoexec.py'] = str

def get_autoexec ():
    f = open (get_absolute_path ('autoexec.py'))
    str = f.read()
    return str

# Use this instead of execfile to ensure that stuff goes into the global
# namespace. Also, use it to exec "files" that have actually been cached as
# strings when we play back a recording

def global_execfile (f) :
    name = os.path.basename (f)
    if script_cache.has_key (name):
        exec (script_cache[name], globals())
    else:
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

# Return a list of all the level scripts in the FreQ root directory.
#
def get_level_scripts ():
    return map (full_level_path,  ['Tutorial',
                                   'demo_dpist',
                                   'demo_winner'])

def full_arena_path (name):
    return os.path.join (root, get_script (name, 'arenas'))

# Return a list of all the arena scripts in the FreQ root directory.
def get_arena_scripts ():
    return map (full_arena_path,  ['blue', 'const'])


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
    for script in get_level_scripts():
        global_execfile (script)
        inst = make_level (get_class_name(), script)
        level_list[inst.directory_name] = inst

def load_arena_scripts ():
    for script in get_arena_scripts():
        global_execfile (script)
        inst = get_arena_class_name() ()
        arena_list[inst.directory_name] = inst
    

## Does a level with the given name and the given suffix exist?

#def level_exists (name, suffix):
#    return os.path.exists (get_script_with_suffix (name, suffix, 'levels'))

## Return a string-list of levels
#
def get_levels ():
    names = map (lambda x: x.directory_name, level_list.values())
    names.sort()
    return names

## Return a string-list of arenas
#
def get_arenas ():
    names = map (lambda x: x.directory_name, arena_list.values())
    names.sort()
    return names


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

# List of recording files to play back in attract mode
recording_files = ['TD_dubpistols.bin', 'TD_winner.bin']
#recording_files = ['rec.bin']

which_recording = -1
def choose_random_recording ():
    global which_recording
    which_recording += 1
    if which_recording >= len(recording_files):
        which_recording -= len(recording_files)
    return recording_files[which_recording]

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
def get_screen_config ():
    return (800, 600, 16, 60)


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

def config_input ():
    hx.input ('add', 0, 'rotR', None, 'joy', 1, JOY_RIGHT)
    hx.input ('add', 0, 'rotL', None, 'joy', 1, JOY_LEFT)
    hx.input ('add', 0, 'advn', None, 'joy', 1, JOY_UP)
    hx.input ('add', 0, 'loop', None, 'joy', 1, JOY_DOWN)
    hx.input ('add', 0, 'rpch',    0, 'joy', 1, JOY_SQUARE)
    hx.input ('add', 0, 'rpch',    0, 'joy', 1, JOY_L1)
    hx.input ('add', 0, 'rpch',    1, 'joy', 1, JOY_TRIANGLE)
    hx.input ('add', 0, 'rpch',    1, 'joy', 1, JOY_R1)
    hx.input ('add', 0, 'rpch',    2, 'joy', 1, JOY_CIRCLE)
    hx.input ('add', 0, 'rpch',    2, 'joy', 1, JOY_R2)
    hx.input ('add', 0, 'rpch',    0, 'joy', 1, JOY_LTHUMB)
    hx.input ('add', 0, 'eras', None, 'joy', 1, JOY_X)
    hx.input ('add', 0, 'regi', None, 'joy', 1, 100)
    hx.input ('add', 0, 'axfx', None, 'joy', 1, 101)
    hx.input ('add', 0, 'powx', None, 'joy', 1, 102)
    hx.input ('add', 0, 'powy', None, 'joy', 1, 103)
    hx.input ('add', 0, 'powb', None, 'joy', 1, JOY_RTHUMB)
    hx.input ('add', 0, 'pbck', None, 'joy', 1, JOY_SELECT)


    hx.input ('add', 1, 'rotR', None, 'joy', 2, 14)
    hx.input ('add', 1, 'rotL', None, 'joy', 2, 16)
    hx.input ('add', 1, 'advn', None, 'joy', 2, 13)
    hx.input ('add', 1, 'loop', None, 'joy', 2, 15)
    hx.input ('add', 1, 'rpch',    0, 'joy', 2, 4)
    hx.input ('add', 1, 'rpch',    0, 'joy', 2, 7)
    hx.input ('add', 1, 'rpch',    1, 'joy', 2, 1)
    hx.input ('add', 1, 'rpch',    1, 'joy', 2, 8)
    hx.input ('add', 1, 'rpch',    2, 'joy', 2, 2)
    hx.input ('add', 1, 'rpch',    2, 'joy', 2, 6)
    hx.input ('add', 1, 'rpch',    0, 'joy', 2, 12)
    hx.input ('add', 1, 'eras', None, 'joy', 2, 3)
    hx.input ('add', 1, 'regi', None, 'joy', 2, 100)
    hx.input ('add', 1, 'axfx', None, 'joy', 2, 101)
    hx.input ('add', 1, 'powx', None, 'joy', 2, 102)
    hx.input ('add', 1, 'powy', None, 'joy', 2, 103)
    hx.input ('add', 1, 'powb', None, 'joy', 2, 11)
    hx.input ('add', 1, 'rotL', None, 'key', 1, 37)
    hx.input ('add', 1, 'rotR', None, 'key', 1, 39)
    hx.input ('add', 1, 'rpch',    0, 'key', 1, 49)
    hx.input ('add', 1, 'rpch',    1, 'key', 1, 50)
    hx.input ('add', 1, 'rpch',    2, 'key', 1, 51)
    hx.input ('add', 1, 'eras', None, 'key', 1, 52)


    hx.input ('add', 2, 'rotR', None, 'joy', 3, 14)
    hx.input ('add', 2, 'rotL', None, 'joy', 3, 16)
    hx.input ('add', 2, 'advn', None, 'joy', 3, 13)
    hx.input ('add', 2, 'loop', None, 'joy', 3, 15)
    hx.input ('add', 2, 'rpch',    0, 'joy', 3, 4)
    hx.input ('add', 2, 'rpch',    0, 'joy', 3, 7)
    hx.input ('add', 2, 'rpch',    1, 'joy', 3, 1)
    hx.input ('add', 2, 'rpch',    1, 'joy', 3, 8)
    hx.input ('add', 2, 'rpch',    2, 'joy', 3, 2)
    hx.input ('add', 2, 'rpch',    2, 'joy', 3, 6)
    hx.input ('add', 2, 'rpch',    0, 'joy', 3, 12)
    hx.input ('add', 2, 'eras', None, 'joy', 3, 3)
    hx.input ('add', 2, 'regi', None, 'joy', 3, 100)
    hx.input ('add', 2, 'axfx', None, 'joy', 3, 101)
    hx.input ('add', 2, 'powx', None, 'joy', 3, 102)
    hx.input ('add', 2, 'powy', None, 'joy', 3, 103)
    hx.input ('add', 2, 'powb', None, 'joy', 3, 11)


    hx.input ('add', 3, 'rotR', None, 'joy', 4, 14)
    hx.input ('add', 3, 'rotL', None, 'joy', 4, 16)
    hx.input ('add', 3, 'advn', None, 'joy', 4, 13)
    hx.input ('add', 3, 'loop', None, 'joy', 4, 15)
    hx.input ('add', 3, 'rpch',    0, 'joy', 4, 4)
    hx.input ('add', 3, 'rpch',    0, 'joy', 4, 7)
    hx.input ('add', 3, 'rpch',    1, 'joy', 4, 1)
    hx.input ('add', 3, 'rpch',    1, 'joy', 4, 8)
    hx.input ('add', 3, 'rpch',    2, 'joy', 4, 2)
    hx.input ('add', 3, 'rpch',    2, 'joy', 4, 6)
    hx.input ('add', 3, 'rpch',    0, 'joy', 4, 12)
    hx.input ('add', 3, 'eras', None, 'joy', 4, 3)
    hx.input ('add', 3, 'regi', None, 'joy', 4, 100)
    hx.input ('add', 3, 'axfx', None, 'joy', 4, 101)
    hx.input ('add', 3, 'powx', None, 'joy', 4, 102)
    hx.input ('add', 3, 'powy', None, 'joy', 4, 103)
    hx.input ('add', 3, 'powb', None, 'joy', 4, 11)

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

# Sets the community-type for this level: solo, local, net
def set_community (name):
    global community
    community = name
   
# Sets the ruleset for this level: game, jam
def set_ruleset (name):
    global ruleset
    ruleset = name

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
        apply (getattr (current_level, func), args)
        apply (getattr (current_arena, func), args)

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
powerup_names = { 'neu':0, 'crp':1, 'fre':2, 'aut':3, 'bum':4,
                  'vol':5, 'wah':6, 'stt':7, 'ech':8,
                  'flg':9, 'cho':10 }

def powerup_num (name):
    try:
        return powerup_names[name]
    except KeyError:
        raise KeyError ('Not a valid powerup name:%s' % name)

def get_ps2_metagame_hard_bank (cd=0):
   return get_absolute_path ("MetaGame/Sounds/sfx_meta_bank.bd")

def get_ps2_metagame_hard_bank_header (cd=0):
   return get_absolute_path ("MetaGame/Sounds/sfx_meta_bank.hd")

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

###################

def enable_all_tracks ():
    for i in range(8):
        hx.track_ctrl ('enable', i)

# A dictionary of button -> [cheat function, arg1, arg2, ...]
cheats = {
    JOY_TRIANGLE: [hx.freeze_juice, 1],
    JOY_SQUARE:   [enable_all_tracks],
    JOY_CIRCLE:   [hx.juice_meter, 1],
    JOY_X:        [hx.juice_meter, 0],
    JOY_SELECT:   [hx.cheat_win, 1],
    JOY_START:    [hx.screen_dump, 0],
    JOY_R2:       [hx.memlog_term],
    JOY_R1:       [hx.zone_dump,1],
    }

def on_debug_pad_down (butt) :
    pass
    if cheats.has_key (butt):
        data = cheats[butt]
        if len(data) == 1:
            apply (data[0], ())
        else:
            apply (data[0], data[1:])

###################

class Level:

    def __init__ (self):
        self.file_name = None
        self.short_name = None          # used for .hd and .bd files
        self.enable_all = 0

        self.jam_bg_criteria  = ('yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.game_bg_criteria = ('yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.section_boundaries = [8, 16, 24, 32]
        self.section_names =  ['section1', 'section2', 'section3', 'section4', 'section5',
                               'section6', 'section7', 'section8', 'section9', 'section10']
        self.section_instances = [0, 0, 1, 2]

        # each set is for [easy, medium, hard]
        self.slop             = [100, 90, 80]
        self.catch_points     = [5, 4, 3]
        self.freestyle_points = [5, 7, 9]
        self.initial_points   = [20, 16, 12]
        self.max_points       = [20, 20, 20]

        # based on # of players playing (1->4):
        self.num_laps         = [3, 4, 3, 3]  
        
        self.game_powerups = ['aut', 'neu', 'crp', 'fre']
        self.powerbar_table = [
            ['aut', 'aut', 'aut', 'aut', 'aut', 'aut', 'aut', 'aut'],
            ['crp', 'crp', 'crp', 'crp', 'crp', 'crp', 'crp', 'crp'],
            ['aut', 'aut', 'aut', 'aut', 'aut', 'aut', 'aut', 'aut'],
            ['neu', 'neu', 'neu', 'neu', 'neu', 'neu', 'neu', 'neu']
            ]
        
        self.jam_fx  = ['wah', 'stt', 'ech', 'vol']

        self.fx_filt_max    = (127,  127,  127,  127,  127,  127,  127,  127)
        self.fx_filt_period = (1920, 960,  1920, 960,  1920, 960,  1920, 960)
        self.fx_stt         = (240, 0)
        self.fx_volume      = 50

        # How much to attenuate non-current tracks, on a scale of
        # 0--127, indexed by how many tracks are on (starting at 0).
        # So for [0, 20, 40], if there are two tracks that have been
        # turned on, then all non-current tracks are attenuated 40.
        self.track_attenuations = [0, 8, 16, 24, 32, 40, 48, 56]

	# for local mode
        self.loc_top_flip   = 1
        self.loc_cam_offset = -1100
        self.loc_cam_fov    = 40
        self.loc_splitscreen = 1

    # for metagame
        self.stage_num = 0    # means no stage

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
        return 6
    
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
        return self.num_laps[num_players-1]
        
    # number of tracks in a level (keep this at 8)
    def get_num_tracks (self): return 8

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
    
    # find the powerbar for a given track section
    def get_powerbar (self, track, section):
        if section >= len(self.powerbar_table):
            section %= len(self.powerbar_table)
        return powerup_num (self.powerbar_table[section][track])

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

    def get_section_instances (self):
        return self.section_instances

    def get_bitmap (self):
        return get_absolute_path ("levels/%s/%s.bmp" % (self.directory_name, self.directory_name))
    
    def ruleset_suffix (self):
        suffix = 'F1'
        if ruleset == 'game':
            suffix += '_c'
        elif ruleset == 'jam':
            suffix += '_p'
        else:
            raise 'Bad ruleset: %s' % ruleset
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

    def get_ps2_hard_bank (self, cd=0):
      return get_absolute_path ("levels/%s/%s.bd" %
                                      (self.directory_name, self.short_name))

    def get_ps2_hard_bank_header (self, cd=0):
      return get_absolute_path ("levels/%s/%s.hd" %
                                      (self.directory_name, self.short_name))

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

    #
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
    
    #***********************************************************************
    # lvl::on_ handlers: let python get a chance to do stuff when msgs are sent to the
    # tunnel
   
   
    # game begin:
    def on_game_begin (self):
        pass
#       hx.toggle_cursor()
#       hx.toggle_nowbar()
#       hx.show_sections()
        
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

    def on_choose_powerup (self):
        pass

    def on_deploy_powerup (self):
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
    
    def on_invalid_pitch (self):
        pass
    
    def on_phrase_capture (self, track):
        pass
    
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
    
    def on_choose_powerup (self):
        pass

    def on_deploy_powerup (self):
        pass

    def advancesection (self, adv):
        pass
    
    def willadvancesection (self, adv):
        pass

    def effects_off (self, track):
        pass

    def set_effect(self, track, ieffect, onoff):
        pass

    def make_current (self):
        global current_arena
        current_arena = self





#    def load_rnd_data (self):
#        global_execfile (get_arena_script (self.get_arena_name()))
#        self.arena = get_arena_class_name () ()

#    def set_arena_name (self, name):
#        self.arenaName = name

#    def get_arena_name (self):
#        global ruleset
#        return self.arenaName
#        if (ruleset == 'jam'):
#            return "videowall"
#        else:
#            return self.arenaName
    


##############################################
# Initialization stuff


#try autoexec.py in cwd. Otherwise, try in absolute path (with root)
if (not exec_if_exists ('autoexec.py')):
    exec_if_exists (get_absolute_path ('autoexec.py'))
    
load_level_scripts ()   # Initialize level_list
load_arena_scripts ()   # Initialize arena_list

#load_localusers()                       # Initialize localusers

global_execfile (get_absolute_path ('metagame/met_strings.py'))

global_execfile (get_absolute_path ('metagame/persona/pers_dat.py'))

