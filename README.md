# Milo Script Library

This is a repository for the raw scripts in as many Harmonix titles as we have ripped and available to us. Usually these scripts are in Harmonix's homebrew Lisp-like Data Array language, though *FreQuency*, their earliest title, used Python 1 instead. (The name "Milo" refers to the name Harmonix themselves gave their game engine. Nearly all of their games share the same engine with upgrades and improvements made over time.)

Some games (namely *Rock Band* for the PS2 and the *Amplitude* PS2 OPM demo) feature these scripts in their raw DTA format, and thus contain Harmonix's original comments, an invaluable insight into their development process. Most other games have had their DTBs (the tokenized and encrypted script format the game actually reads) converted to DTA; these are therefore missing comments.

## Extraction status
Here are some tables for games that fit within our scope and where they're at as far as being added to the repo. **Extracted** means they're in the repo, **Available** means we have them, but they're not yet added, and **Not available** means we don't have raw scripts for that game, usually because they haven't yet been cracked or because no one has a dump of the disc.

### Official Releases
| Game | Platform | Script Format | Status |
| ---- | -------- | ------------- | ------ |
| **FreQuency** | PS2 | Known (Python 1) | Extracted |
| **Amplitude** | PS2 | Unknown | Not available |
| **Karaoke Revolution** | PS2<br>Xbox | Unknown<br>Known (DTA) | Not available<br>Available |
| **Karaoke Revolution Volume 2** | PS2 | TBD | TBD |
| **Karaoke Revolution Volume 3** | PS2 | TBD | TBD |
| **Karaoke Revolution Party** | PS2<br>Gamecube<br>Xbox | Known (old-style DTB) | Available<br>Available<br>Available |
| **Eyetoy: Antigrav** | PS2 | TBD | TBD |
| **Guitar Hero** | PS2 | Known (DTB) | Extracted |
| **Guitar Hero II** | PS2<br>Xbox 360 | Known (old-style DTB)<br>Known (new-style DTB) | Extracted<br>Available |
| **Guitar Hero Encore: Rocks the 80's** | PS2 | Known (old-style DTB) | Extracted |
| **Rock Band** | PS2<br>PS3<br>Xbox 360<br>Wii | Known (PS2 uses old-<br>style DTB, all others<br>use new-style DTB)<br>*(DTAs for the<br>PS2 version available)* | Extracted<br>Available<br>Available<br>Available |
| **Rock Band Track Pack Volume 1** | PS2<br>Wii | Known (PS2 uses old-<br>style DTB, all others<br>use new-style DTB) | Extracted<br>Available |
| **AC/DC Live: Rock Band Track Pack** | PS2<br>PS3<br>Xbox 360<br>Wii | Known (PS2 uses old-<br>style DTB, all others<br>use new-style DTB) | Available<br>Available<br>Available<br>Available |
| **Rock Band Track Pack Volume 2** | PS2<br>PS3<br>Xbox 360<br>Wii | Known (PS2 uses old-<br>style DTB, all others<br>use new-style DTB) | Extracted<br>Available |
| **Rock Band Track Pack: Classic Rock** | PS2<br>PS3<br>Xbox 360<br>Wii | Known (PS2 uses old-<br>style DTB, all others<br>use new-style DTB) | Available<br>Available<br>Available<br>Available |
| **Rock Band Country Track Pack** | PS2<br>PS3<br>Xbox 360<br>Wii | Known (PS2 uses old-<br>style DTB, all others<br>use new-style DTB) | Available<br>Available<br>Available<br>Available |
| **Rock Band Metal Track Pack** | PS2<br>PS3<br>Xbox 360<br>Wii | Known (PS2 uses old-<br>style DTB, all others<br>use new-style DTB) | Available<br>Available<br>Available<br>Available |
| **Rock Band Country Track Pack 2** | PS3<br>Xbox 360<br>Wii | Known (new-style DTB) | Available<br>Available<br>Available |
| **Rock Band 2** | PS2<br>PS3<br>Xbox 360<br>Wii | Known (new-style DTB) | Available<br>Available<br>Available<br>Available |
| **Lego Rock Band** | PS3<br>Xbox 360<br>Wii | Known (new-style DTB) | Available<br>Available<br>Available |
| **The Beatles: Rock Band** | PS3<br>Xbox 360<br>Wii | Known (new-style DTB) | Available<br>Available<br>Available |
| **Green Day: Rock Band** | PS3<br>Xbox 360<br>Wii | Known (new-style DTB) | Available<br>Available<br>Available |
| **Rock Band 3** | PS3<br>Xbox 360<br>Wii | Known (new-style DTB) | Available<br>Available<br>Available |
| **Rock Band Blitz** | PS3<br>Xbox 360 | Known (new-style DTB) | Available<br>Available |

### Prototypes and Demos
| Game | Build | Platform | Script Format | Status |
| ---- | ----- | -------- | ------------- | ------ |
| **FreQuency** | R179 prototype | PS2 | Known (Python) | Extracted |
| **Amplitude** | OPM prototype | PS2 | Known (DTA) | Extracted |
| **Amplitude** | Deluge prototype | PS2 | Unknown | Not available |
| **Amplitude** | Space demo | PS2 | Unknown | Not available |
| **Karaoke Revolution** | Deluge prototype 1 | PS2 | Unknown | Not available |
| **Karaoke Revolution** | Deluge prototype 2 | PS2 | Unknown | Not available |
| **Karaoke Revolution** | Deluge prototype 3 | PS2 | Unknown | Not available |
| **Karaoke Revolution Volume 2** | Deluge prototype 1 | PS2 | TBD | TBD |
| **Karaoke Revolution Volume 2** | Deluge prototype 2 | PS2 | TBD | TBD |
| **Karaoke Revolution Volume 3** | Deluge prototype | PS2 | TBD | TBD |
| **Karaoke Revolution Party** | Deluge prototype | PS2 | Known (old-style DTB) | Available |
| **Guitar Hero** | Deluge prototype | PS2 | Known (old-style DTB) | Extracted |
| **Guitar Hero II** | OPM prototype | PS2 | Known (old-style DTB) | Extracted |
| **Guitar Hero II** | Retail prototype | PS2 | Known (old-style DTB) | Extracted |
| **Guitar Hero Encore: Rocks the 80's** | Deluge prototype | PS2 | Known (old-style DTB) | Extracted |

These tables are not exhaustive. Harmonix released many games and many updates for those games, so this is subject to change and addition as the time goes on. Please let me know about omissions.