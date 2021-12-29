# This file is loaded in the Tnl::Renderer ctor

class BlueArena (Arena):
    def __init__ (self):
        self.directory_name = 'blue'

    def get_name (self):        return "Blue Pylon"
    def get_arena_id (self):    return 1          # Unique id for this arena

    # arg is: 0 - bad, 1 - good, 2 - great
    def on_health (self, arg):
        if (arg > 2): arg = 2
        
        hx.anim_speed ("sleeve_01.view", (0, 1, 2)[arg])
        hx.anim_speed ("sleeve_02.view", (0, 1, 2)[arg])
        hx.anim_speed ("sleeve_07.view", (0, 1, 3)[arg])
        hx.anim_speed ("sleeve_08.view", (0, 1, 2.5)[arg])
        hx.anim_speed ("sleeve_04.view", (0, 1, 3)[arg])
        hx.anim_speed ("swirl.view", (.25, 1, 1)[arg])
        hx.anim_speed ("meshgens.view", (0, .5, 1.5)[arg])
        hx.anim_speed ("particle_system.view", (.25, .75, .75)[arg])
        hx.anim_speed ("camlight.tnm", (0, 8, 16)[arg])

        hx.anim_speed ("blue_alpha.mnm", (6, 30, 40)[arg])
        hx.anim_speed ("red_alpha.mnm", (6, 30, 50)[arg])
        hx.anim_speed ("yellow_alpha.mnm", (6, 35, 50)[arg])        
	hx.anim_speed ("blue_opaque.mnm", (4, 35, 50)[arg])
        hx.anim_speed ("red_opaque.mnm", (4, 30, 50)[arg])
        hx.anim_speed ("yellow_opaque.mnm", (4, 35, 50)[arg])
        hx.anim_speed ("spectrum.mnm", (4, 6, 20)[arg])
        hx.anim_speed ("camlight.lnm", (1, 6, 12)[arg])

	hx.anim_minmax ("camlight.lnm", (70000, 0, 90000)[arg], (85000, 61440, 100000)[arg])
	hx.anim_minmax ("camlight.tnm", (70000, 0, 0)[arg], (85000, 61440, 61440)[arg])
	hx.anim_minmax ("red_alpha.mnm", (70000, 0, 0)[arg], (85000, 61440, 61440)[arg])
	hx.anim_minmax ("blue_alpha.mnm", (70000, 0, 0)[arg], (85000, 61440, 61440)[arg])
	hx.anim_minmax ("yellow_alpha.mnm", (70000, 0, 0)[arg], (85000, 61440, 61440)[arg])
	hx.anim_minmax ("red_opaque.mnm", (70000, 0, 0)[arg], (85000, 61440, 61440)[arg])
	hx.anim_minmax ("blue_opaque.mnm", (70000, 0, 0)[arg], (85000, 61440, 61440)[arg])
	hx.anim_minmax ("yellow_opaque.mnm", (70000, 0, 0)[arg], (85000, 61440, 61440)[arg])
	hx.anim_minmax ("spectrum.mnm", (70000, 0, 0)[arg], (85000, 61440, 61440)[arg])

    # example: 
    #def on_health (self, arg):
    #    hx.anim_speed ("sleeve_01.view", arg)
    #    hx.anim_speed ("sleeve_02.view", arg)
    #    if arg == 0:
    #        hx.anim_offset ("outer.litanim", 0)
    #    else:
    #        hx.anim_offset ("outer.litanim", 100)
        
def get_arena_class_name ():
    return BlueArena
