##########################################################
#
# pers_dat.py
#
# This file contains all default persona data
#
# Below, each FreQ character has a 'dictionary' lookup of 
# its attributes
#
# At the very bottom of the file is the global list of all characters.
#
# If you add a character, you must both create a dictionary
# and add them to the global list at the bottom
#

##########################################################
#
# definition of all the FreQs
#
##########################################################

#--------------------------------------------------------
velma_dict = {
   'name'   : 'Velma',
   'id'     : 'dj_velma.tex',
   'skill'  : 'hard',
   'rank'   : '4',
   'email'  : 'tekgrl@tek.org',
   'music'  :  'freezepop',
   'info'   :  'i luv symbion'
}

#--------------------------------------------------------
slimy_dict = {
   'name'   : 'Dj Slimy',
   'id'     : 'dj_djslimy.tex',
   'skill'  : '',
   'rank'   : '',
   'email'  : '',
   'music'  : '',
   'info'   : ''
}

#--------------------------------------------------------
angryrobot_dict = {
   'name'   : 'Angry Robot',
   'id'     : 'dj_angryrobot.tex',
   'skill'  : '',
   'rank'   : '',
   'email'  : '',
   'music'  : '',
   'info'   : ''
}

#--------------------------------------------------------
munk_dict = {
   'name'   : 'MuNk',
   'id'     : 'dj_munk.tex',
   'skill'  : '',
   'rank'   : '',
   'email'  : '',
   'music'  : '',
   'info'   : ''
}

#--------------------------------------------------------
mechbunny_dict = {
   'name'   : 'Mech Bunny',
   'id'     : 'dj_mechbunny.tex',
   'skill'  : '',
   'rank'   : '',
   'email'  : '',
   'music'  : '',
   'info'   : ''
}

#--------------------------------------------------------
gruvmonk_dict = {
   'name'   : 'Gruv Monkey',
   'id'     : 'dj_groovemonkey.tex',
   'skill'  : '',
   'rank'   : '',
   'email'  : '',
   'music'  : '',
   'info'   : ''
}

#--------------------------------------------------------
punker_dict = {
   'name'   : 'Punker',
   'id'     : 'dj_mohawk.tex',
   'skill'  : '',
   'rank'   : '',
   'email'  : '',
   'music'  : '',
   'info'   : ''
}

#--------------------------------------------------------
atomic_dict = {
   'name'   : 'Atomic',
   'id'     : 'dj_atomic.tex',
   'skill'  : '',
   'rank'   : '',
   'email'  : '',
   'music'  : '',
   'info'   : ''
}

#--------------------------------------------------------
babyhuey_dict = {
   'name'   : 'Baby Huey',
   'id'     : 'dj_babyhuey.tex',
   'skill'  : '',
   'rank'   : '',
   'email'  : '',
   'music'  : '',
   'info'   : ''
}

#--------------------------------------------------------
c3poo_dict = {
   'name'   : 'C303PO',
   'id'     : 'dj_c3poo.tex',
   'skill'  : '',
   'rank'   : '',
   'email'  : '',
   'music'  : '',
   'info'   : ''
}

#--------------------------------------------------------
farout_dict = {
   'name'   : 'Farout',
   'id'     : 'dj_farout.tex',
   'skill'  : '',
   'rank'   : '',
   'email'  : '',
   'music'  : '',
   'info'   : ''
}

#--------------------------------------------------------
free_dict = {
   'name'   : 'Free',
   'id'     : 'dj_free.tex',
   'skill'  : '',
   'rank'   : '',
   'email'  : '',
   'music'  : '',
   'info'   : ''
}

#--------------------------------------------------------
femfatal_dict = {
   'name'   : 'Fem Fatal',
   'id'     : 'dj_femmefatal.tex',
   'skill'  : '',
   'rank'   : '',
   'email'  : '',
   'music'  : '',
   'info'   : ''
}

#--------------------------------------------------------
nerdstrom_dict = {
   'name'   : 'Nerdstrom',
   'id'     : 'dj_nerdstrom.tex',
   'skill'  : '',
   'rank'   : '',
   'email'  : '',
   'music'  : '',
   'info'   : ''
}

#--------------------------------------------------------
pinkeye_dict = {
   'name'   : 'Pinkeye',
   'id'     : 'dj_pinkeye.tex',
   'skill'  : '',
   'rank'   : '',
   'email'  : '',
   'music'  : '',
   'info'   : ''
}

#--------------------------------------------------------
racer_dict = {
   'name'   : 'Racer',
   'id'     : 'dj_racer.tex',
   'skill'  : '',
   'rank'   : '',
   'email'  : '',
   'music'  : '',
   'info'   : ''
}

##########################################################
#
# list of all characters
#
##########################################################
gPersonaDict = {
   'punker'          : punker_dict,
   'velma'           : velma_dict,
   'slimy'           : slimy_dict,
   'angryrobot'      : angryrobot_dict,
   'munk'            : munk_dict,
   'mechbunny'       : mechbunny_dict,
   'gruvmonk'        : gruvmonk_dict,
   'atomic'          : atomic_dict,
   'babyhuey'        : babyhuey_dict,
   'c3poo'           : c3poo_dict,
   'farout'          : farout_dict,
   'free'            : free_dict,
   'femfatal'        : femfatal_dict,
   'nerdstrom'       : nerdstrom_dict,
   'pinkeye'         : pinkeye_dict,
   'racer'           : racer_dict
}

##########################################################
#
# This function returns the keys to the global list of personas
#
def get_pers_table():
    return (gPersonaDict.keys())


##########################################################
#
# This function returns the value associated with a_key for dictionary dict
#
def get_pers_string(dict, a_key):
    return (gPersonaDict[dict][a_key])

