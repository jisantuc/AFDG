class Unit:

    def __init__(self, game, location, player_name):
        """
        Takes a location (tuple), a player (of class Player), and an
        indicator for whether the unit is a wizard. Places a unit of that type
        on location belonging to player.
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

    def __repr__(self):
        return 'Unit at {LOC} owned by {PLAYER}'.format(
            LOC = '({x},{y})'.format(x = self.x,
                                     y = self.y),
            PLAYER = self.player.name)

    def set_location(self, new_location):
        self.x = new_location[0]
        self.y = new_location[1]

    def can_move(self, direction):

        def no_walls(direction):

            pass

        def can_invade(direction):
            
            pass
        
        return (no_walls(direction) & can_invade(direction))

class Oaf(Unit):
    pass

class Wizard(Unit):
    pass
