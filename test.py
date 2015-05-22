"""
Sets up necessary data for other tests.
"""

from afdg import Game

g = Game.Game()
#need to fix turn order here - should be player1 first at the beginning 
#always

for t in g.tiles:
    t.set_walls({'north': False,
                 'south': False,
                 'east': False,
                 'west': False})
