import warnings
import random

import matplotlib.pyplot as plt

import Player
import Tile


class Game(object):

    def __init__(self, n_players = 2, n_turns = 8, grid_size = (4,4)):
        """
        Initializes game.

        Checks that:
        1: walls are of type int
        2: n_turns is of type int
        3: grid_size is a 2-tuple
        4: grid_size is made of ints

        Sets up initial player order and randomly places
        walls on tiles in the grid.

        """

        assert type(n_turns) == int
        assert type(grid_size) == tuple
        assert len(grid_size) == 2
        assert type(grid_size[0]) == int and type(grid_size[1]) == int

        self.n_players = n_players
        self.n_turns = n_turns
        self.phase = 'INITIAL'
        self.grid_size = grid_size
        self.turn = 1
        self.players = [Player.Player('Player{}'.format(n+1), self) for n in range(self.n_players)]
        self.player_names = [p.name for p in self.players]
        self.player_order = random.sample(self.players, len(self.players))
        self.tiles = [Tile.Tile(self,
                                location = (i,j),
                                wall_north = False,
                                wall_south = False,
                                wall_east = False,
                                wall_west = False) for i in range(4) \
                                                   for j in range(4)]
        for t in self.tiles:
            t.add_random_walls()
        self.units = []
        
        print 'Player order is: ' + ', '.join(
            [s.name for s in self.player_order]
        )
        
    def __getitem__(self,xy):
        """
        Returns the tile at xy.
        """

        try:
            assert xy[0] < self.grid_size[0] and xy[1] < self.grid_size[1]
        except AssertionError as e:
            warnings.warn('Grid location out of range. Doing nothing.')
            return

        return [t for t in self.tiles if t.location == xy][0]

    def find_player(self, player_name):
        """
        Finds the player object corresponding to the player
        with name = player_name.
        """

        return [p for p in self.players if p.name == player_name][0]

    def collect_units(self):
        """
        Sets self.units to current list of units in the game.
        """

        us = []
        for p in self.players:
            us.append(p.units)
        
        self.units = us

    def loc_in_grid(self, location):
        """
        Checks whether a location is in the game's grid. Returns
        True if this is the case, otherwise False.
        """

        if location[0] < self.grid_size[0] and\
           location[1] < self.grid_size[1]:
            return True
        else:
            return False

    def bases_near(self, location):
        """
        Counts number of bases orthogonally adjacent to location.
        """

        targets = [(location[0] + 1, location[1]),
                   (location[0] - 1, location[1]),
                   (location[0], location[1] + 1),
                   (location[0], location[1] - 1)]

        return bool(sum([self[t].is_base if self.loc_in_grid(t) \
                         else 0 for t in targets]))

    def MAR(self, player):
        """
        Runs the move/attack/rotate phase for player.
        """

        pass
    
    def action_phase(self, player):
        """
        Runs the action phase for player.
        """

        pass
        
    def turn(self):
        """
        For each player in self.players, runs first action_phase
        and then MAR.
        """

        pass

    def cleanup(self):
        """
        Resets moved status of all units in game by iterating
        over tiles.
        """

        for t in self.tiles:
            t.cleanup()
        for p in self.players:
            p.cleanup()

        turn_data = [(p, p.count_tiles(), p.n_units) \
                     for p in self.player_order]

        new_order = sorted(turn_data, key = lambda x: (x[1],x[2]))

        self.player_order = [n[0] for n in new_order]
        
        
