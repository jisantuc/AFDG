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

    def can_move(self, direction, skip_CI = False):
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

        skip_CI parameter allows omitting the check for possibility of
        invasion. Used during the check for possibility of invasion to
        avoid recursion.
        """

        try:
            assert direction in ['north','south','east','west']
        except AssertionError as e:
            warnings.warn('Direction {} not allowed'.format(direction))
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

        def can_invade(direction):
            """
            Checks whether target tile is either unoccupied or
            occupied by the phasing player. If the target tile
            is occupied by any other player, checks whether the
            player has enough units that can move to that tile
            and have not attacked to invade.
            """
            
            occupation = target.occupied()

            if occupation:
                occupant, defense = occupation

                if occupant == self.player:
                    return True
                else:
                    return True if self.player.units_near(taget.location) >\
                                   defense else False
            else:
                return True
                
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
