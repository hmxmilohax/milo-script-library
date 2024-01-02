# This file is loaded in the Tnl::Renderer ctor

class BlueArena (Arena):
    def __init__ (self):
        self.directory_name = 'Blue'

    def get_name (self):        return "Blue Pylon"



def get_arena_class_name ():
    return BlueArena
