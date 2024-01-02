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
### THESE ARE TEXT FOR BUTTONS
############################################
gMetStrings = {

# pause screen
   'pause_game'   : 'Game Paused',
   'pause_remix'  : 'Remix Paused',
   'pause_net'    : 'Quit Playing?',

# loading screen
   'load_game'    : 'LOADING GAME',
   'load_remix'   : 'LOADING REMIX',
   'load_tut'     : 'LOADING\nTUTORIAL',

# persona screen - select your Freq
   'id_create'    : 'CREATE NEW FREQ',
   'id_edit'      : 'EDIT YOUR FREQ',

# persona create new Freq

   'p_username'   : 'user name',
   'p_custID'     : 'customize FreQ',
   'p_info'       : 'personal info',
   'p_viewp'      : 'view profile',
   'p_save'       : 'accept',
   'p_del'        : 'delete',

   'cid_save'     : 'SAVE',
   'cid_accept'   : 'ACCEPT',

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
   
   'tut'       : 'TUTORIAL',
   'solo'      : 'SOLO',
   'multi'     : 'MULTI',
   'net'       : 'NET',
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

# stage select

   'stage1'    : 'STAGE 1',
   'stage2'    : 'STAGE 2',
   'stage3'    : 'STAGE 3',
   'stage4'    : 'STAGE 4',
   'stage5'    : 'STAGE 5',
   'exit'      : 'EXIT',
   'stage'     : 'STAGE',
   'ss_custom' : 'CUSTOM',

   'stage4easywarn' : 'AVAILABLE IN NORMAL AND EXPERT MODE',
   'stage5easywarn' : 'AVAILABLE IN EXPERT MODE ONLY',
   'custom_warning' : 'CUSTOM LEVELS WILL BE HERE',

# arena select
   'arena1' : 'ARENA 1',
   'arena2' : 'ARENA 2',
   'arena3' : 'ARENA 3',
   'arena4' : 'ARENA 4',
   'arena5' : 'ARENA 5',
   'arena6' : 'ARENA 6',

# stage_finish
   'stf_congrat'      : 'CONGRATULATIONS!',
   'stf_complete1'    : 'You\'ve unlocked the ',
   'stf_arena'        : 'arena',
   'stf_completeX'    : 'You\'ve unlocked stage ',
   'stf_completeMid'  : 'and the ',
   

############################################
# net buttons
############################################

# net portal

   'np_name'   : 'NAME',
   'np_enter'  : 'ENTER FREQNET',
   'np_exit'   : 'EXIT',
   'np_edit'   : 'EDIT YOUR FREQ',
   'np_tut'    : 'TUTORIAL',
   'np_opt'    : 'NET SETTINGS',

# net settings
   'nsip_ip'   : 'IP ADDRESS',
   'nsip_id'   : 'WORLD ID',
    
# net main

   'nm_chat'   :  'CHAT',
   'nm_host'   :  'HOST',
   'nm_join'   :  'JOIN',
   'nm_quick'  :  'QUICKPLAY',
   'nm_friends':  'FRIENDS',
   'nm_rank'   :  'RANKINGS',
   'nm_option' :  'OPTIONS',

# net main chat
   'nmc_label'        : 'LOBBY NAME',
   'nmc_room_label'   : 'ROOMS',
   'nmc_remix_label'  : 'REMIXES',
   'nmc_game_label'   : 'GAMES',
   'nmc_freq_label'   : 'FREQS',

# net main lobby
   'nml_label' : 'lobbies',

# net main new chat
   'nmnc_newname'    : 'new name',
   'nmnc_ok'         : 'ok',
   'nmnc_create_lbl' : 'create new chat',
   'nmnc_name_lbl'   : 'name',
   'nmnc_friends_lbl': 'friends only',

# net community
   'nc_host'      :  'host',
   'nc_join'      :  'join',
   'nc_observe'   :  'observe',
   'nc_find'      :  'find',
   'nc_chat'      :  'chat',

# net community games
   'ncg_mode'     :  'mode',
   'ncg_level'    :  'level',
   'ncg_skill'    :  'skill',
   'ncg_number'   :  '#',

   'ncg_dummy'    : 'g    body mov     n    1/2',

# net community player
   'ncp_player'   : 'player',

# net community player profile
   'nccp_rank'    : 'rank:',
   'nccp_email'   : 'email:',
   'nccp_info'    : 'info:',
   'nccp_music'   : 'music:',

# net hosting
   'nh_levels' : 'RANDOM',
   'nh_arenas' : 'RANDOM',
   'nh_host'   : 'HOST',
   'nh_abort'  : 'ABORT',
   'nh_mode_lbl'   : 'MODE',
   'nh_skill_lbl'  : 'SKILL',
   'nh_num_lbl'    : '# PLAYERS',
   'nh_levels_lbl' : 'LEVELS',
   'nh_arenas_lbl' : 'ARENAS',
   'nh_friend_lbl' : 'FRIENDS ONLY',

# net hosting - used for levels and arenas
   'nh_random'    : 'Random',

# net hosting levels
   'nhl_level_lbl'   : 'LEVELS',

# net searching
   'ns_find'   : 'FIND',
   'ns_levels' : 'ALL LEVELS',
   'ns_mode_lbl'   : 'MODE',
   'ns_skill_lbl'  : 'SKILL',
   'ns_levels_lbl' : 'LEVELS',
   'ns_friends_lbl' : 'FRIENDS ONLY',

# net sorted hub
   'nsh_join'        :  'join',
   'nsh_dummy'       :  'g body movin n 2/3 ',
   'nsh_mode_lbl'    :  'mode',
   'nsh_lev_lbl'     :  'lev',
   'nsh_skill_lbl'   :  'skill',
   'nsh_num_lbl'     :  '#',
   'nsh_conn_lbl'    :  'conn',
   'nsh_friend_lbl'  :  'friend',


# net launch host
   'nlh_launch' : 'LAUNCH',
   'nlh_abort'  : 'ABORT',
   'nlh_edit'   : 'EDIT',
   'nlh_invite' : 'INVITE',
   'nlh_chat'   : 'CHAT',

# net launch client
   'nlc_invite' :  'INVITE',
   'nlc_abort'  :  'ABORT',
   'nlc_chat'   :  'CHAT',

# net launch session
   'nls_arena_label'    : 'ARENA:',
   'nls_mode_label'     : 'MODE:',
   'nls_skill_label'    : 'SKILL:',
   'nls_numplay_label'  : '# PLAYERS:',
   'nls_friend_label'   : 'FRIENDS:',

# net launch players
   'nl_players_lbl'     : 'PLAYERS',

# end of game solo lose
   'egsl_again'   : 'REPLAY',
   'egsl_levels'  : 'EXIT',

   'egsw_continue' : 'CONTINUE',
   'egsw_exit'     : 'QUIT',

   'egsr_continue' : 'CONTINUE',

   'egmg_again'    : 'PLAY AGAIN',
   'egmg_new'      : 'NEW GAME',

   'egmr_continue' : 'CONTINUE',
   'egng_continue' : 'CONTINUE',

# stage finish
   'stf_continue'  : 'CONTINUE',
   'stf_exit'      : 'EXIT',

# memory card
   'mcrf_remix'    : 'REMIXES',
   'mcrf_freq'     : 'FREQS',

#############################################
# DEMO MSGS
#############################################

   'demo_ss1'     : 'TUTORIAL',
   'demo_ss2'     : 'SONG 1: EASY',
   'demo_ss3'     : 'SONG 2: EASY',
   'demo_ss4'     : 'SONG 1: NORM',
   'demo_ss5'     : 'SONG 2: NORM',

#############################################
# DIALOG MSGS
#############################################

# memory card
  'mem_load'      : 'Loading data from PS2 Memory Card (8MB) in Memory Card Slot 1. Do not remove your memory card',
#  'mem_check'     : 'FreQuency requires a PS2 Memory Card (8MB) with at least X kb free to save game progress and configuration information.  You may proceed but will lose all information when system is powered down or reset.',
  'mem_check'     : 'No memory card detected.',

#############################################
# keyboard
#############################################

# special for last-row, ' ' indicates no key, s=space key, b=back arrow, 
# f=forward arrow, k signifies kill or delete, d indicates DONE.
#  

   'f_row'     : '  abcdefghijkl  ',
   'row1'      : ' 1234567890-+=% ',
   'row2'      : 'abcdefghijklmnop',
   'row3'      : 'qrstuvwxyz!~:,.?',
   'row4'      : '    _@&()"\'>    ',
   'last_row'  : '  ssss bfk ddd  ',

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
   'load_char'  : 'LOAD YOUR FREQ',
   'create_char' : 'CREATE YOUR FREQ',
   'mode'       : ': SELECT MODE',
   'skill'      : ' GAME: SELECT SKILL',
   'm_num_p'    : 'MULTIPLAYER: SELECT NUMBER',
   'mp_char'    : 'MULTIPLAYER: SELECT YOUR FREQ',
   'remix_type' : ': SELECT REMIX',
   'stages'     : ': SELECT LEVEL',
   'game'       : 'GAME',
   'remix'      : 'REMIX',
   'arenas'     : ': SELECT ARENA',

   'net_portal'   : 'FREQNET PORTAL',
   'net_settings' : 'NET SETTINGS',
   'net_main'     : 'FREQNET MAIN',
   'net_host'     : 'CONFIGURE HOST',
   'net_search'   : 'FREQNET GAME SEARCH',
   'net_sort'     : 'FREQNET GAMES HUB',
   'net_com'      : 'PHATBEATS ROOM',
   'net_launch'   : 'LAUNCHPAD',

   'mcl_card'     : 'MEMORY CARD: LOAD - DELETE',
   'mem_delete'   : 'DELETE FROM MEMORY CARD',
   'mem_del_freq' : 'DELETE FREQ',

   'psx_control'  : 'CONTROLLER CONFIGURATION',
   'mode_demo'    : 'DEMO GAME: SELECT MODE',
   'level_demo'   : 'DEMO GAME: SELECT SONG',
   'post_demo'    : 'END OF DEMO',

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

# net main
   'nm_lobby'        : ('electronica', 'hiphop', 'house', 'rock', 'trance'),
   'nm_lobby_stat'   : ('12>400', '12>400', '12>400', '12>400', '12>400'),
   'nm_lobbyinfo'    : ('516 people in electronica', 
                        '716 people in hiphop',
                        '444 people in house',
                        '327 people in rock',
                        '666 people in trance' ),

   'nm_chatrooms'      : ('create new room', 'phatbeats', 'kick it', 'bass bin'),
   'nm_chatrooms_info' : ('', '322 in phatbeats', '78 in kick it', '116 in bass bin'),

# net host setup
   'nh_modes'        : ('GAME', 'REMIX'),
   'nh_skills'       : ('EASY', 'NORMAL', 'EXPERT'),
   'nh_numPlayers'   : ( '2 PLAYERS', '3 PLAYERS', '4 PLAYERS'),
   'nh_friends'      : ( 'YES', 'NO'),
   'ns_modes'        : ( 'ALL MODES', 'GAME', 'REMIX')
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
# the table of formatted option strings
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
gMetOptionStrings = {
   'ms_tut'      : 'learn to play',
   'ms_solo'     : 'you vs. frequency',
   'ms_multi'    : 'you vs. your friends',
   'ms_net'      : 'you vs. the world',
   'ms_opt'      : 'adjust your settings',

   'mcl_card'    : '<FC>d<F1>load <FC>b<F1>back <FC>c<F1>refresh',

   'mcrf_remix'  : 'access remixes from memory card',
   'mcrf_freq'   : 'access freqs from memory card',

   'mcfl_01'     : 'pick which freq to delete',

   'id_name'     : '<FC>mn<F1> choose your freq', 
   'id_create'   : 'create a new freq',
   'id_edit'     : 'edit your image or info',

   'cid_name'    : '<FC>mn<F1> choose your face <FC>a <F1> edit name',
   'cid_save'    : 'save this FreQ',
   'cid_accept'  : 'proceed with this FreQ',

   'p_username'   : 'type your freq name. <FC>c <F1> keyboard.',
   'p_custID'     : 'design your freq',
   'p_info'       : '',
   'p_viewp'      : 'view your freq profile',
   'p_save'       : 'save to memory card',

   'tut_g'        : 'learn to play game mode',
   'tut_r'        : 'learn to play remix mode',

   'sms_game'     : 'beat the game',
   'sms_jam'      : 'create custom remixes',

   'smgs_easy'    : 'beat 12 beginner levels',
   'smgs_normal'  : 'beat 16 challenging levels',
   'smgs_expert'  : 'beat 20 mind-numbing levels',

   'smrt_new'     : 'create custom remix',
   'smrt_load'    : 'load from your memory card',
   'smrt_jukebox' : 'make a remix mega-mix',

   'levels'       : '<FC>kl <F1> next stage <FC>mn <F1> next Level',

   'arenas'       : '<FC>kl <F1> next arena',

   'loc_2p'      : 'select number of players',
   'loc_3p'      : 'select number of players',
   'loc_4p'      : 'select number of players',
   
   'loc_pc'      : '<FC>mn <F1> choose your freq',

   'np_name'   : '<FC>mn<F1> choose your freq',
   'np_enter'  : 'connect to play online',
   'np_edit'   : 'edit your image or info',
   'np_tut'    : 'learn to play',
   'np_opt'    : 'modify your net settings',

   'nsip_ip'   : '',
   'nsip_id'   : '',

   'nh_host'   : 'host a new session',
   'nh_mode'   : 'select mode of play',
   'nh_skill'  : 'select difficulty',
   'nh_level'  : 'select a level',
   'nh_arena'  : 'select an arena',
   'nh_friends' : 'open or closed',

   'nlh_launch_g' : 'start the game.',
   'nlh_launch_r' : 'start the remix.',
   'nlh_edit_g'   : 'change game settings',
   'nlh_edit_r'   : 'change remix settings',
   'nlh_invite'   : 'invite friends to join',
   'nlh_abort_g'  : 'exit game',
   'nlh_abort_r'  : 'exit remix',

   'nlc_invite'   : 'invite friends to join',
   'nlc_abort_g'  : 'exit game',
   'nlc_abort_r'  : 'exit remix',
   
   'nlp_h'       : '<FC> n <F1> to launch.',
   'nlp_g'       : '<FC> n <F1> to invite.',

   'psx_control'  : '<FC> d <F1> = continue',
   'main_demo1'   : 'you vs. frequency',
   'main_demo2'   : 'available in full version',
   'main_demo3'   : 'available in full version',
   'main_demo4'   : 'available in full version',
   'mode_demo1'   : 'beat the game',
   'mode_demo2'   : 'available in full version',
   'level_demo'   : '<FC>kl <F1> next song',

   'standard_title' : '<FC> d <F2> ACCEPT <FC> b <F2> BACK',
   'no_back_title'  : '<FC> d <F2> CONTINUE',

   'last'        : ''
}

#########################################################
#
# our Font Lookup function
#
def translate_font (str):
   FontLookUp = {
      'F1'     :  'font1_plain_3',
      'F2'     :  'font1_blue_1',
      'FC'     :  'controller.font'
   }
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

import re
font_re = re.compile (r"<(F\w+)>")

def parse_str (str):
    table = []                          # return value
    font = 'F1'                         # start out with default font
    while len(str) > 0:
        match = font_re.search (str)
        if match:
            text_end = match.start()    # where regular text ends
            if text_end > 0:            # case where font expr is not at beginning
                text = str[:match.start()]
                table.append ((translate_font(font), text))
            font = match.group(1)
            str = str[match.end():]
        else:
            break
    if len(str) > 0:
        table.append ((translate_font(font), str))
    return table

#########################################################
#
# get_options_FST (str)
# returns the font-string-table for 'str'
# this is the function that C++ uses
#
def get_options_FST (str):
    return parse_str (gMetOptionStrings[str])
