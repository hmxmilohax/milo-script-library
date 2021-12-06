class WallMultiArena (Arena):
    def __init__ (self):
        self.directory_name = 'wall_multi'

    def available_in (self, community):
        if community == 'local':
            return 1
        else:
            return 0

    def get_name (self):        return "VideoWall"
    def get_arena_id (self):    return 17          # Unique id for this arena

def get_arena_class_name ():
    return WallMultiArena
