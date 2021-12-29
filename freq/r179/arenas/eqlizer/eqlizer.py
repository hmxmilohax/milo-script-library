class EQArena (Arena):
    def __init__ (self):
        self.directory_name = 'eqlizer'

    def get_name (self):        return "EQlizer"
    def get_arena_id (self):    return 3          # Unique id for this arena

    # arg is: 0 - bad, 1 - good, 2 - great
    def on_health (self, arg):
        if (arg > 2): arg = 2
        
        hx.anim_speed ("Group_a1.view", (0.2, 1, 1.5)[arg])
	hx.anim_speed ("Group_a2.view", (0.2, 1, 1.5)[arg])
	hx.anim_speed ("Group_a3.view", (0.2, 1, 1.5)[arg])
	hx.anim_speed ("Group_a4.view", (0.2, 1, 1.5)[arg])
        hx.anim_speed ("Group_b1.view", (0.2, 1, 1.2)[arg])
	hx.anim_speed ("Group_b2.view", (0.2, 1, 1.2)[arg])
        hx.anim_speed ("Group_c_columns.view", (0.2, 1, 1.5)[arg])
        hx.anim_speed ("Group_d1.view", (0.2, 1, 1.5)[arg])
	hx.anim_speed ("Group_d2.view", (0.2, 1, 1.5)[arg])
	hx.anim_speed ("Group_d3.view", (0.2, 1, 1.5)[arg])
	hx.anim_speed ("D_object1_plane1.msnm", (0, 5, 7)[arg])

	hx.anim_minmax ("light01.litAnim", (200,0,400)[arg], (300,100,1000)[arg])
	hx.anim_minmax ("A_red.matAnim", (800,0,200)[arg], (2300,100,700)[arg])
	hx.anim_minmax ("A_purple2.matAnim", (800,0,200)[arg], (1000,100,700)[arg])
	hx.anim_minmax ("A_stairs.matAnim", (800,0,200)[arg], (1000,100,700)[arg])
	hx.anim_minmax ("B_red.matAnim", (800,0,200)[arg], (1000,100,700)[arg])
	hx.anim_minmax ("D_blue.matAnim", (800,0,200)[arg], (1000,100,700)[arg])
	hx.anim_minmax ("skysphere.matAnim", (200,0,0)[arg], (300,100,100)[arg])



def get_arena_class_name ():
    return EQArena
