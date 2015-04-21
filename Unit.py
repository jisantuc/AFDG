import warnings

class Unit:

    def __init__(self, game, location, player_name):
        """
        Takes a game (of class Game), a location (tuple), a player
        (of class Player). Places a unit on location in game
        belonging to player.
        """

        self.x = location[0]
        self.y = location[1]

        assert self.x < game.grid_size[0] and self.y < game.grid_size[1]
        
        if player_name in game.player_names:
            self.player = game.find_player(player_name)
        else:
            raise Exception('Player not found: %r' % player)

        self.moved = False
        self.attacked = False

        self.limits = game.grid_size()
        game.units.append(self)
        self.game = game

    def __repr__(self):
        return 'Unit at {LOC} owned by {PLAYER}'.format(
            LOC = '({x},{y})'.format(x = self.x,
                                     y = self.y),
            PLAYER = self.player.name)

    def set_location(self, new_location):
        """
        Changes location of unit.
        """

        self.x = new_location[0]
        self.y = new_location[1]

    def can_move(self, location = None, direction = None):
        """
        Verifies that a unit can move in a particular direction by
        checking:

        1. Whether the unit's tile has a wall between the unit and the
        target, impeding progress.
        2. Whether the target tile has a wall between the unit and the
        target, impeding progress.
        3. Whether the player needs to conquer the tile and if they are
        able to, then if they opt to.

        If 1 and 2 are false and invasion is unnecessary, returns True.
        If 1 and 2 are false and invasion is possible, returns 'INVADE'.
        Otherwise returns False.

        One of location or direction must be specified. If location is
        specified, direction is inferred from the units current location.
        If direction is specified, location will not be evaluated, i.e.,
        specifying a direction and location in conflict will evaluate
        whether the unit can move in direction instead of to location.
        """

        if direction:
            try:
                assert direction in ['north','south','east','west']
            except AssertionError as e:
                warnings.warn('Direction {} not allowed'.format(direction))
                return False

        elif location:
            test = (self.x - location[0], self.y - location[1])
            if test == (-1,0):
                direction = 'east'
            elif test == (1,0):
                direction = 'west'
            elif test == (0,1):
                direction = 'south'
            elif test == (0,-1):
                direction = 'north'
            else:
                return False

        if self.game[self.x, self.y].has_wall(direction):
            warnings.warn('Wall on your tile to the {}.'.format(direction) +\
                          ' Doing nothing.')
            return False

        try:
            if direction == 'north':
                target = self.game[(self.x, self.y-1)]
                check_dir = 'south'
            elif direction == 'south':
                target = self.game[(self.x, self.y+1)]
                check_dir = 'north'
            elif direction == 'west':
                target = self.game[(self.x-1, self.y)]
                check_dir = 'east'
            else:
                target = self.game[(self.x+1, self.y)]
                check_dir = 'west'

        except IndexError as e:
            warnings.warn('Edge of the map to the {}.'.format(direction) +\
                          ' Doing nothing.')
            return False

        def no_walls(direction = check_dir):
            """
            Checks if target tile has a wall inhibiting movement
            in specified direction.
            """
            return not target.has_wall(check_dir)
                
        return (no_walls(direction) & can_invade(direction))

class Oaf(Unit):
    """
    Subclasses Unit. Includes the move method, which sets both
    self.attacked and self.moved to True.
    """
    pass

class Wizard(Unit):
    """
    Subclass Unit. Includes the move method, which sets
    self.moved to True, and the attack method, which sets
    self.attacked to True.
    """
    pass
