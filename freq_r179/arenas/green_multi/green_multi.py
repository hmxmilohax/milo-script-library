class GreenMultiArena (Arena):
    def __init__ (self):
        self.directory_name = 'green_multi'

    def available_in (self, community):
        if community == 'local':
            return 1
        else:
            return 0

    def get_name (self):        return "Green Obelisk"
    def get_arena_id (self):    return 16          # Unique id for this arena

    # arg is: 0 - bad, 1 - good, 2 - great
    def on_health (self, arg):
        if (arg > 2): arg = 2

        hx.anim_speed ("roto_controllers.view", (0, 1, 2)[arg])
        hx.anim_speed ("matanim.view", (0, 1, 2)[arg])

	hx.anim_minmax ("matanim.view", (70000, 0, 85000)[arg], (80000, 61440, 90000)[arg])

def get_arena_class_name ():
    return GreenMultiArena
