"""
Sets up necessary data for other tests.
"""

from afdg import Game

g = Game.Game()

for t in g.tiles:
    for d in ['north', 'south', 'east', 'west']:
        t.remove_wall(d)
