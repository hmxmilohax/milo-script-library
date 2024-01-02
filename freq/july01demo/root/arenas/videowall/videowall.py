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
   someTrack = 0
   oldLogSection = 0
   currLogSection = 0
   currPhysSection = 0
   tunnel = None
   matChaser = None
   sectionMatNames = ["section1.mat","section2.mat"]
   matNames = ["wall1.mat","wall2.mat","wall3.mat","wall4.mat"]

   def __init__ (self):
      pass

# on_key_down() handles the following keys:
#
# F5 - fire a chaser down a track

   def on_key_down(self, key):

      if key == 116:  #f5
#         bar = self.tunnel.bar % self.tunnel.numbars
#         self.slTracks[self.someTrack].addoverridecycle(self.matChaser,110,100,bar,1)
#         self.someTrack = self.someTrack + 3
#         if self.someTrack >= self.numTracks:
#             self.someTrack = self.someTrack - self.numTracks
         return

# on_game_begin() calls the setup routine which initializes the videowall.

   def on_game_begin (self):
      self.setup()
#      hx.post_script(960, "current_level.arena.setup()")

# setbasemats() sets the base repeating materials in the tunnel.  They are
# implemented as powerups (the screen mechanism then overlays on this same
# powerup mechanism.

   def setbasemats(self, physsect, matname):
      startbar = physsect * self.numBarsInSection
      endbar = startbar + self.numBarsInSection
      self.tunnel.setbarpowerupblock(startbar, endbar, matname)

# willadvancesection() is called ahead of time when it is known or surmised
# that the next section will or will not advance (called on up-button click in
# single player, called automatically in multi-player).  It rewrites the next
# physical section of tunnel with either the same or the next logical material.

   def willadvancesection(self, adv):
      if adv > 0:
         self.currLogSection = (self.oldLogSection + 1) % self.numLogSections
      else:
         self.currLogSection = self.oldLogSection
      nextPhys = (self.currPhysSection + 1) % self.numPhysSections
      rpm.copyovermat(self.sectionMatNames[nextPhys], self.matNames[self.currLogSection])
      hx.videowall_program_section(nextPhys, self.currLogSection)

# advancesection() is called when a section boundary is actually crossed.  In
# this case, all we have to do is set the now-passed physical section to the
# "new" material, and advance the physical section.

   def advancesection(self, adv):
      rpm.copyovermat(self.sectionMatNames[self.currPhysSection], self.matNames[self.currLogSection])
      hx.videowall_program_section(self.currPhysSection, self.currLogSection)
      self.currPhysSection = (self.currPhysSection + 1) % self.numPhysSections
      self.oldLogSection = self.currLogSection

# set_effect() is called when an effect is laid down

   def set_effect(self, track, ieffect, onoff):
      pass
#      hx.videowall_set_effect(self.oldLogSection, track, ieffect, onoff);
#      hx.videowall_program_section(self.currPhysSection, self.oldLogSection);
#      if self.oldLogSection == self.currLogSection:
#         nextPhys = (self.currPhysSection + 1) % self.numPhysSections
#         hx.videowall_program_section(nextPhys, self.currLogSection)

# effects_off() turns off all effects on a track/section

   def effects_off(self, track):
      pass
#      hx.videowall_effects_off(self.oldLogSection, track)
#      hx.videowall_program_section(self.currPhysSection, self.oldLogSection)
#      if self.oldLogSection == self.currLogSection:
#         nextPhys = (self.currPhysSection + 1) % self.numPhysSections
#         hx.videowall_program_section(nextPhys, self.currLogSection)

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
      self.matChaser = rpm.findmat("chaser.mat")
      rpm.copyovermat("section1.mat","wall1.mat")
      rpm.copyovermat("section2.mat","wall1.mat")
      self.setbasemats(0, "section1.mat")
      self.setbasemats(1, "section2.mat")
      self.currPhysSection = 0
      self.currLogSection = 0
      self.oldLogSection = 0
      rpm.setscreenlistanimparent("videowall")
      self.buildscreenlists()
      hx.videowall_create("videowall")
      hx.videowall_setmat(0, "fx_echo.mat")
      hx.videowall_setmat(1, "fx_volume.mat")
      hx.videowall_setmat(2, "fx_wah.mat")
      hx.videowall_setmat(3, "fx_chorus.mat")
#      self.slBars[0].addoverridecycle(self.matChaser,100,100,0,0)
#      self.slBars[2].addoverridecycle(self.matChaser,100,50,0,0)
#      self.slBars[4].addoverridecycle(self.matChaser,100,100,0,0)
#      self.slBars[6].addoverridecycle(self.matChaser,100,50,0,0)
#      self.slBars[8].addoverridecycle(self.matChaser,100,150,0,0)
#      self.slBars[10].addoverridecycle(self.matChaser,100,75,0,0)
#      self.slBars[12].addoverridecycle(self.matChaser,100,150,0,0)
#      self.slBars[14].addoverridecycle(self.matChaser,100,75,0,0)

#   def changemat(self,dt):
#      hx.post_script(hx.clock('tick') + dt, "current_level.arena.changemat(9600)")

def get_arena_class_name ():
   return VideoWallArena
