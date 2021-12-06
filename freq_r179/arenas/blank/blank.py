# This file is loaded in the Tnl::Renderer ctor

class BlankArena (Arena):
    def __init__ (self):
        self.directory_name = 'blank'

    def get_name (self):        return "No Arena"
    def get_arena_id (self):    return 9          # Unique id for this arena

        
    def available_in (self, community):
            return 1

def get_arena_class_name ():
    return BlankArena
