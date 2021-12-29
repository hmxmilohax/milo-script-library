class CarnArena (Arena):
    def __init__ (self):
        self.directory_name = 'carn'

    def get_name (self):        return "VR.Tex"
    def get_arena_id (self):    return 6          # Unique id for this arena

def get_arena_class_name ():
    return CarnArena

    # arg is: 0 - bad, 1 - good, 2 - great
    def on_health (self, arg):
        if (arg > 2): arg = 2
        
        hx.anim_speed ("Group_BigTv's.tnm", (0, 1, 2)[arg])
        hx.anim_speed ("Group_BigTv's01.tnm", (0, 1, 2)[arg])
        hx.anim_speed ("Group_a.view", (.1, 1, 2)[arg])
        hx.anim_speed ("Group_b.view", (.2, 1, 2)[arg])
        hx.anim_speed ("Group_c.view", (.2, 1, 2)[arg])
        hx.anim_speed ("Group_d.view", (.2, 1, 2)[arg])

        
    # example: 
    #def on_health (self, arg):
    #    hx.anim_speed ("sleeve_01.view", arg)
    #    hx.anim_speed ("sleeve_02.view", arg)
    #    if arg == 0:
    #        hx.anim_offset ("outer.litanim", 0)
    #    else:
    #        hx.anim_offset ("outer.litanim", 100)
