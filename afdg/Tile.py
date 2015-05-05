import warnings
import random

import Unit

class Tile:
    
    def __init__(self, game, location, wall_north, wall_south, wall_east, wall_west):
        """
        Creates a tile in a game at a particular location with
        booleans indicating in which direction the tile has walls.
        """
        assert location[0] < game.grid_size[0] and \
               location[1] < game.grid_size[1]

        self.walls = {'north': wall_north,
                      'south': wall_south,
                      'east': wall_east,
                      'west': wall_west}
        self.game = game
        self.location = location
        self.units = []
        self.defended_by = 0
        self.has_oaf = False
        self.is_base = False
        self.owned_by = None

    def __repr__(self):
        return '\n'.join(['[{0},{1}]'.format(*self.location)] +\
                         [k + ' ' + str(v) for k, v in self.walls.items()])

    def has_wall(self,direction):
        """
        Returns whether a tile has a wall in a particular direction.
        """

        return self.walls[direction]

    def occupied(self):
        """
        Returns either the player and number of units defending the tile
        or False if no player is occupying the tile.
        """

        self.defended_by = self.count_defenders()
        return (self.units[0].player, self.defended_by) if self.units else False

    def count_defenders(self):
        """
        Counts number of defenders on the tile.
        Based on the rules of AFDG, if there are no oafs, the tile
        is not actually defended no matter how many wizards are on it.
        """

        return len(self.units) if self.has_oaf else False

    def add_wall(self, direction):
        """
        Adds a wall to this tile on side direction if no wall
        already present on that side.
        """

        if not self.walls[direction]:
            self.walls[direction] = True
        else:
            warnings.warn('Wall already on {0} of {1}.'.format(
                direction,
                self.location
            ) + ' Doing nothing.')

    def remove_wall(self, direction):
        """
        Removes a wall from this tile on side direction if a
        wall is already present on that side.
        """

        if self.walls[direction]:
            self.walls[direction] = False
        else:
            warnings.warn('No wall on {} on {}'.format(direction,
                                                       self.location)+\
                          ' Doing nothing.')

    def add_random_walls(self):
        """
        Adds up to three walls in randomly selected directions.
        """
        
        dirs = ['north','south','east','west']
        n_walls = random.choice([0,1,2,2,3]) #slightly overweights 2

        walls = random.sample(dirs, n_walls)
        for w in walls:
            self.add_wall(w)            
        
    def set_walls(self, walls):
        """
        Replaces self.walls with a new dictionary of walls.
        """

        self.walls = walls

    def rotate(self, angle = 90):
        """
        Rotates the tile by angle. Angle must be evenly divisible
        by 90, but is otherwise unbounded.
        """

        assert angle % 90 == 0
        angle = angle % 360
        dirs = {90: {'north': 'west',
                     'west': 'south',
                     'south': 'east',
                     'east': 'north'},
                180: {'north': 'south',
                      'south': 'north',
                      'west': 'east',
                      'east': 'west'},
                270: {'north': 'east',
                      'east': 'south',
                      'south': 'west',
                      'west': 'north'}}

        new_walls = {dirs[angle][k]: self.walls[k] for k in dirs[angle].keys()}

        self.set_walls(new_walls)
         
    def set_owner(self,player_name = None):
        """
        Sets self.owned_by equal to player.name.
        """

        self.owned_by = player_name if player_name is not None else None

    def make_base(self,player):
        """
        Makes self a base location for player.
        """

        self.is_base = True
        self.owned_by = player.name

    def can_add_base(self,player):
        """
        Checks if self is a base for player.
        """

        test_occ = self.occupied()
        if self.is_base:
            return False
        elif test_occ and test_occ[0].name != player.name:
            return False
        elif self.game.bases_near(self.location):
            return False
        else:
            return True
    
    def check_for_oaf(self):
        """
        Checks whether tile has an oaf.
        """

        return bool(sum([isinstance(u, Unit.Oaf) for u in self.units]))

    def update_oaf(self):
        """
        Sets self.has_oaf to current oaf status.
        """

        self.has_oaf = self.check_for_oaf()

    def collect_units(self):
        """
        Collects units on this tile. Called at the end of a
        player's move/attack/rotate phase.
        Also updates self's has_oaf attribute.
        """

        self.units = [u for u in self.game.units if u.loc == self.location]
        self.has_oaf = self.check_for_oaf()

    def add_unit(self, u):
        """
        Adds unit u to self.units.
        """

        self.units.append(u)

    def set_units(self, us):
        """
        Takes a list of units and sets self.units equal
        to that list.
        """

        self.units = us

    def set_base(self, b):
        """
        Sets self.is_base to b.
        """

        self.is_base = b

    def remove_unit(self, u):
        """
        Removes unit from self.units.
        """

        self.units.remove(u)
        return u

    def conquered(self):
        """
        Removes all units and stores any oafs in a list to return.
        """

        player = self.units[0].player
        for u in self.units:
            player.units.remove(u)

        if self.is_base:
            player.n_bases -= 1

        if player.n_bases == 0:
            return []
            
        return [self.remove_unit(u) for u in self.units \
                if isinstance(u, Unit.Oaf)]

    def cleanup(self):
        """
        Sets moved to False for all units on self and counts defenders.
        """

        for u in self.units:
            u.moved = False
        self.defended_by = self.count_defenders()
