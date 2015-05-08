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

        self.limits = game.grid_size
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

    def infer_direction(self, location):
        test = (self.x - location[0], self.y - location[1])

        if test == (-1,0):
            return 'east'
        elif test == (1,0):
            return 'west'
        elif test == (0,-1):
            return 'south'
        elif test == (0,1):
            return 'north'
        else:
            return False        

    def can_move(self, dir_or_loc):
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
        Otherwise returns False.

        One of location or direction must be specified. If location is
        specified, direction is inferred from the units current location.
        If direction is specified, location will not be evaluated, i.e.,
        specifying a direction and location in conflict will evaluate
        whether the unit can move in direction instead of to location.
        """

        if isinstance(dir_or_loc, str):
            try:
                assert dir_or_loc in ['north','south','east','west']
                direction = dir_or_loc
            except AssertionError as e:
                warnings.warn('Direction {} not allowed'.format(dir_or_loc))
                return False

        elif isinstance(dir_or_loc, tuple):
            direction = self.infer_direction(dir_or_loc)
            if not direction:
                return False

        else:
            warnings.warn('Direction must be string or tuple. Doing nothing.')
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
                
        return no_walls(direction)

    def set_direction(self, dir_or_loc):
        """
        Returns string of direction based on current location
        as either tuple or string.
        """

        if isinstance(dir_or_loc, str):
            try:
                assert dir_or_loc in ['north','south','east','west']
                return dir_or_loc
            except AssertionError as e:
                warnings.warn('Direction {} not allowed'.format(dir_or_loc))
                return False

        elif isinstance(dir_or_loc, tuple):
            direction = self.infer_direction(dir_or_loc)
            if direction:
                return direction
            else:
                return False

    def move_unit(self, loc):
        """
        Does the shared part of unit movement for wizards and oafs.
        """

        direction = self.set_direction(loc)
        able = self.can_move(direction)
            
        if not able:
            return False

        self.game[self.x, self.y].units.remove(self)

        if direction == 'north':
            self.set_location((self.x, self.y-1))
            self.game[self.x, self.y].units.append(self)
        elif direction == 'south':
            self.set_location((self.x, self.y+1))
            self.game[self.x, self.y].units.append(self)
        elif direction == 'east':
            self.set_location((self.x+1, self.y))
            self.game[self.x, self.y].units.append(self)
        else:
            self.set_location((self.x-1, self.y))
            self.game[self.x, self.y].units.append(self)
        

class Oaf(Unit):
    """
    Subclasses Unit. Includes the move method, which sets both
    self.attacked and self.moved to True.
    """

    def __repr__(self):
        return 'Oaf on ({X},{Y}).'.format(X=self.x,
                                          Y=self.y)
    
    def move(self, loc):
        """
        Moves this unit in direction, if allowed. Direction
        must be a string (nsew) or a tuple.
        """

        old_loc = (self.x, self.y)

        self.move_unit(loc)

        self.moved = True
        self.attacked = True
        self.game[self.x, self.y].update_oaf()
        self.game[old_loc].update_oaf()

class Wizard(Unit):
    """
    Subclass Unit. Includes the move method, which sets
    self.moved to True, and the attack method, which sets
    self.attacked to True.
    """
    
    def __repr__(self):
        return 'Wizard on ({X},{Y}).'.format(X=self.x,
                                             Y=self.y)

    def move(self, direction):
        """
        Moves this unit in direction, if allowed. If location
        is specified and direction is not, infers direction from
        location. If direction and location are both specified,
        ignores location.
        """

        self.move_unit(direction)
        
        self.moved = True

    def count_walls_between(self, dir_or_loc):
        """
        Counts walls between self and tile in direction. Returns False
        if (self.x, self.y) and dir_or_loc are not adjacent or if
        dir_or_loc is a direction not in NSEW.
        """

        if isinstance(dir_or_loc, tuple):
            direction = self.infer_direction(dir_or_loc)
        elif isinstance(dir_or_loc, str) and \
             dir_or_loc in ['north','south','east','west']:
            direction = dir_or_loc
        else:
            warnings.warn('Cannot interpret {}.'.format(dir_or_loc) +\
                          ' Doing nothing.')
            return False

        if not direction:
            return False

        if direction == 'north':
            return self.game[self.x, self.y].walls['north'] +\
                   self.game[self.x, self.y - 1].walls['south']
        elif direction == 'south':
            return self.game[self.x, self.y].walls['south'] +\
                   self.game[self.x, self.y + 1].walls['north']
        elif direction == 'east':
            return self.game[self.x, self.y].walls['east'] +\
                   self.game[self.x + 1, self.y].walls['west']
        else:
            return self.game[self.x, self.y].walls['west'] +\
                   self.game[self.x - 1, self.y].walls['east']
            

    def attack(self, location = None, direction = None):
        """
        Attacks location, possibly with help?
        """
        pass
