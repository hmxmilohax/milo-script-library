# This file is loaded in the Tnl::Renderer ctor

# Once more of Python interfaces with Rnd, this file can implement
# database loading and arena-specific customizations

class NoodleArena (Arena):
    def __init__ (self):
        pass


def get_arena_class_name ():
    return NoodleArena
