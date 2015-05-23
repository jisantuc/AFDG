from test import *
print """
All printed instructions necessary for assertions to pass.
Assertions check that each component of the game functions as
expected.
"""

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

#TURN 1 MAR only
#Player 1 moves all killed units to (2,2) for this turn

print "All Player1 units must be relocated to (2,2) for assertions to pass."

#move some units
g.find_player('Player1').move(n_oafs = 2,
                              n_wizards = 2,
                              from_loc = (2,2),
                              to_loc = (2,3))
g.find_player('Player1').move(n_oafs = 2,
                              n_wizards = 2,
                              from_loc = (1,1),
                              to_loc = (1,2))
g.find_player('Player1').rotate((1,1), -90)

g.find_player('Player2').move(n_oafs = 3,
                              n_wizards = 2,
                              from_loc = (3,3),
                              to_loc = (2,3))

assert len(g[2,2].units) == 4

g.find_player('Player2').move(n_oafs = 1,
                              n_wizards = 2,
                              from_loc = (0,0),
                              to_loc = (1,0))
g.find_player('Player2').attack_with_wizards(
    n_wizards = [2],
    w_locs = [(1,0)],
    location = (1,1),
    targets = ['oaf'] * 2
)

g.cleanup()

print "Turn 2 player order."
print g.player_order

assert g.find_player('Player2') == g.player_order[-1]
assert len(g[2,2].units) == 6

#TURN 2 ACTIONS

g.find_player('Player2').trade_tiles((0,1), (1,1))
g.find_player('Player1').place_wall((0,1), 'north')

assert g.find_player('Player1').last_action == 'place wall'
assert g.find_player('Player2').last_action == 'trade tiles'

#TURN 2 MAR

g.find_player('Player1').move(1,2,(1,2),(1,1))
g.find_player('Player1').attack_with_wizards(
    n_wizards = [2],
    w_locs = [(1,1)],
    location = (1,0),
    targets = ['wizard','wizard']
)
print "Player2 must relocate one unit to (3,3) and two to (0,0)"
g.find_player('Player1').move(6,0,(2,2),(2,3))
assert len(g[2,3].units) == 6
#player 2 relocates one oaf to (3,3), two to (0,0)

g.find_player('Player1').rotate((3,0), 270)
g.find_player('Player2').move(5,0,(0,0),(1,0))
g.find_player('Player2').rotate((0,1),90)
assert g[0,1].walls['west']

g.cleanup()

assert g.player_order[-1] == g.find_player('Player1')

#TURN 3 ACTIONS

g.find_player('Player1').place_base((3,0))
assert g[0,0].is_base and g[0,0].owned_by == 'Player2'
print 'Player1 reenforces to (3,0)'
g.find_player('Player2').oaf_reenforce([(0,0),(3,3)], [2,1])
assert len(g[0,0].units) == 2
assert len(g[3,3].units) == 3

#TURN 3 MAR

g.find_player('Player2').move(1,0,(0,0),(0,1))
g.find_player('Player2').move(4,0,(1,0),(1,1))
#Player1 relocates to (3,0)
g.find_player('Player2').move(2,0,(3,3),(3,2))

g.find_player('Player2').rotate((0,1),90)
assert g[0,1].walls['south']
assert not g[0,1].is_base and g[0,1].owned_by == 'Player2'

g.find_player('Player1').move(3,0,(2,3),(2,2))
print 'Player2 must relocate to (0,0) because it\'s her only base.'
g.find_player('Player1').move(2,0,(2,3),(3,3))

assert not g[3,3].is_base and g[3,3].owned_by == 'Player1'

g.cleanup()
assert g.player_order[-1] == g.find_player('Player2')

#TURN 4 ACTIONS

g.find_player('Player2').remove_wall((0,1), 'south')
g.find_player('Player1').wizard_reenforce(
    [(3,0),(2,2)],
    [1,1]
)

#TURN 4 MAR

print 'Player2 can only relocate to (0,0)'

g.find_player('Player1').attack_with_wizards(
    [1],
    [(2,2)],
    (3,2),
    ['oaf']
)
g.find_player('Player1').move(2,0,(3,3),(3,2))
g.find_player('Player1').move(1,1,(3,0),(3,1))
g.find_player('Player1').move(1,0,(1,2),(0,2))
g.find_player('Player1').move(3,0,(2,2),(2,1))
g.find_player('Player1').rotate((2,2), 90)

print 'Player1 relocates to (2,2)'
g.find_player('Player2').move(4,0,(1,1),(2,1))

g.find_player('Player2').rotate((3,3), 90)

g.cleanup()
print g.player_order
assert g.player_order[-1] == g.find_player('Player1')

# TURN 5 ACTIONS
g.find_player('Player1').place_wall((2,2), 'north')
g.find_player('Player2').place_wall((3,1), 'west')

# TURN 5 MAR

g.find_player('Player2').move(1,0,(0,1),(1,1))
g.find_player('Player2').move(2,0,(2,1),(2,0))
g.find_player('Player2').rotate((3,3), 270)

g.find_player('Player1').move(1,0,(0,2),(0,1))
g.find_player('Player1').attack_with_wizards(
    [1,1],
    [(2,2),(3,1)],
    (2,1),
    ['oaf']
)
g.find_player('Player1').move(2,1,(2,2),(1,2))
assert len(g[1,2].units) == 3 and\
       g.find_player('Player1').n_wizards_on((1,2)) == 1
g.find_player('Player1').rotate((3,1), 90)

g.cleanup()

# TURN 6 ACTIONS
g.find_player('Player1').oaf_reenforce((3,0),3)
g.find_player('Player2').trade_tiles((2,0),(3,0))
assert g[2,0].is_base and \
       len(g[2,0].units) == 3 \
       and g[2,0].owned_by == 'Player1' \
       and g[3,0].owned_by == 'Player2'

# TURN 6 MAR

print 'First attack from several.'
g.find_player('Player2').move_from_several(
    [2,2,1],
    [0,0,0],
    [(1,0),(3,0),(2,1)],
    (2,0)
)

#lot of assertions because this method is scary
assert len(g[2,0].units) == 5
assert g[2,0].is_base == False and g[2,0].owned_by == 'Player2'
assert len(g[1,0].units) == 0
assert len(g[3,0].units) == 0
assert len(g[2,1].units) == 0
assert len(g[2,2].units) == 4

print 'Second move from several.'
g.find_player('Player2').move_from_several(
    n_oafs = [1,1],
    n_wizards = [0,0],
    from_locs = [(0,0),(1,1)],
    to_loc = (0,1)
)
assert len(g[0,0].units) == 4
assert len(g[1,1].units) == 0
assert len(g[0,1].units) == 2
assert len(g[2,2].units) == 5
assert g[0,1].owned_by == 'Player2'

g.find_player('Player2').rotate((2,2),90)

g.find_player('Player1').move(1,1,(1,2),(0,2))
g.find_player('Player1').attack_with_wizards(
    [1],
    [(0,2)],
    (0,1),
    ['oaf']
)
g.find_player('Player1').move(4,0,(2,2),(2,1))
g.find_player('Player1').move(0,1,(3,1),(2,1))
g.find_player('Player1').attack_with_wizards(
    [1],
    [(2,1)],
    (2,0),
    ['oaf']
)
g.find_player('Player1').move(1,0,(3,2),(3,3))

g.cleanup()

assert g.find_player('Player1').n_tiles == 8
assert g.find_player('Player2').n_tiles == 3

assert len(g[0,0].units) == 6 and\
       len(g[2,0].units) == 4 and\
       len(g[0,1].units) == 1 and\
       len(g[2,1].units) == 5 and\
       len(g[3,1].units) == 1 and\
       g[3,1].walls['south'] and\
       len(g[0,2].units) == 2 and\
       len(g[1,2].units) == 1 and\
       len(g[2,2].units) == 1 and\
       g[2,2].walls['west'] and\
       len(g[3,2].units) == 1 and\
       len(g[2,3].units) == 1 and\
       len(g[3,3].units) == 1

# TURN 7 ACTIONS

#this will be the turn when rotate action is moved, checking that off
