from test import *

for t in g.tiles:
    for d in ['north', 'south', 'east', 'west']:
        t.remove_wall(d)

g.find_player('Player1').place_base((1,1))
g.find_player('Player2').place_base((2,2))

g.find_player('Player1').add_unit('oaf', (1,1), 3)
g.find_player('Player2').add_unit('oaf', (2,2), 2)

g.cleanup()
print g.player_order

g.find_player('Player2').move(n_oafs = 1, n_wizards = 0,
                              from_loc = (2,2), to_loc = (3,2))
g.cleanup()
print g.player_order

g.find_player('Player1').move(n_oafs = 1, n_wizards = 0,
                              from_loc = (1,1), to_loc = (1,0))
g.cleanup()
print g.player_order
