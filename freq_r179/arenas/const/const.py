class ConstArena (Arena):
    def __init__ (self):
        self.directory_name = 'const'

    def get_name (self):        return "Constructo"
    def get_arena_id (self):    return 2          # Unique id for this arena

    # arg is: 0 - bad, 1 - good, 2 - great
    def on_health (self, arg):
        if (arg > 2): arg = 2
        
        hx.anim_speed ("Group_C.view", (0.1, 1, 2)[arg])
        hx.anim_speed ("wall_red.matAnim", (5,5,15)[arg])
        hx.anim_speed ("green_cube_mat.view", (0,1,1.5)[arg])
        hx.anim_speed ("light01.litAnim", (1,10,20)[arg])

	hx.anim_minmax ("wall_base_purple.matAnim", (200,0,0)[arg], (300,100,100)[arg])
	hx.anim_minmax ("wall_blue.matAnim", (200,0,0)[arg], (300,100,100)[arg])
	hx.anim_minmax ("wall_light_purple.matAnim", (200,0,0)[arg], (300,100,100)[arg])
	hx.anim_minmax ("monitor_A01.msnm", (0,0,62440)[arg], (100,100,65440)[arg])
	hx.anim_minmax ("green_cube_mat.view", (21000,0,10000)[arg], (21100,9000,22000)[arg])
	hx.anim_minmax ("light01.litAnim", (0,0,11000)[arg], (10000,10000,22000)[arg])

def get_arena_class_name ():
    return ConstArena
