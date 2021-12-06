#
# met_strings.py
#
# This file contains all strings used in the Meta Game.
#
# This includes: button text, label text
#				
# This does NOT include: level-specific text (title, composer, etc.)
# 			 character specific text
#


############################################
### THESE ARE TEXTS FOR BUTTONS
############################################
gMetStrings = {

# pause screen
   'pause_game'      : 'Game Paused',
   'pause_remix'     : 'Remix Paused',
   'pause_tutorial'  : 'Tutorial Paused',

   'pause_on'     : 'ON',
   'pause_off'    : 'OFF',

# loading screen
   'load_loading' : 'LOADING',
   'load_game'    : 'GAME',
   'load_remix'   : 'REMIX',
   'load_tut'     : 'TUTORIAL',
   'load_demo'    : 'DEMO',

# load pre-fab
   'pf_edit' : 'EDIT ',
   'pf_create' : 'FREQMAKER',

# load new
   'nf_enter'  : 'ENTER NAME',
   'nf_edit'   : 'MODIFY BASIC FREQ',
   'nf_create' : 'FREQMAKER',

# load from memory card
   'lf_edit'   : 'EDIT ',
   'lf_create' : 'CREATE NEW FREQ',

# create freq
   'create_from_prefab'  : 'MODIFY BASIC FREQ',
   'create_from_scratch' : 'FREQMAKER',

# freqmaker
	 'fqmak_randomize'   : 'RANDOMIZE',
	 'fqmak_body'			: 'BODY',
	 'fqmak_head'			: 'HEAD',
	 'fqmak_face'			: 'FACE',
	 'fqmak_details'		: 'DETAILS',
	 'fqmak_logos'			: 'LOGOS',
	 'fqmak_edit'			: 'EDIT',
	 'fqmak_name'			: 'NAME',
	 'fqmak_save'			: 'SAVE',


# config options buttons
	 'nob_game_setup'       : 'GAME SETTINGS',
	 'nob_controller_setup' : 'CONTROLLER',
	 'nob_mem_card_setup'   : 'MEMORY CARD',
	 'nob_disk_change'		: 'DISC CHANGE',
	 'nob_credits'			: 'CREDITS',
    'config_controller_player' : 'PLAYER',
    'config_controller_setup'  : 'SETUP',


# config controller buttons
	 'controller_config_left_note_1'    : 'Left Note',
	 'controller_config_left_note_2'    : 'Left Note',
	 'controller_config_center_note_1'  : 'Center Note',
	 'controller_config_center_note_2'  : 'Center Note',
	 'controller_config_right_note_1'   : 'Right Note',
	 'controller_config_right_note_2'   : 'Right Note',
	 'controller_config_erase_and_power'    : '    Erase & Powerup',
	 'controller_config_expression' : 'Expression',
     'controller_config_remix_fx'   : 'Remix Fx',

     'controller_config_instruct1'  : 'set control for selected action',
     'controller_config_instruct2'  : 'restore default configuration',  

#game prefs...
     'pangame_audio' :   'Mono / Stereo',
     'pangame_beat_assist'  : 'Optical Out ',
     'pangame_force_feedback'   :   'Force Feedback',

     'pangame_audio_lbl'   : 'AUDIO',
     'pangame_force_lbl'   : 'VIBRATION FUNCTION',
     'pangame_beat_lbl'    : 'OPTICAL OUT',

# expansion pak

   'expansion_prepare' : 'Opening CD tray for disk exchange.  Do not restart your PlayStation® 2 or remove your current Frequency disc.',
   'expansion_check' : 'Please remove the current FreQuency™ disc.  Insert a new FreQuency™ Disc and press Continue.  Do not restart your PlayStation® 2 or close the CD tray.',
   'expansion_retry' : 'Attempt to load Disc failed.  Please remove the current FreQuency™ Disc.  Insert a new FreQuency™ Disc and press Retry or insert the previous Frequency Disc press Cancel.  Do not restart your PlayStation® 2.',
   'expansion_load'  : 'Loading data from FreQuency™ Disc.',
   'expansion_cancel' : 'Reloading from current FreQuency™ Disc.  Do not restart your PlayStation® 2.',
   'expansion_done1'  : 'FreQuency™ Disc',
   'expansion_done2'  : 'has been loaded.',

# persona create new Freq

   'p_username'   : 'user name',
   'p_custID'     : 'customize FreQ',
   'p_info'       : 'personal info',
   'p_viewp'      : 'view profile',
   'p_save'       : 'accept',
   'p_del'        : 'delete',

   'cid_save'     : 'SAVE',
   'cid_accept'   : 'ACCEPT',

   'cid_edit'     : 'EDIT',
	'cid_custom'   : 'CUSTOM',

# persona customize id

   'pc_random'    : 'randomize',
   'pc_avatar'    : 'avatar',
   'pc_head1'     : 'head 1',
   'pc_head2'     : 'head 2',
   'pc_logo'      : 'logo',
   'pc_color'     : 'adjust colors',
   'pc_ok'        : 'ok',
   
# persona personal info

   'pp_title'     : 'info',
   'pp_email'     : 'email',
   'pp_music'     : 'music',
   'pp_info'      : 'info',
   'pp_ok'        : 'ok',

# main
   
   'tut'       : 'TUTORIALS',
   'solo'      : 'SOLO',
   'multi'     : 'MULTI',
   'opt'       : 'OPTIONS',

# tutorial

   'tut_g'     : 'GAME MODE',
   'tut_r'     : 'REMIX MODE',

# mode

   'ms_game'   : 'GAME',
   'ms_jam'    : 'REMIX',

# remix type

   'ms_newjam' : 'NEW REMIX',
   'ms_loadjam': 'LOAD REMIX',
   'ms_jukebox': 'JUKEBOX',
   
# skill

   'ms_easy'   : 'EASY',
   'ms_normal' : 'NORMAL',
   'ms_expert' : 'EXPERT',

# local mode num players
   
   'loc_2p'    : '2 PLAYERS',
   'loc_3p'    : '3 PLAYERS',
   'loc_4p'    : '4 PLAYERS',
   'multi_tips' : 'MULTI TIPS',

# multiplayer tips
   'tp_panel'        : 'TIPS',
   'tp_activator1'   : 'PLAYER 1 ACTIVATOR',
   'tp_activator2'   : 'PLAYER 2 ACTIVATOR',

   'tp_score1'       : 'PLAYER 1 SCORE',
   'tp_score2'       : 'PLAYER 2 SCORE',

   'tp1_title'       :  'HOW TO PLAY MULTIPLAYER:',
   'tp1_help'        :  'In multiplayer mode, you catch one bar of notes at a time instead of two.  Whoever gets the most points wins!',

   'tp2_title_1'      : 'SCORING:',
   'tp2_help_1'       : '                                      More complex note patterns will give you more points.  Look for harder patterns to beef up your score.',
   'tp2_title_2'      : 'HOT STREAK BONUS:',
   'tp2_help_2'       : '                                                                                Catch multiple bars in a row for an added bonus!',

   'tp3_panel'        : 'POWERUPS',
   'tp3_notes'        : 'POWERUP NOTES',
   'tp3_inventory'    : 'INVENTORY',
   'tp3_title_1'      : 'HOW TO CATCH POWERUPS:',
   'tp3_help_1'       : 'Capture all of the special powerup notes in a bar to add a powerup to your inventory.',
   'tp3_title_2'      : 'HOW TO USE POWERUPS:',
   'tp3_help_2'       : 'Press X to deploy a powerup on your opponents\' activator or on a specific bar of notes.',

   'tp4_hud_label'    : 'HUD',
   'tp4_note_label'   : 'NOTE',
   'tp4_desc_label'   : 'POWERUP DESCRIPTION',
   'tp4_title_1'      : 'AUTOCATCHER:',
   'tp4_help_1'       : '                                                              Deploy on free notes to catch them automatically.',
   'tp4_title_2'      : 'FREESTYLER:',
   'tp4_help_2'       : '                                                       Deploy on an Axe track or Scratch track, then freestyle on that track to get more points.',
   'tp4_title_3'      : 'CRIPPLER:',
   'tp4_help_3'       : '                                           Deploy on another player\'s activator and watch the sparks fly.',
   'tp4_title_4'      : 'NEUTRALIZER:',
   'tp4_help_4'       : '                                                          Deploy on your opponent\'s captured track to steal their points and free up that track.',
   'tp4_title_5'      : 'BUMPER:',
   'tp4_help_5'       : '                                    Deploy on another player\'s activator to bump them to the back of the line.',

   'tp5_panel'        : 'PLAYER COLORS',
   'tp5_title'       :  'PLAYER COLORS:',
   'tp5_help'        :  'Each player\'s activator, notes, panels, name and score are color-coded.',



# stage select

   'stage1'    : 'STAGE 1',
   'stage2'    : 'STAGE 2',
   'stage3'    : 'STAGE 3',
   'stage4'    : 'STAGE 4',
   'stage5'    : 'STAGE 5',
   'exit'      : 'EXIT',
   'stage'     : 'STAGE',
   'ss_custom' : 'CUSTOM',
   'stage_score' : 'Stage Score : ',
   'stage_beat'  : 'Try to Beat : ',
   'bonus_msg1'  : 'Get Stage Score of ',
   'bonus_msg2'  : ' to unlock bonus song.',

   'stage4easywarn' : 'AVAILABLE IN NORMAL AND EXPERT MODE',
   'stage5easywarn' : 'AVAILABLE IN EXPERT MODE ONLY',
   'custom_warning' : 'PRESS X TO LOAD CUSTOM REMIXES AS GAME SONGS',

# arena select
   'arena1' : 'ARENA 1',
   'arena2' : 'ARENA 2',
   'arena3' : 'ARENA 3',
   'arena4' : 'ARENA 4',
   'arena5' : 'ARENA 5',
   'arena6' : 'ARENA 6',
   'arena7' : 'ARENA 7',
   'arena8' : 'ARENA 8',
   'arena_none' : 'NO ARENA',

# stage_finish
   'stf_complete1'        : 'You\'ve unlocked the',
   'stf_arena'            : 'arena',
   'stf_completeX'        : 'You\'ve unlocked stage',
   'stf_complete_lev'     : 'You\'ve beat the game at',
   'stf_keep_try_secret'  : 'Beat all the Bonus songs to unlock the Secret Song!',
   'stf_try_lev'          : 'Would you like to try the game at',
   'stf_stage_score_beat' : 'You beat the stage score!  The Bonus Song is now unlocked.',
   'stf_try_secret'       : 'You beat all the bonus songs! The Secret song is now unlocked.', 
   

# end of game solo stats

   'egs_panel_label' : 'PLAYER STATS',
   'egs_score_label' : 'SCORE:',
   'egs_song_label' : 'SONG:',
   'egs_skill_label' : 'SKILL:',
   'egs_complete1_label' : '% of song',
   'egs_complete2_label' : 'complete:',
   'egs_phrase1_label' : 'phrase capture',
   'egs_phrase2_label' : 'accuracy:',
   'egs_hottest_label' : 'hottest streak:',
   'egs_perfect'       : 'PERFECT!',

# save remix panel title
   'remix_player'     : 'PLAYER',

# end of remix stats
   'remix_panel_label'  : 'REMIX DATA',

# end of multi remix save
   'multi_save_remix_label' : 'REMIX PLAYERS',
   'multi_save_instruct'    : 'Would you like to save?',

# end of multi session
   'egm_game_label'           : 'GAME DATA',
   'egm_remix_label'          : 'REMIX DATA',
   'egm_game_player_label'    : 'SCORES',
   'egm_remix_player_label'   : 'PLAYERS',

# end of game solo lose buttons
   'egsl_again'   : 'PLAY AGAIN',
   'egsl_levels'  : 'EXIT',

# end of game solo win buttons
   'egsw_continue' : 'CONTINUE',
   'egsw_exit'     : 'QUIT',
   'egsw_restart'  : 'PLAY AGAIN',

   'egsr_continue' : 'CONTINUE',


# end of game multi buttons
   'egmg_again'    : 'PLAY AGAIN',
   'egmg_new'      : 'NEW GAME',

   'egmr_continue' : 'CONTINUE',
   'egng_continue' : 'CONTINUE',

# stage finish
   'stf_continue'  : 'CONTINUE',
   'stf_exit'      : 'EXIT',

# memory card
   'mcrf_remix'      : 'REMIXES',
   'mcrf_freq'       : 'FREQS',
   'mem_card_select' : 'SELECT',
   'mc_sel_none'     : 'no memory cards are available',
   'mc_sel_card'     : 'select memory card slot number',


#############################################
# DIALOG MSGS
#############################################

# memory card
  'mem_detect'      : 'Checking for memory card (8MB) (for PlayStation® 2) in MEMORY CARD slot 1. Do not remove your memory card.',
  'mem_load'        : 'Loading data from memory card (8MB) (for PlayStation® 2) in MEMORY CARD slot 1. Do not remove.',
  'mem_check'      : 'FreQuency™ requires a memory card (8MB) (for PlayStation® 2) with at least 256 kb free to save game progress and configuration information.  You may proceed but will lose all information when system is powered down or reset.',
  'mem_format_check': 'The memory card (8MB) (for PlayStation® 2) in MEMORY CARD slot 1 is not formatted. Do you want to format?',
  'mem_format_go'   : 'The memory card (8MB)(for PlayStation® 2) in MEMORY CARD slot 1 is being formatted.',
  'mem_format_done' : 'The memory card (8MB) (for PlayStation® 2) in MEMORY CARD slot 1 has been formatted.',
  'mem_save'        : 'Saving data to memory card (8MB) (for PlayStation® 2) in MEMORY CARD slot 1. Do not remove.',
  'freq_del_ok'     : 'Are you sure you want to delete your FreQ campaign?',
  'freq_mid_del1'   : 'Deleting your FreQ campaign from memory card (8MB) (for PlayStation® 2) in MEMORY CARD slot',
  'freq_mid_del2'   : '. Do not remove your memory card.',
  'mem_check_remix' : 'Warning: FreQuency™ did not detect a memory card in MEMORY CARD slot 1. FreQuency™ requires a memory card (8MB) (for PlayStation® 2) with at least 256 kb free to save Remixes. You may proceed without saving your Remix.',
  'discard_remix'   : 'Are you sure you want to discard your Remix?',
  'remix_del_ask'   : 'Are you sure you want to delete this Remix?',
  'remix_copy_ask'   : 'Are you sure you want to copy this Remix?',
  'no_remix_on_card': 'There are no Remixes on this memory card (8MB) (for PlayStation® 2).',
  'no_freq_on_card' : 'There are no FreQ campaigns on this memory card (8MB) (for PlayStation® 2).',
  'remix_del1'      : 'Deleting your Remix from memory card (8MB) (for PlayStation® 2) in MEMORY CARD slot ',
  'remix_del2'      : '.  Do not remove your memory card.',
  'remix_copy1'     : 'Copying your Remix to memory card (8MB) (for PlayStation® 2) in MEMORY CARD slot',
  'remix_copy2'     : 'Do not remove your memory card.',
  'mem_remix_dupe'  : 'Are you sure you want to overwrite your saved Remix: ',
  'remix_load'      : 'Loading Remix from memory card (8 MB) (for PlayStation® 2) in MEMORY CARD slot 1. Do not remove your memory card.',
  'custom_load'     : 'Loading Custom Song from memory card (8 MB) (for PlayStation® 2) in MEMORY CARD slot 1. Do not remove your memory card.',
  'fact_remix_load' : 'Loading Remix from Disc.  Do no remove Disc.',
  'fact_custom_load': 'Loading Custom Song from Disc.  Do not remove Disc.',
  'mem_detect'      : 'Detecting memory cards (8MB) (for PlayStation® 2) from MEMORY CARD slots 1-4.',
  'remix_list_load' : 'Loading Remix List from memory card (8 MB) (for PlayStation® 2) in MEMORY CARD slot 1. Do not remove your memory card.',
  'freq_load_fail1' : 'Could not load data from memory card (8 MB) (for PlayStation® 2) in MEMORY CARD slot ',
  'remix_load_fail1': 'Could not load Remix from memory card (8 MB) (for PlayStation® 2) in MEMORY CARD slot ',

  'save_remix_command'  : 'Enter a title to save your Remix in MEMORY CARD slot ',
  'save_fail_no_space'  : 'The save has failed because there is insufficient space to save game progress and configuration information. FreQuency™ requires a memory card (8MB) (for PlayStation® 2) with at least 256 kb free to save game progress and configuration information. You may proceed but will lose game progress and configuration information when system is powered down or reset.',
  'save_fail_general'   : 'Save failed.',
  'warn_game_no_space'  : 'There is insufficient space to save game progress and configuration information. FreQuency™ requires a memory card (8MB) (for PlayStation® 2) with at least 256 kb free to save game progress and configuration information. You may proceed but will lose game progress and configuration information when system is powered down or reset.',
  'warn_remix_no_space' : 'There is insufficient space to save Remix data. FreQuency™ requires a memory card (8MB) (for PlayStation® 2) with at least 256 kb free to save remix data. You may proceed but will lose remix information when system is powered down or reset.',

  'freq_limit1' : 'You have saved the maximum number (8) of FreQ campaigns on the memory card  (for PlayStation® 2) in MEMORY CARD slot ',
  'freq_limit2' : 'You must delete some FreQ campaigns from this memory card to make room for more FreQ campaigns.',

  'copy_title' : 'COPYING',
  'mem_copy12' : 'Copying data from memory card (8MB) (for Playstation® 2) in MEMORY CARD slot 1 to memory card (8MB) (for Playstation® 2) in MEMORY CARD slot 2.Do not remove memory cards.',
  'mem_copy21' : 'Copying data from memory card (8MB) (for Playstation® 2) in MEMORY CARD slot 2 to memory card (8MB) (for Playstation® 2) in MEMORY CARD slot 1.Do not remove memory cards.',

  'save_title' : 'SAVING',
  'mem_saveA' : 'Saving data to memory card (8MB) (Playstation® 2) in MEMORY CARD slot ',
  'mem_saveB' : 'Do not remove your memory card.',

#############################################
# keyboard
#############################################

# special for last-row, ' ' indicates no key, s=space key, b=back arrow, 
# f=forward arrow, k signifies kill or delete, d indicates DONE.
#  

#   'f_row'     : '  abcdefghijkl  ',
#   'row1'      : ' 1234567890-+=% ',
#   'row2'      : 'abcdefghijklmnop',
#   'row3'      : 'qrstuvwxyz!~:,.?',
#   'row4'      : '    _@&()"\'>    ',
#   'last_row'  : '  ssss bfk ddd  ',



#keyboard macros
    'kb_macro_f1'   :   'Wanna play a game?',
    'kb_macro_f2'   :   'Wanna remix?',
    'kb_macro_f3'   :   'Yes.',
    'kb_macro_f4'   :   'No.',
    'kb_macro_f5'   :   'I\'m outta here.',
    'kb_macro_f6'   :   'I\'m back.',
    'kb_macro_f7'   :   'Let\'s play "Expert"',
    'kb_macro_f8'   :   'Let\'s play "Normal"',
    'kb_macro_f9'   :   'Let\'s play "Easy"',
    'kb_macro_f10'   :   'Ready?  I\'m gonna launch.',
    'kb_macro_f11'   :   'Easier.',
    'kb_macro_f12'   :   'Harder.',



#the end.
    'end'       : 'end'

    }

def get_met_string (name) :
    return gMetStrings[name]

#########################################################
#
# Every Metagame screen has a title, listed below
#
#########################################################
gMetTitleStrings = {
   'main'       : 'MAIN SCREEN',
   'solo'       : 'SOLO',
   'multi'      : 'MULTIPLAYER',
   'tutorial'   : 'SELECT TUTORIAL',
   'sel_char'   : 'SELECT YOUR FREQ',
   
   'load_char'       : 'LOAD YOUR FREQ',
   'create_char'     : 'CREATE A FREQ',
   'pick_char'       : 'SELECT A FREQ',
   'create_new_char' : 'CREATE NEW FREQ',

   'mode'       : ': SELECT MODE',
   'skill'      : ' GAME: SELECT SKILL',
   'm_num_p'    : 'MULTIPLAYER: SELECT NUMBER',
   'mp_char'    : 'MULTIPLAYER: SELECT YOUR FREQ',
   'remix_type' : ': SELECT REMIX',
   'stages'     : ': SELECT SONG',
   'game'       : 'GAME',
   'remix'      : 'REMIX',
   'arenas'     : ': SELECT ARENA',
   'multi_tips' : 'MULTIPLAYER TIPS ',

   'mcl_card'     : 'MEMORY CARD: SELECT',
   'mem_prefix'   : 'MEMORY CARD SLOT ',
   'mem_del_freq' : 'DELETE OR COPY FREQ',
   'mem_load_remix' : 'MEMORY CARD SLOT 1: LOAD REMIX',
   'mem_del_remix'  : 'DELETE OR COPY A REMIX',
   'mem_load_custom' : 'MEMORY CARD SLOT 1: LOAD CUSTOM SONG',
   'mem_del_type1'    : 'MEMORY CARD SLOT ',
   'mem_del_type2'    : ': DELETE/COPY',

    'freq_maker_buttons'    : 'FreQMAKER: EDIT YOUR FreQ',
    'config_option_buttons' : 'CONFIGURATION OPTIONS',
    'custom_macro_screen'   :   'CUSTOM MACROS',
    'config_controller_options' : 'CONFIGURATION',
    'pangame_options'   :   'GAME SETTINGS',

   'solo_lose'      : 'SOLO GAME: YOU LOSE',
   'solo_win'       : 'SOLO GAME: YOU WIN',
   'solo_remix_over'     : 'END SOLO REMIX',

   'multi_game_over'  : 'MULTIPLAYER GAME OVER',
   'multi_remix_over' : 'END MULTIPLAYER REMIX',

   'met_jukebox_title' :   'JUKEBOX',
   
   'last'       : ''
   }

def get_met_title_string (name) :
   return gMetTitleStrings[name]

#########################################################
#
# Lists of items used in the metagame
#
#########################################################
gMetStringLists = {

# pause screens
   'pause_solo_game'  : ('Resume', 'Quit', 'Restart', 'Controller config', 'Game Settings'),
   'pause_solo_remix' : ('Resume', 'Quit', 'Controller config', 'Game Settings'),

   'pause_multi_game'  : ('Resume', 'Quit', 'Restart'),
   'pause_multi_remix' : ('Resume', 'Quit'),
}

def get_met_stringList (name) :
    return gMetStringLists[name]


#########################################################
#
# Font specification is embedded in the string
#
#########################################################

#########################################################
#
# the table of formatted help strings
#
# use this correspondence for controller characters:
# a - square
# b - triangle
# c - circle
# d - x 
# e - L1 shoulder button
# f - L2 shoulder button
# g - R1 shoulder button
# h - R2 shoulder button
# i - select
# j - start
# k - up arrow
# l - down arrow
# m - left arrow
# n - right arrow
#


############################################
# help text - bottom of screen
############################################
gMetHelpStrings = {
   'ms_tut'          : 'learn to play',
   'ms_solo'         : 'you vs. frequency',
   'ms_multi'        : 'you vs. your friends',
   'ms_opt'          : 'adjust your settings',

   'mcl_card'    : '<FC> c <F1> refresh memory card',

   'mcrf_remix'  : 'delete or copy your remixes',
   'mcrf_freq'   : 'delete or copy your freQs',

   'del_freq'    : '<FC> a <F1> - delete a FreQ, <FC> c <F1> - copy a FreQ',

   'id_name'     : '<FC>mn <F1> choose your FreQ', 
   'id_create'   : 'create a new FreQ',
   'id_edit'     : 'edit your image or info',

   'cid_name'    : '<FC>mn <F1> choose from pre-fab FreQs',
   'cid_save'    : 'save this FreQ',
   'cid_accept'  : 'proceed with this FreQ',
	'cid_edit'    : 'HELP TEXT FOR edit',

   'create_from_prefab'  : 'create new FreQ from basic freQs',
   'create_from_scratch' : 'create new FreQ from scratch',

    #name name freq
    'name_new_freq_ticker'  :   'Hit Enter to Save FreQ',

    #clear text
    'keyboard_clear_ticker'  :   '',

   'p_username'   : 'type your FreQ name. <FC>c <F1> keyboard.',
   'p_custID'     : 'design your FreQ',
   'p_info'       : '',
   'p_viewp'      : 'view your FreQ profile',
   'p_save'       : 'save to memory card',

   'tut_g'        : 'learn to play game mode',
   'tut_r'        : 'learn to play remix mode',

   'sms_game'     : 'beat the game',
   'sms_jam'      : 'create custom remixes',

   'smgs_easy'    : 'beat 12 beginner songs',
   'smgs_normal'  : 'beat 16 challenging songs',
   'smgs_expert'  : 'beat 20 mind-numbing songs',

   'mgs_easy'    : '12 beginner songs',
   'mgs_normal'  : '16 challenging songs',
   'mgs_expert'  : '20 mind-numbing songs',

   'smrt_new'     : 'create custom remix',
   'smrt_load'    : 'load from your memory card',
   'smrt_jukebox' : 'make a remix mega-mix',

   'mem_load_remix' : '<FC>kl <F1> select remix to load',
   'mem_load_custom': '<FC>kl <F1> select remix to load custom song',
   'mem_del_remix'  : '<FC> a <F1> - delete a remix, <FC> c <F1> - copy a remix',

   'levels'       : '<FC>kl <F1> next stage <FC>mn <F1> next song',

   'arenas'       : '<FC>kl <F1> next arena',

   'loc_2p'      : 'select number of players',
   'loc_3p'      : 'select number of players',
   'loc_4p'      : 'select number of players',
   'multi_tips'  : 'learn to play multi mode',

   'multi_tip_help'  : '<FC> a <F1> exit multiplayer tips',
   
   'loc_pc'      : '<FC> mn <F1> choose your freq',

# freqmaker
	 'fqmak_randomize'      : '<FC> d <F1> generate a random freq',
     'fqmak_mutate'         : '<FC> d <F1> mutate your freq',
	 'fqmak_body'			: '<FC> d <F1> select a body stamp',
	 'fqmak_head'			: '<FC> d <F1> select a head stamp',
	 'fqmak_face'			: '<FC> d <F1> select a face stamp',
	 'fqmak_details'		: '<FC> d <F1> select a detail stamp',
	 'fqmak_logos'			: '<FC> d <F1> select a logo stamp',
	 'fqmak_edit'			: '<FC> d <F1> edit your freq',
	 'fqmak_name'			: '<FC> d <F1> name your freq',
	 'fqmak_save'			: '<FC> d <F1> save your freq',

     'fqmak_editing_mode'		: 'right analog stick to position stamp',
     'fqmak_positioning_mode'	: 'right analog stick to position stamp',
     'fqmak_choosing_mode'		: '<FC> k l m n <F1> to select a stamp',
     'fqmak_coloring_mode'		: 'right analog stick to select color',



# config options buttons
	 'nob_game_setup'       : 'Change your settings',
	 'nob_controller_setup' : 'Customize controller configuration',
	 'nob_mem_card_setup'   : 'Delete & copy FreQs and remixes',
	 'nob_disk_change'		: 'Expansion pack access',
	 'nob_credits'			   : 'The FreQ freqs...',


# config controller buttons
	 'controller_config_left_note_1'    : '<FC> m n <F1> primary left note button',
	 'controller_config_left_note_2'    : '<FC> m n <F1> secondary left note button',
	 'controller_config_center_note_1'  : '<FC> m n <F1> primary center note button',
	 'controller_config_center_note_2'  : '<FC> m n <F1> secondary center note button',
	 'controller_config_right_note_1'   : '<FC> m n <F1> primary right note button',
	 'controller_config_right_note_2'   : '<FC> m n <F1> secondary right note button',
	 'controller_config_erase_and_power'    : '<FC> m n <F1> erase & powerup button',
	 'controller_config_expression' : '<FC> m n <F1> expression button',
     'controller_config_remix_fx'   : '<FC> m n <F1> remix fx button',


# keyboard
    'met_keyboard_text_too_wide'    :   'text limit reached',
    'met_keyboard_macro_too_large'  :   'macro too large for the space allowed',

#jukebox
    'met_jukebox_base_screen_help_tab'  :   '<FC>d<F2> ADD  <FC>b<F2> BACK',
    'met_jukebox_base_screen_ticker_tape'   :   '<FC>d<F1> add remix to my playlist',
    'met_jukebox_edit_screen_help_tab'  :   '<FC>d<F2> DELETE  <FC>b<F2> BACK',
    'met_jukebox_edit_screen_ticker_tape'   :   '<FC>d<F1> remove remix from my playlist',
    'met_jukebox_done_screen_tab_play'  :   '<FC>d<F2> LOAD  <FC>b<F2> BACK',
    'met_jukebox_done_screen_ticker_play'   :   '<FC>d<F1> play my playlist',
    'met_jukebox_done_screen_tab_save'  :   '<FC>d<F2> SAVE  <FC>b<F2> BACK',
    'met_jukebox_done_screen_ticker_save'   :'<FC>d<F1> save my playlist',

#save remix
    'met_save_remix_screen_ticker_tape' :   'name your remix',

#k,l,m,n = ^,v,<,>
#game prefs...
     'pangame_audio' :   '<FC> m n <F1> Select Mono / Stereo',
     'pangame_beat_assist'  : '<FC> m n <F1> Audio Clues',
     'pangame_force_feedback'   :   '<FC> m n <F1> Controller Vibration',
     'pangame_tab_text'   :   '<FC> d <F2> SAVE <FC> b <F2> BACK',

# save remix
   'remix_save' : '<FC> c <F1> to bring up keyboard',

# end game
   'egsl_again'        : 'play this song again',
   'egsl_levels'       : 'return to song select screen',
   
   'egsw_continue'     : 'return to song select screen',
   'egsw_exit'         : 'return to main menu',
   'egsw_restart'      : 'play this song again',


   'egmg_again'        : 'play this song again',
   'egmg_new'          : 'return to song select screen',

# tab titles for options help panel
   'standard_title' : '<FC> d <F2> ACCEPT <FC> b <F2> BACK',
   'freq_maker_save_button' : '<FC> d <F2> SAVE <FC> b <F2> BACK',
   'no_back_title'  : '<FC> d <F2> ACCEPT ',
   'only_back_title'  : '<FC> b <F2> BACK',
   'remix_save_options' : '<FC> d <F2> SAVE  <FC> a <F2> DISCARD',
   'remix_load_opt' : '<FC> d <F2> LOAD  <FC> b <F2> BACK',
   'del_opt'        : '<FC> a <F2> DELETE  <FC> b <F2> BACK',
   'mc_opt'         : '<FC> d <F2> LOAD  <FC> b <F2> BACK',
   'mem_card_pick_title' : '<FC> d <F2> LOAD  <FC> b <F2> BACK',

   'last'        : ''
}

#########################################################
#
# our Font Lookup function
#
FontLookUp = {
    'F1'     :  'font1_plain_3',
    'F2'     :  'font1_blue_1',
    'FC'     :  'controller.font'
}

def translate_font (str):
   return FontLookUp[str]

#########################################################
#
# Parse a font string
#
# given a string '<FC>RL <F1>Choose your FreQ'
#
# return         ( ('controller.font', 'RL')
#                  ('font_1_blue_2', 'Choose your FreQ')
#                )

#  import re
#  font_re = re.compile (r"<(F\w+)>")

#  def parse_str_with_re (str):
#      table = []                          # return value
#      font = 'F1'                         # start out with default font
#      while len(str) > 0:
#          match = font_re.search (str)
#          if match:
#              text_end = match.start()    # where regular text ends
#              if text_end > 0:            # case where font expr is not at beginning
#                  text = str[:match.start()]
#                  table.append ((translate_font(font), text))
#              font = match.group(1)
#              str = str[match.end():]
#          else:
#              break
#      if len(str) > 0:
#          table.append ((translate_font(font), str))
#      return table

# Version without having to import re
def parse_str (str):
    table = []                          # return value
    font = 'F1'                         # start out with default font
    while len(str) > 0:
        pos = str.find ('<F')
        if pos != -1:
            pos2 = str.find ('>', pos)
            if pos2 != -1:
                if pos > 0:             # case where font expr is not at beginning
                    text = str[:pos]
                    table.append ((translate_font(font), text))
                font = str[pos+1 : pos2]
                str = str[pos2+1 : ]
        else:
            break
    if len(str) > 0:
        table.append ((translate_font(font), str))
    return table

#########################################################
#
# get_help_FST (str)
# returns the font-string-table for 'str'
# this is the function that C++ uses
#
def get_help_FST (str):
    return parse_str (gMetHelpStrings[str])
