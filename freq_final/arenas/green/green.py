class GreenArena (Arena):
    def __init__ (self):
        self.directory_name = 'green'

    def get_name (self):        return "Green Obelisk"
    def get_arena_id (self):    return 3          # Unique id for this arena

    # arg is: 0 - bad, 1 - good, 2 - great
    def on_health (self, arg):
        if (arg > 2): arg = 2
        
        hx.anim_speed ("sleeve_01.view", (0, 1, 2)[arg])
        hx.anim_speed ("sleeve_02.view", (0, 1, 2)[arg])
        hx.anim_speed ("sleeve_06.view", (0, 1, 1.5)[arg])
        hx.anim_speed ("sleeve_11.view", (0, 1, 2)[arg])
        hx.anim_speed ("sleeve_12.view", (0, 1, 2)[arg])
        hx.anim_speed ("sleeve_13.view", (0, 1, 2)[arg])
        hx.anim_speed ("sleeve_14.view", (0, 1, 2)[arg])
        hx.anim_speed ("roto_controllers.view", (0, 1, 2)[arg])
        hx.anim_speed ("matanim.view", (0, 1, 2)[arg])
        hx.anim_speed ("particles.view", (0, .5, 1)[arg])
        hx.anim_speed ("particles_2.view", (0, .5, 1)[arg])
        hx.anim_speed ("mgen_01.view", (0, 1, 1.25)[arg])
        hx.anim_speed ("mgen_02.view", (0, 1, 1.25)[arg])

	hx.anim_minmax ("matanim.view", (70000, 0, 85000)[arg], (80000, 61440, 90000)[arg])

    # example: 
    #def on_health (self, arg):
    #    hx.anim_speed ("sleeve_01.view", arg)
    #    hx.anim_speed ("sleeve_02.view", arg)
    #    if arg == 0:
    #        hx.anim_offset ("outer.litanim", 0)
    #    else:
    #        hx.anim_offset ("outer.litanim", 100)

def get_arena_class_name ():
    return GreenArena
