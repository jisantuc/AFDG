import logging
import warnings
import sys

from Player import Player
from Tile import Tile
from Unit import Unit

import matplotlib.pyplot as plt
import numpy as np

class Game(object):

    def __init__(self, n_walls = 15, n_players = 2, n_turns = 8, grid_size = (4,4)):

        assert type(n_walls) == int
        assert type(n_turns) == int
        assert type(grid_size) == tuple
        assert len(grid_size) == 2
        assert type(grid_size[0]) == int
                        
        self.n_walls = n_walls
        self.n_players = n_players
        self.n_turns = n_turns
        self.phase = 'INITIAL'
        self.grid_size = grid_size
        self.turn = 1
        self.players = [Player('Player{}'.format(n+1)) for n in range(self.n_players)]
        self.player_names = [p.name for p in self.players]
        self.player_order = [p.name for p in np.random.choice(self.players, size = len(self.players), replace = False)]
        self.tiles = [Tile(self,
                           location = (i,j),
                           wall_north = False,
                           wall_south = False,
                           wall_east = False,
                           wall_west = False) for i in range(4) \
                                              for j in range(4)]
        self.units = []
        
        print 'Player order is: ' + ', '.join(self.player_order)
        
    def find_player(self, player_name):
        return [p for p in self.players if p.name == player_name][0]

    def MAR():
        pass
    
    def action_phase():
        pass
        
    def turn():
        pass
