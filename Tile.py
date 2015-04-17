import warnings

class Tile:
    
    def __init__(self, game, location, wall_north, wall_south, wall_east, wall_west):

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

    def __repr__(self):
        return '\n'.join(['[{0},{1}]'.format(*self.location)] +\
                         [k + ' ' + str(v) for k, v in self.walls.items()])

    def has_wall(self,direction):
        return self.walls[direction]

    def occupied(self):
        return (self.units[0].player, self.defended_by) if self.units else False

    def count_defenders(self):
        defender_types = ['wizard' if u.wizard else 'oaf' for u in self.units]
        return len(defender_types) if 'oaf' in defender_types else 0

    def add_wall(self, direction):
        if not self.walls[direction]:
            self.walls[direction] = True
        else:
            warnings.warn('Wall already on {}.'.format(direction)+\
                          ' Doing nothing.')

    def remove_wall(self, direction):
        if not self.walls[direction]:
            self.walls[directoin] = True
        else:
            warnings.warn('No wall on {}'.format(direction)+\
                          ' Doing nothing.')

    def set_walls(self, walls):
        self.walls = walls

    def rotate(self, angle = 90):
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
        
        
    def collect_units(self):
        self.units = [u for u in self.game.units if u.loc == self.location]
