from test import *

g.players[0]

g.players[0].place_base((1,1))
g.players[0].add_unit('wizard', (1,1))
g.players[0].trade_tiles((3,3), (3,2))
g.players[0].cleanup()
g.players[0].place_base((2,2))
g.players[0].add_unit('wizard', (2,2))

g.players[1].place_base((1,3))
g.players[1].add_unit('oaf', (1,3))
g.players[1].move(1, 0, (1,3), (1,2))

#g[2,2].add_wall('west')
#g[1,1].add_wall('south')

assert g[1,1].units[0].attack((1,2)) == 1
assert g[2,2].units[0].attack((1,2)) == 1

g.players[0].attack_with_wizards(
    n_wizards = [1,1],
    w_locs = [(1,1), (2,2)],
    location = (2,2),
    targets = ['oaf']
)

print g[1,2].units
