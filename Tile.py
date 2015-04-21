import warnings
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
            warnings.warn('Wall already on {}.'.format(direction)+\
                          ' Doing nothing.')

    def remove_wall(self, direction):
        """
        Removes a wall from this tile on side direction if a
        wall is already present on that side.
        """

        if not self.walls[direction]:
            self.walls[directoin] = True
        else:
            warnings.warn('No wall on {}'.format(direction)+\
                          ' Doing nothing.')

    def set_walls(self, walls):
        """
        Replaces self.walls with a new dictionary of walls.
        """
        self.walls = walls

    def rotate(self, ange = 90):
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
 
    def check_for_oaf(self):
        """
        Returns True if an Oaf is present on the tile,
        otherwise False.
        """
        return bool(len([u for u in self.units if isinstance(u, Unit.Oaf)]))
        
    def collect_units(self):
        """
        Collects units on this tile. Called at the end of a
        player's move/attack/rotate phase.
        Also updates self's has_oaf attribute.
        """
        self.units = [u for u in self.game.units if u.loc == self.location]
        self.has_oaf = self.check_for_oaf()
