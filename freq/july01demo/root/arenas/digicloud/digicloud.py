# This file is loaded in the Tnl::Renderer ctor

class DigiArena (Arena):
    def __init__ (self):
        self.directory_name = 'DigiCloud'

    def get_name (self):        return "Red DigiClouds"



def get_arena_class_name ():
    return DigiArena
