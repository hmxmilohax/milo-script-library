class BlueMultiArena (Arena):
    def __init__ (self):
        self.directory_name = 'blue_multi'

    def available_in (self, community):
        if community == 'local':
            return 1
        else:
            return 0

    def get_name (self):        return "Blue Pylon"
    def get_arena_id (self):    return 11          # Unique id for this arena

    # arg is: 0 - bad, 1 - good, 2 - great
    def on_health (self, arg):
        if (arg > 2): arg = 2


        hx.anim_speed ("camlight.tnm", (0, 10, 20)[arg])

 	hx.anim_speed ("blue_opaque.mnm", (4, 35, 70)[arg])
        hx.anim_speed ("red_opaque.mnm", (4, 30, 90)[arg])
        hx.anim_speed ("yellow_opaque.mnm", (4, 35, 105)[arg])
        hx.anim_speed ("spectrum.mnm", (4, 6, 150)[arg])
        hx.anim_speed ("camlight.lnm", (1, 10, 14)[arg])

	hx.anim_minmax ("camlight.lnm", (70000, 0, 90000)[arg], (85000, 61440, 100000)[arg])
	hx.anim_minmax ("camlight.tnm", (70000, 0, 0)[arg], (85000, 61440, 61440)[arg])
	hx.anim_minmax ("red_opaque.mnm", (70000, 0, 0)[arg], (85000, 61440, 61440)[arg])
	hx.anim_minmax ("blue_opaque.mnm", (70000, 0, 0)[arg], (85000, 61440, 61440)[arg])
	hx.anim_minmax ("yellow_opaque.mnm", (70000, 0, 0)[arg], (85000, 61440, 61440)[arg])
	hx.anim_minmax ("spectrum.mnm", (70000, 0, 0)[arg], (85000, 61440, 61440)[arg])

def get_arena_class_name ():
    return BlueMultiArena
