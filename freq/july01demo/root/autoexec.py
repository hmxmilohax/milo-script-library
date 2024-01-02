def skip_metagame () : return 0
default_game_params = ['FunkyDope', 'game', 1, 1, 'Blue']

def show_timers (): return 0


#def get_midi_device() : return 1
#proc hx::wacko_panning {} { return 1 }

def on_key_down (key) :
    if   key == 112: hx.clock ('step', 10)  #f1
    elif key == 113: hx.clock ('step', 50)  #f2
    elif key == 114: hx.clock ('start')     #f3
    elif key == 115: hx.toggle_hudview()    #f4
    elif key == 116: add_powerups_to_all()  #f5

def add_powerups_to_all ():
    for pl in (0,1,2,3) :
        hx.add_powerup (pl, powerup_num ('neu'))
        hx.add_powerup (pl, powerup_num ('fre'))
        hx.add_powerup (pl, powerup_num ('aut'))
        hx.add_powerup (pl, powerup_num ('crp'))

def autoexec() :
#   hx.capture ('rec')
    pass

#last number: use 1 for window, 0 for full-screen
def get_screen_config ():  return (640, 480, 16, 1)

# 0 = false, 1 = true
def show_splash_screen ():  return 0
def show_gui_fullscreen (): return 0

#def get_freqnet_session(): return "FreqnetServerDev"

class LevelOverride:
    def __init__ (self):
        self.enable_all = 0

    #def wacko_panning (self):
    #    return 1

    #def get_initial_bar_amount (self): return 120
    
    # How many bars does the juice meter cap at?
    #def get_max_bar_amount (self): return 120

    # How far off you can be from a gem and still catch it, in milliseconds
    #def get_slop (self): return 80



#
# APPENDIX
#
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
