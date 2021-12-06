class WallArena (Arena):
    def __init__ (self):
        self.directory_name = 'wall'

    def get_name (self):        return "VideoWall"
    def get_arena_id (self):    return 8          # Unique id for this arena

def get_arena_class_name ():
    return WallArena
