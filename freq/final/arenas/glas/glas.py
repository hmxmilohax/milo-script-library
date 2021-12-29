class GlasArena (Arena):
    def __init__ (self):
        self.directory_name = 'glas'

    def get_name (self):        return "GlasHaus"
    def get_arena_id (self):    return 4          # Unique id for this arena

    # arg is: 0 - bad, 1 - good, 2 - great
    def on_health (self, arg):
        if (arg > 2): arg = 2
        
        hx.anim_speed ("Group_a1.view", (0.1, 1, 2)[arg])
        hx.anim_speed ("Group_a2.view", (0.1, 1, 2)[arg])
        hx.anim_speed ("Group_a3.view", (0.1, 1, 2)[arg])
        hx.anim_speed ("Group_a4.view", (0.1, 1, 2)[arg])
        hx.anim_speed ("Group_a5.view", (0.1, 1, 2)[arg])
        hx.anim_speed ("object_A03_shape.msnm", (0, 5, 10)[arg])
        hx.anim_speed ("A_screenPlane4.tnm", (0.1, 1, 2)[arg])
        hx.anim_speed ("A_screenPlane7.tnm", (0.1, 1, 2)[arg])

        hx.anim_speed ("Group_B_object1.view", (0, 1, 2)[arg])
        hx.anim_speed ("Group_B_object2.view", (0, 1, 2)[arg])

        hx.anim_speed ("Group_c1.view", (0, 1, 2)[arg])
        hx.anim_speed ("Group_c2.view", (0, 1, 2)[arg])
        hx.anim_speed ("Group_c3.view", (0, 1, 2)[arg])
        hx.anim_speed ("Group_c4.view", (0, 1, 2)[arg])
        hx.anim_speed ("Group_c5.view", (0, 1, 2)[arg])
        hx.anim_speed ("Group_c6.view", (0, 1, 2)[arg])
        hx.anim_speed ("Group_c7.view", (0, 1, 2)[arg])

        hx.anim_speed ("Group_d1.view", (0, 1, 2)[arg])
        hx.anim_speed ("Group_d2.view", (0, 1, 2)[arg])
        hx.anim_speed ("Group_d3.view", (0, 1, 2)[arg])
        hx.anim_speed ("Group_d4.view", (0, 1, 2)[arg])

        hx.anim_speed ("pattern05.matAnim", (0, 2, 4)[arg])

	hx.anim_minmax ("A_objects.matAnim", (200,0,400)[arg], (300,100,1600)[arg])
	hx.anim_minmax ("translucent_blue.matAnim", (200,0,400)[arg], (300,100,1600)[arg])
	hx.anim_minmax ("translucent_orange.matAnim", (200,0,400)[arg], (300,100,1600)[arg])
	hx.anim_minmax ("translucent_pink.matAnim", (200,0,400)[arg], (300,100,1600)[arg])
	hx.anim_minmax ("translucent_red.matAnim", (200,0,400)[arg], (300,100,1600)[arg])

def get_arena_class_name ():
    return GlasArena
