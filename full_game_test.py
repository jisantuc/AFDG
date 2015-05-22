from test import *

#draft bases
g.find_player('Player1').place_base((1,1), initial = True)
g.find_player('Player2').place_base((3,3), initial = True)
g.find_player('Player2').place_base((0,0), initial = True)
g.find_player('Player1').place_base((2,2), initial = True)

#add Player1's units
g.find_player('Player1').add_unit('oaf', (1,1), 4)
g.find_player('Player1').add_unit('oaf', (2,2), 4)
g.find_player('Player1').add_unit('wizard', (1,1), 2)
g.find_player('Player1').add_unit('wizard', (2,2), 2)

#add Player2's units
g.find_player('Player2').add_unit('oaf', (0,0), 4)
g.find_player('Player2').add_unit('oaf', (3,3), 4)
g.find_player('Player2').add_unit('wizard', (0,0), 2)
g.find_player('Player2').add_unit('wizard', (3,3), 2)

#TURN 1

#move some units
g.find_player('Player1').move(n_oafs = 2,
                              n_wizards = 2,
                              from_loc = (2,2),
                              to_loc = (2,3))
g.find_player('Player1').move(n_oafs = 2,
                              n_wizards = 2,
                              from_loc = (1,1),
                              to_loc = (1,2))

g.find_player('Player2').move(n_oafs = 3,
                              n_wizards = 2,
                              from_loc = (3,3),
                              to_loc = (2,3))
#should prompt twice for new locations for dead oafs
assert len(g[2,2].units) == 4


g.find_player('Player2').move(n_oafs = 1,
                              n_wizards = 2,
                              from_loc = (0,0),
                              to_loc = (0,1))
