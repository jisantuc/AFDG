"""
Sets up necessary data for other tests.
"""

from afdg import Game

g = Game.Game()

for t in g.tiles:
    t.set_walls({'north': False,
                 'south': False,
                 'east': False,
                 'west': False})
