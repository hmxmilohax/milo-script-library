class ConstructoMultiArena (Arena):
    def __init__ (self):
        self.directory_name = 'const_multi'

    def available_in (self, community):
        if community == 'local':
            return 1
        else:
            return 0

    def get_name (self):        return "Constructo"
    def get_arena_id (self):    return 12          # Unique id for this arena

def get_arena_class_name ():
    return ConstructoMultiArena
