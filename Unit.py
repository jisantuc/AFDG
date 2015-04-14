class Unit:

    def __init__(self, game, location, player, wizard = False):
        """
        Takes a location (of class Tile), a player (of class Player), and an
        indicator for whether the unit is a wizard. Places a unit of that type
        on location belonging to player.
        """

        self.x = location[0]
        self.y = location[1]
        self.unit_type = 'wizard' if wizard else 'oaf'

        if player in game.players:
            self.player = player
        else:
            raise Exception('Player not found: %r' % player)

        self.moved = False

    def set_location(self, new_location):
        self.x = new_location[0]
        self.y = new_location[1]

    def move(self, direction = 'north'):
        """
        If possible, moves unit in direction and sets self.moved to True.
        If not possible, warns that nothing happened. Movement in a direction
        is not possible when and only when there is a wall or the edge of the
        grid in that direction.
        """

        if game.tiles[self.location].has_wall(direction):
            warnings.warn('Wall on this unit\'s tile. Cannot move this direction.')
            return
        elif direction == 'north':
            if self.y == 0:
                warnings.warn('Edge of map that way. Cannot move.')
                return
            elif game.tiles[(self.x, self.y - 1)].has_wall('south'):
                warning.warn('Wall on target tile that way.  Cannot move.')
                return
            else:
                self.set_location((self.x, self.y+1))
        elif direction == 'south':
            if self.y == len(game.tiles):
                warnings.warn('Edge of map that way. Cannot move.')
            elif game.tiles[(self.x, self.y + 1)].has_wall('north'):
                warning.warn('Wall on target tile that way. Cannot move.')
            else:
                self.set_location((self.x, self.y+1))
