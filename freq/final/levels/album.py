
############################################
#
# Everything in here will change from album to album(expansion to expansion)
#

# Need to run this python script in order to use the tutorials.  Should only
#  happen for the original frequency disk!!!
global_execfile (get_absolute_path ('levels/tutorial/tutor.py'))

def get_album_name ():
    return 'Frequency -- Original'

def get_album_num ():
    return 0


# the levels of this game: (<level-name>, <stage-num>, <order-within-stage>)
levels_database = (
    ('winner',          1, 1),
    ('akro',            1, 2),
    ('nodoubt',         1, 3),
    ('xlr8r',           1, 4),
    ('sgg',             1, 5),
    
    ('dubpistols',      2, 1),
    ('lofi',            2, 2),
    ('fear',            2, 3),
    ('oakenf',          2, 4),
    ('selecta',         2, 5),
    
    ('power',           3, 1),
    ('orbital',         3, 2),
    ('qbert',           3, 3),
    ('bt',              3, 4),
    ('curve',           3, 5),
    
    ('jungle',          4, 1),
    ('funk',            4, 2),
    ('ronisize',        4, 3),
    ('mbm',             4, 4),
    ('juno',            4, 5),
    
    ('moto',            5, 1),
    ('trance',          5, 2),
    ('funkydope',       5, 3),
    ('controlyourbody', 5, 4),
    ('freqout',         5, 5),

# stage 6 is a fake way of showing the secret levels
# they really will be found hidden in stage 5

    ('luge',            6, 6),
    ('endofyourworld',  6, 7)
    )

# the arenas of this game: (<arena-name>, <display-order>)
arenas_database = (
    ('blue',    1),
    ('carn',    2),
    ('const',   3),
    ('eqlizer', 4),
    ('glas',    5),
    ('para',    6),
    ('green',   7),
    ('wall',    8),
    ('blank',   9),
    ('green_multi', 1),
    ('blue_multi',  2),
    ('wall_multi',  3),
    ('const_multi', 4)
    )

# the high score needed to beat a stage: (<easy>, <normal>, <expert>)
beat_stages_lookup = [
# STAGE 1
   [800, 2000, 4000],

# STAGE 2
   [1000, 2000, 4000],

# STAGE 3
   [1200, 2400, 4400],

# STAGE 4
   [1200, 2400, 4000],

# STAGE 5
   [1200, 2400, 3200]
   ]

# List of recording files to play back in attract mode
recording_files = ['levels/winner.bin',
                   'levels/dubpistols.bin',
                   'levels/orbital.bin',
                   'levels/qbert.bin',
                   'levels/fear.bin',
                   'levels/okenf.bin',
                   'levels/selecta.bin',
                   'levels/curve.bin']
