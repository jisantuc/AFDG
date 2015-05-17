from test import *

#add bases for player 1
g.find_player('Player1').place_base((1,1), initial = True)
g.find_player('Player1').place_base((2,2), initial = True)

#add wizards for player 1
g.find_player('Player1').add_unit('wizard', (1,1))
g.find_player('Player1').add_unit('wizard', (2,2))

#add base for player 2
g.find_player('Player2').place_base((1,3), initial = True)

#add oaf for player 2
g.find_player('Player2').add_unit('oaf', (1,3))

#add wizard for player 2
g.find_player('Player2').add_unit('wizard', (1,3))

#move player 2's oaf and wizard into range
g.find_player('Player2').move(1,1,(1,3),(1,2))

#add walls as obstacles
g[1,2].add_wall('east')
g[1,2].add_wall('north')

#ensure that attack is calculated correctly post- adding walls
assert g[1,1].units[0].attack((1,2)) == 0.5
assert g[2,2].units[0].attack((1,2)) == 0.5

target = 'wizard' #can change to oaf to check that that works as well

#kill an oaf or wizard
g.find_player('Player1').attack_with_wizards(
    [1,1],
    [(1,1),(2,2)],
    (1,2),
    [target]
)

print '(1,2) units:'
print g[1,2].units
print '(1,3) units:'
print g[1,3].units
