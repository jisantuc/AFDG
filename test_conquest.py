"""
Tests conquering a player's base and moving the unit.
"""

#to add: make sure original base is no longer a base after conquest

from test import *

g.players[0].place_base((2,2))
g.players[0].add_unit('oaf', (2,2), 4)
g.players[0].add_unit('wizard', (2,2), 2)

g.players[1].place_base((3,3), initial = True)
g.players[1].add_unit('oaf', (3,3))
g.players[1].trade_tiles((3,3), (3,2))
g.players[1].place_base((1,1))

g.players[0].move(n_oafs = 2, n_wizards = 2, from_loc = (2,2), to_loc = (3,2))

print 'Units on (2,2):'
print g[2,2].units

print 'Units on (3,2):'
print g[3,2].units

print 'Units on (1,1):'
print g[1,1].units
