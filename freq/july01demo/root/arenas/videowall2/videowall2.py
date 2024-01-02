# This file is loaded in the Tnl::Renderer ctor

class VideoWallArena (Arena):
   meshesTracks = []
   meshesBars = []
   slTracks = []
   slBars = []
   numTracks = 8
   numBars = 16
   numBarsInSection = 8
   numPhysSections = 2
   numLogSections = 4
   loopBar = 16
   someChase = 0
   numChase = 2
   oldLogSection = 0
   currLogSection = 0
   currPhysSection = 0
   tunnel = None
   matChase = []
   movieNames = ["movie1.mat","movie2.mat","movie3.mat","movie4.mat",
      "movie5.mat","movie6.mat","movie7.mat","movie8.mat"]
   chaseNames = ["chase1.mat","chase2.mat"]
   vidtunn_style = 'ring'     # 'track' or 'ring' (or default 'random')

   def __init__ (self):
      pass

# on_key_down() handles the following keys:

   def on_key_down(self, key):

      self.someChase = (self.someChase + 1) % self.numChase;

      if key == 116:  #f5: send a movie quickly down all tracks
         bar = self.tunnel.bar % self.numBars
         for i in range(0, self.tunnel.numtracks):
            self.slTracks[i].addoverridecycle(self.matChase[self.someChase],110,100,bar,1,1)
         return

      if key == 117:  #f6: send a movie slowly down all tracks
         bar = self.tunnel.bar % self.numBars
         for i in range(0, self.tunnel.numtracks):
            self.slTracks[i].addoverridecycle(self.matChase[self.someChase],110,300,bar,1,1)
         return

      if key == 118:  #f7: send a movie quickly down all tracks, towards you
         bar = (self.tunnel.bar + 15) % self.tunnel.numbars
         for i in range(0, self.tunnel.numtracks):
            self.slTracks[i].addoverridecycle(self.matChase[self.someChase],110,100,bar,-1,1)
         return

      if key == 119:  #f8: send a movie slowly down all tracks, towards you
         bar = (self.tunnel.bar + 15) % self.tunnel.numbars
         for i in range(0, self.tunnel.numtracks):
            self.slTracks[i].addoverridecycle(self.matChase[self.someChase],110,300,bar,-1,1)
         return

      if key == 120:  # f9: do a few loops in the bars ahead
         bar1 = (self.tunnel.bar + 1) % self.numBars
         bar2 = (bar1 + 1) % self.numBars
         bar3 = (bar2 + 1) % self.numBars
         self.slBars[bar1].addoverridecycle(self.matChase[1],120,100,0,1,10)
         self.slBars[bar1].addoverridecycle(self.matChase[1],120,100,1,1,10)
         self.slBars[bar1].addoverridecycle(self.matChase[1],120,100,2,1,10)
         self.slBars[bar2].addoverridecycle(self.matChase[1],120,200,3,-1,10)
         self.slBars[bar2].addoverridecycle(self.matChase[1],120,200,4,-1,10)
         self.slBars[bar2].addoverridecycle(self.matChase[1],120,200,5,-1,10)
         self.slBars[bar3].addoverridecycle(self.matChase[1],120,100,6,1,10)
         self.slBars[bar3].addoverridecycle(self.matChase[1],120,100,7,1,10)
         self.slBars[bar3].addoverridecycle(self.matChase[1],120,100,0,1,10)
         return

# on_game_begin() calls the setup routine which initializes the videowall.

   def on_game_begin (self):
      self.setup()


   def setbasemats(self, physsect, matname):
      startbar = physsect * self.numBarsInSection
      endbar = startbar + self.numBarsInSection
      self.tunnel.setbarpowerupblock(startbar, endbar, matname)

# setbasematsaround() sets the base repeating materials in the tunnel, implemented
# with each group going around a concentric ring.

   def setbasematsaround(self, physsect):
      startbar = physsect * self.numBarsInSection
      endbar = startbar + self.numBarsInSection
      imat = 0
      for bar in range(startbar, endbar):
         self.tunnel.setbarpowerupblock(bar, bar+1, self.movieNames[imat])
         imat = (imat + 1) % len(self.movieNames)

# setbasematsdown() sets the base repeating materials in the tunnel, implemented
# with each group going down the tunnel.

   def setbasematsdown(self, physsect):
      startbar = physsect * self.numBarsInSection
      endbar = startbar + self.numBarsInSection
      imat = 0
      for track in range(0, self.numTracks):
         self.tunnel.setbarpowerupblocktrack(track, startbar, endbar, self.movieNames[imat])
         imat = (imat + 1) % len(self.movieNames)

# setrandbasemats() makes a random starting set of mats in the tunnel.

   def setrandbasemats(self, physsect):
      startbar = physsect * self.numBarsInSection
      endbar = startbar + self.numBarsInSection
      self.tunnel.setrandombarpowerupblock(startbar, endbar, self.movieNames)

# willadvancesection() is called ahead of time when it is known or surmised
# that the next section will or will not advance (called on up-button click in
# single player, called automatically in multi-player).  It rewrites the next
# physical section of tunnel with either the same or the next logical material.

   def willadvancesection(self, adv):
      pass

# advancesection() is called when a section boundary is actually crossed.  In
# this case, all we have to do is set the now-passed physical section to the
# "new" material, and advance the physical section.

   def advancesection(self, adv):
      pass

# set_effect() is called when an effect is laid down

   def set_effect(self, track, ieffect, onoff):
      pass

# effects_off() turns off all effects on a track/section

   def effects_off(self, track):
      pass

# buildscreenlists() builds the lists of screenlists

   def buildscreenlists(self):
      self.slTracks = []
      for track in range(0, self.numTracks):
         name = 'slTracks_' + str(track)
         sl = rpm.newscreenlist(name)
         sl.addscreentunnel(self.tunnel, track, range(0, self.loopBar))
         self.slTracks.append(sl)
      self.slBars = []
      for bar in range(0, self.loopBar):
         name = 'slBars_' + str(bar)
         sl = rpm.newscreenlist(name)
         sl.addscreentunnel(self.tunnel, range(0, self.numTracks), bar)
         self.slBars.append(sl)

# setup sets the base materials and builds the screenlists

   def setup(self):
      import rpm
      self.tunnel = rpm.findtunnel("videowall")
      self.matChase.append(rpm.findmat(self.chaseNames[0]))
      self.matChase.append(rpm.findmat(self.chaseNames[1]))
      if self.vidtunn_style == 'ring':
         self.setbasematsaround(0)
         self.setbasematsaround(1)
      elif self.vidtunn_style == 'track':
         self.setbasematsdown(0)
         self.setbasematsdown(1)
      else:
         self.setrandbasemats(0)
         self.setrandbasemats(1)
      self.currPhysSection = 0
      self.currLogSection = 0
      self.oldLogSection = 0
      rpm.setscreenlistanimparent("videowall")
      self.buildscreenlists()

def get_arena_class_name ():
   return VideoWallArena
