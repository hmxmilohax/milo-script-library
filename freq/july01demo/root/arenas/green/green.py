# This file is loaded in the Tnl::Renderer ctor

class GreenArena (Arena):
    def __init__ (self):
        self.directory_name = 'Green'

    def get_name (self):        return "Green Obelisk"



def get_arena_class_name ():
    return GreenArena
