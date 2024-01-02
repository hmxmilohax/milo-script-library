# This file is loaded in the Tnl::Renderer ctor

class ConstArena (Arena):
    def __init__ (self):
        self.directory_name = 'Const'

    def get_name (self):        return "Constructo"



def get_arena_class_name ():
    return ConstArena
