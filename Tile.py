class Tile:
    
    def __init__(self, wall_north, wall_south, wall_east, wall_west):
        self.walls = {'north': wall_north,
                      'south': wall_south,
                      'east': wall_east,
                      'west': wall_west}

    def has_wall(direction):
        return self.walls[direction]
