# This file is loaded in the Tnl::Renderer ctor

class ParaArena (Arena):
    def __init__ (self):
        self.directory_name = 'para'

    def get_name (self):        return "Parallaxia"
    def get_arena_id (self):    return 7          # Unique id for this arena

# arg is: 0 - bad, 1 - good, 2 - great
    def on_health (self, arg):
        if (arg > 2): arg = 2
                
        hx.anim_speed ("blue_shaded.mnm", (4, 20, 50)[arg])
        hx.anim_speed ("green_shaded.mnm", (4, 15, 30)[arg])
	hx.anim_speed ("purple_shaded.mnm", (3, 24, 30)[arg])
	hx.anim_speed ("purple_cube.mnm", (3, 24, 30)[arg])
        hx.anim_speed ("panelmap_p.mnm", (.5, 16, 30)[arg])
        hx.anim_speed ("panelmap_b.mnm", (2, 16, 30)[arg])
        hx.anim_speed ("portal_lanternfloor.mnm", (3, 16, 30)[arg])
        hx.anim_speed ("portal_lanternbase.mnm", (3, 16, 30)[arg])
        hx.anim_speed ("redsphere.mnm", (0, 25, 50)[arg])
        hx.anim_speed ("outer_01.lnm", (6, 30, 50)[arg])
	hx.anim_speed ("outer_01.tnm", (4, 12, 24)[arg])
        
	hx.anim_speed ("4_portal_01.view", (.05, 1, 6)[arg])
        hx.anim_speed ("4_portal_02.view", (.05, 1, 6)[arg])
        hx.anim_speed ("4_portal_03.view", (.05, 1, 6)[arg])
        hx.anim_speed ("4_portal_04.view", (.05, 1, 6)[arg])

	hx.anim_minmax ("outer_01.lnm", (70000, 0, 0)[arg], (85000, 61440, 61440)[arg])
	hx.anim_minmax ("blue_shaded.mnm", (70000, 0, 0)[arg], (85000, 61440, 61440)[arg])
	hx.anim_minmax ("green_shaded.mnm", (70000, 0, 0)[arg], (85000, 61440, 61440)[arg])
	hx.anim_minmax ("purple_shaded.mnm", (70000, 0, 0)[arg], (85000, 61440, 61440)[arg])
	hx.anim_minmax ("purple_cube.mnm", (70000, 0, 0)[arg], (85000, 61440, 61440)[arg])
	hx.anim_minmax ("panelmap_b.mnm", (70000, 0, 0)[arg], (85000, 61440, 61440)[arg])
	hx.anim_minmax ("panelmap_p.mnm", (70000, 0, 0)[arg], (85000, 61440, 61440)[arg])
	hx.anim_minmax ("circ_purple_alpha.mnm", (70000, 0, 0)[arg], (85000, 61440, 61440)[arg])
	hx.anim_minmax ("circ_mod_alpha.mnm", (70000, 0, 0)[arg], (85000, 61440, 61440)[arg])
	hx.anim_minmax ("circ_green_alpha.mnm", (70000, 0, 0)[arg], (85000, 61440, 61440)[arg])
	hx.anim_minmax ("redsphere.mnm", (70000, 0, 0)[arg], (85000, 61440, 61440)[arg])

    # example: 
    #def on_health (self, arg):
    #    hx.anim_speed ("sleeve_01.view", arg)
    #    hx.anim_speed ("sleeve_02.view", arg)
    #    if arg == 0:
    #        hx.anim_offset ("outer.litanim", 0)
    #    else:
    #        hx.anim_offset ("outer.litanim", 100)


def get_arena_class_name ():
    return ParaArena
