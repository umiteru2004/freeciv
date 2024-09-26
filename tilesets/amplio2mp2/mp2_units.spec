
[spec]

; Format and options of this spec file: 
options = "+Freeciv-3.1-spec"

[info]

; Apolyton Tileset created by CapTVK with thanks to the Apolyton Civ2
; Scenario League.

; Special thanks go to:
; Alex Mor and Captain Nemo for their excellent graphics work
; in the scenarios 2194 days war, Red Front, 2nd front and other misc graphics. 
; Fairline for his huge collection of original Civ2 unit spanning centuries
; Bebro for his collection of mediveal units and ships

artists = "
    Lexxie9952 [Lexxie]
    Alex Mor [Alex]
    Allard H.S. Höfelt [AHS]
    Bebro [BB]
    Captain Nemo [Nemo][MHN]
    CapTVK [CT] <thomas@worldonline.nl>
    Curt Sibling [CS]
    Erwan [EW]
    Fairline [GB]
    GoPostal [GP]
    Oprisan Sorin [Sor]
    Tanelorn [T]
    Paul Klein Lankhorst / GukGuk [GG]
    Andrew ''Panda´´ Livings [APL]
    Vodvakov
    J. W. Bjerk / Eleazar <www.jwbjerk.com>
    qwm
    FiftyNine
"

[file]
gfx = "amplio2mp2/mp2_units"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 64
dy = 48
pixel_border = 1

tiles = { "row", "column", "tag"
				; Scenario League tags in brackets
  1, 18, "u.escort_fighter" ; [Lexxie]
  1, 19, "u.medium_bomber"  ; [Lexxie]
  2,  1, "u.amphorae"       ; [Lexxie]
  2, 18, "u.anti_aircraft"    ; [Lexxie]
  2, 19, "u.tribesmen"        ; [Lexxie]
  3,  0, "u.well_digger"		  ; [Lexxie]
  3,  2, "u.missile_destroyer" ; [Lexxie]
  3,  3, "u.war_galley"       ; ???
  3,  5, "u.container"        ; Lexxie      ; Is the Freight graphic for MP2 onward (not u.freight--preserves ammplio2 compatibility for other rules)
  3,  6, "u.atom_bomb"        ; Lexxie  
  3,  7, "u.galley"           ; Lexxie
  3,  8, "u.jet_fighter"      ; [Nemo] & [AHS] & [Lexxie]
  3,  9, "u.ram_ship"         ; Lexxie
  3, 10, "u.armor_ii"         ; Wahazar & Lexxie
  3, 11, "u.boat"             ; Lexxie
  3, 12, "u.cargo_ship"       ; Lexxie
  3, 13, "u.mobile_sam"       ; Lexxie
  3, 14, "u.proletarian"	    ; Lexxie
  3, 15, "u.dive_bomber"      ; Lexxie
  3, 16, "u.strike_fighter"   ; Lexxie
  3, 17, "u.pilgrims"		      ; Lexxie
  3, 18, "u.queen"            ; Lexxie 
  3, 19, "u.hbomb"            ; Lexxie
  4,  0, "u.tnuke"            ; Lexxie
  4,  1, "u.ddomb"            ; Lexxie  Doomsday Bomb, should've been ddbomb
  4,  3, "u.train"            ; Lexxie
  4,  4, "u.t_helicopter"     ; Lexxie
  4,  5, "u.airplane"         ; Lexxie
  4,  6, "u.archers2"         ; Lexxie
  4,  7, "u.siege_ram"        ; Lexxie
  4,  8, "u.satellite"        ; Lexxie
  4,  9, "u.falconeers"       ; Lexxie
  4, 10, "u.zealots"          ; Lexxie 
  4, 11, "u.peasants"         ; Lexxie
  4, 12, "u.groundtroops"     ; Lexxie
  4, 13, "u.scout"            ; Lexxie
}
