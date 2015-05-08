from test import *

g.find_player('Player1').place_base((2,2))
g.find_player('Player1').add_unit('wizard', (2,2))

try:
    assert g.find_player('Player1')[2,2][0].count_walls_between((2,1)) == 0
except AssertionError:
    print g.find_player('Player1')[2,2][0].count_walls_between((2,1))

g[2,2].add_wall('north')

try:
    assert g.find_player('Player1')[2,2][0].count_walls_between((2,1)) == 1
except AssertionError:
    print g.find_player('Player1')[2,2][0].count_walls_between((2,1))

g[2,1].add_wall('south')

try:
    assert g.find_player('Player1')[2,2][0].count_walls_between((2,1)) == 2
except AssertionError:
    print g.find_player('Player1')[2,2][0].count_walls_between((2,1))
