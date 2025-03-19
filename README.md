# Milo Script Library

This is a repository for the raw scripts in as many Harmonix titles as we have ripped and available to us. Usually these scripts are in Harmonix's homebrew Lisp-like Data Array language, though *FreQuency*, their earliest title, used Python 1 instead. (The name "Milo" refers to the name Harmonix themselves gave their game engine. Nearly all of their games share the same engine with upgrades and improvements made over time.)

Some games (namely *Rock Band* for the PS2 and the *Amplitude* PS2 OPM demo) feature these scripts in their raw DTA format, and thus contain Harmonix's original comments, an invaluable insight into their development process. Most other games have had their DTBs (the tokenized and encrypted script format the game actually reads) converted to DTA; these are therefore missing comments.

If you need this stuff, you should also join the MiloHax Discord, where people can help you out and we can all chat about modding Milo and whatnot: https://discord.gg/WWmsQvHSC6

## Extraction status
Here are some tables for games that fit within our scope and where they're at as far as being added to the repo. :white_check_mark: means they're in the repo, :x: means we have them, but they're not yet added, and :heavy_minus_sign: means we don't have raw scripts for that game, usually because the file formats haven't yet been cracked.

### Official Releases
| Game | Platform | Script Format | Status |
| ---- | -------- | ------------- | ------ |
| **FreQuency** | PS2 | Known (Python 1) | :white_check_mark: |
| **Amplitude 2003** | PS2 | Known (Amp-style DTB) | :white_check_mark: |
| **Karaoke Revolution** | PS2<br>Xbox | Unknown<br>Known (Raw DTA) | :x:<br>:white_check_mark: |
| **Karaoke Revolution Volume 2** | PS2 | Unknown | :heavy_minus_sign: |
| **Karaoke Revolution Volume 3** | PS2 | Unknown | :heavy_minus_sign: |
| **Eyetoy: Antigrav** | PS2 | TBD | :x: |
| **Karaoke Revolution Party** | PS2<br>Gamecube<br>Xbox | Known (old-style DTB) | :white_check_mark:<br>:white_check_mark:<br>:heavy_minus_sign: |
| **Guitar Hero** | PS2 | Known (old-style DTB) | :white_check_mark: |
| **Guitar Hero II** | PS2<br>Xbox 360 | Known (old-style DTB)<br>Known (new-style DTB) | :white_check_mark:<br>:white_check_mark: |
| **Guitar Hero Encore: Rocks the 80's** | PS2 | Known (old-style DTB) | :white_check_mark: |
| **Phase** | iPod | Known (old-style DTB) | :white_check_mark: |
| **Rock Band** | PS2<br>PS3<br>Xbox 360<br>Wii | Known (PS2 uses old-<br>style DTB and has raw DTA, all others<br>use new-style DTB) | :white_check_mark:<br>:white_check_mark:<br>:white_check_mark:<br>:white_check_mark: |
| **Rock Band Track Pack Volume 1** | PS2<br>Wii | Known (PS2 uses old-<br>style DTB, all others<br>use new-style DTB) | :white_check_mark:<br>:white_check_mark: |
| **Rock Band 2** | PS2<br>PS3<br>Xbox 360<br>Wii | Known (PS2 uses old-<br>style DTB, all others<br>use new-style DTB) | :white_check_mark:<br>:white_check_mark:<br>:white_check_mark:<br>:white_check_mark: |
| **AC/DC Live: Rock Band Track Pack** | PS2<br>PS3<br>Xbox 360<br>Wii | Known (PS2 uses old-<br>style DTB, all others<br>use new-style DTB) | :white_check_mark:<br>:x:<br>:x:<br>:x: |
| **Rock Band Track Pack Volume 2** | PS2<br>PS3<br>Xbox 360<br>Wii | Known (PS2 uses old-<br>style DTB, all others<br>use new-style DTB) | :white_check_mark:<br>:x:<br>:x:<br>:white_check_mark: |
| **Rock Band Track Pack: Classic Rock** | PS2<br>PS3<br>Xbox 360<br>Wii | Known (PS2 uses old-<br>style DTB, all others<br>use new-style DTB) | :white_check_mark:<br>:x:<br>:x:<br>:white_check_mark: |
| **Rock Band Country Track Pack** | PS2<br>PS3<br>Xbox 360<br>Wii | Known (PS2 uses old-<br>style DTB, all others<br>use new-style DTB) | :white_check_mark:<br>:x:<br>:x:<br>:white_check_mark: |
| **The Beatles: Rock Band** | PS3<br>Xbox 360<br>Wii | Known (new-style DTB) | :white_check_mark:<br>:white_check_mark:<br>:white_check_mark: |
| **Rock Band Metal Track Pack** | PS2<br>PS3<br>Xbox 360<br>Wii | Known (PS2 uses old-<br>style DTB, all others<br>use new-style DTB) | :white_check_mark:<br>:x:<br>:x:<br>:white_check_mark: |
| **Lego Rock Band** | PS3<br>Xbox 360<br>Wii | Known (new-style DTB) | :white_check_mark:<br>:x:<br>:x: |
| **Green Day: Rock Band** | PS3<br>Xbox 360<br>Wii | Known (new-style DTB) | :white_check_mark:<br>:white_check_mark:<br>:x: |
| **Rock Band 3** | PS3<br>Xbox 360<br>Wii | Known (new-style DTB) | :white_check_mark:<br>:white_check_mark:<br>:white_check_mark: |
| **Rock Band Country Track Pack 2** | PS3<br>Xbox 360<br>Wii | Known (new-style DTB) | :x:<br>:x:<br>:white_check_mark: |
| **Dance Central** | Xbox 360 | Known (new-style DTB) | :white_check_mark: |
| **Dance Central 2** | Xbox 360 | Known (new-style DTB) | :white_check_mark: |
| **Rock Band Blitz** | PS3<br>Xbox 360 | Known (new-style DTB) | :white_check_mark:<br>:white_check_mark: |
| **Dance Central 3** | Xbox 360 | Known (new-style DTB) | :white_check_mark: |
| **Fantasia: Music Evolved** | Xbox 360<br>Xbox One | Unknown | :white_check_mark:<br>:x:|
| **Dance Central: Spotlight** | Xbox One | Unknown | :white_check_mark: |
| **Rock Band 4** | PS4<br>Xbox One | Known (v3 DTA_DTA) | :white_check_mark:<br>:x:[^1][^2] |
| **Rock Band VR** | PC | Known (v3 DTA_DTA) | :white_check_mark:[^2][^3] |
| **Amplitude 2016** | PS3<br>PS4 | Known (v3 DTA_DTA) | :white_check_mark:[^2] |
| **Super Beat Sports** | Switch | Known (v3 DTA_DTA) | :white_check_mark:[^2] |

### Prototypes, Demos and Extra's
| Game | Build (YYMMDD) | Platform | Script Format | Status |
| ---- | ----- | -------- | ------------- | ------ |
| **FreQuency** | 010730 (USA Demo) | PS2 | Known (Python 1) | :white_check_mark: |
| **FreQuency** | 010926 (r179) | PS2 | Known (Python 1) | :white_check_mark: |
| **FreQuency** | 011118 (OPM Demo) | PS2 | Known (Python 1) | :x: |
| **FreQuency** | 020512 (EU Demo) | PS2 | Known (Python 1) | :x: |
| **FreQuency** | 020526 (FreQnet Demo) | PS2 | Known (Python 1) | :x: |
| **Amplitude 2003** | 021218 (USA Demo)| PS2 | Known (DTA) | :x: |
| **Amplitude 2003** | 030702 (Deluge) | PS2 | Known (Amp-style DTB) | :white_check_mark: |
| **Amplitude 2003** | 030318 (FreQnet Demo) | PS2 | Known (Amp-style DTB) | :white_check_mark: |
| **Amplitude 2003** | 021212 (OPM)| PS2 | Known (DTA) | :white_check_mark: |
| **Amplitude 2003** | 030527 (EU Proto) | PS2 | Unknown | :x: |
| **Amplitude 2003** | 030622 (EU Demo) | PS2 | Unknown | :x: |
| **Amplitude 2003** | 030826 (P.O.D) | PS2 | Unknown | :x: |
| **Karaoke Revolution** | 030718 (Deluge 1) | PS2| Unknown | :x: |
| **Karaoke Revolution** | 030904(Deluge 2) | PS2| Unknown | :x: |
| **Karaoke Revolution** | 040817 (Deluge 3)| Xbox | Raw DTA | :white_check_mark: |
| **Karaoke Revolution** | 040908 (Deluge 4) | Xbox | Raw DTA | :white_check_mark: |
| **Karaoke Revolution Volume 2** | 040412 (Deluge 1) | PS2 | Unknown | :x: |
| **Karaoke Revolution Volume 2** | 040518 (Deluge 2) | PS2 | Unknown | :x: |
| **Karaoke Revolution Volume 3** | 040817 (Deluge) | PS2 | Unknown | :x: |
| **EyeToy: AntiGrav** | 040908 (Deluge) | PS2 | Known (old-style DTB) | :x: |
| **Karaoke Revolution Party** | 050813 (Deluge 1) | PS2 | Known (old-style DTB) | :x: |
| **Karaoke Revolution Party** | 050825 (Deluge 2) | PS2 | Known (old-style DTB) | :x: |
| **Guitar Hero** | 050903 (Deluge) | PS2 | Known (old-style DTB) | :white_check_mark: |
| **Guitar Hero II** | 060620 (OPM) | PS2 | Known (old-style DTB) | :white_check_mark: |
| **Guitar Hero II** | 060901 (Retail) | PS2 | Known (old-style DTB) | :white_check_mark: |
| **Guitar Hero II** | 070126 (Demo) | Xbox 360 | Known (old-style DTB) | :white_check_mark: |
| **Guitar Hero II** | 070209 (Demo) | Xbox 360 | Known (old-style DTB) | :white_check_mark: |
| **Guitar Hero Deluxe 1.0** | 210517 | PS2 | Known (old-style DTB) | :white_check_mark: |
| **Guitar Hero Encore: Rocks the 80's** | 070518 (Deluge) | PS2 | Known (old-style DTB) | :white_check_mark: |
| **Rock Band 2** | 080826 | Xbox 360 | Known (new-style DTB) | :white_check_mark: |
| **Rock Band 2** | 081006 | Wii | Known (new-style DTB) | :white_check_mark: |
| **The Beatles Rock Band** | 090619 (Demo) | Xbox 360 | Known (new-style DTB) | :white_check_mark: |
| **The Beatles Rock Band** | 090714 (Demo) | Xbox 360 | Known (new-style DTB) | :white_check_mark: |
| **Rock Band 2** | 090714 (Demo) | Xbox 360 | Known (new-style DTB) | :white_check_mark: |
| **TBRB/RB2 Demo Loader** | 090714 | Xbox 360 | Known (new-style DTB) | :white_check_mark: |
| **Rock Band 3** | 100119 (Bank 6) | Wii | Known (new-style DTB) | :white_check_mark: |
| **Rock Band 3** | 100316 (Bank 5) | Wii | Known (new-style DTB) | :white_check_mark: |
| **Dance Central** | 100607 (E3) | Xbox 360 | Known (new-style DTB) | :white_check_mark: |
| **Dance Central** | 100810 (Takehome) | Xbox 360 | Known (new-style DTB) | :white_check_mark: |
| **Rock Band 3** | 100829 (Bank 2) | Wii | Known (new-style DTB) | :white_check_mark: |
| **Rock Band 3** | 100901 (Bank 8) | Wii | Known (new-style DTB) | :white_check_mark: |
| **Rock Band 3** | 101019 (Bank 1) | Wii | Known (new-style DTB) | :white_check_mark: |
| **Rock Band Music Store** | 110120 | Xbox 360 | Known (new-style DTB) | :white_check_mark: |
| **Dance Central 2** | 110725 (Takehome) | Xbox 360 | Known (new-style DTB) | :white_check_mark: |
| **Rock Band Blitz** | 120605 | Xbox 360 | Known (new-style DTB) | :white_check_mark: |
| **Dance Central 3** | 120829 | Xbox 360 | Known (new-style DTB) | :white_check_mark: |


These tables are not exhaustive. Harmonix released many games and many updates for those games, so this is subject to change and addition as the time goes on. Please let me know about omissions.

[^1]: Due to a slightly unsupported ARK type, some DTA files in rivals are not accurate to the update and may be from a pre-rivals build
[^2]: Forge has multiple DTA types, `.dta_dta` and `.script_dta`. `.script_dta` files are converted with `_script` appended to the file name
[^3]: Song/MOGG DTAs failed to convert
