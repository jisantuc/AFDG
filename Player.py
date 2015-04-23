class Player:

    def __init__(self, name, game, n_units = 0):
        """
        Initializes a player with a name and a counter for
        number of units. Because players start with zero units
        on the board, this value starts at zero.
        """

        self.name = name
        self.game = game
        self.n_units = n_units
        self.units = []

    def __getitem__(self, location):
        """
        Returns units belonging to player on location.
        """
        return [u for u in self.units if (u.x, u.y) == location]

    def units_near(self, location):
        """
        Finds units near location that are adjacent to location.
        """

        distances_x = [abs(u.x - location[0]) for u in self.units]
        distances_y = [abs(u.y - location[1]) for u in self.units]

        return [u for i,u in enumerate(self.units) if distances_x[i] +\
                distances_y[i] == 1]

    def n_units_near(self, location):
        """
        Counts units near location that are adjacent to location.
        """
        return len(self.units_near(location))

    def moving_units_near(self, location):
        """
        Finds units near location that can move to location.
        """
        return [u for u in self.units_near(location) if \
                u.can_move(location = location)]

    def n_moving_units_near(self, location):
        """
        Counts units near location that can move to location.
        """
        return len([self.moving_units_near(location)])

    def invading_units_near(self, location):
        """
        Returns units belonging to self that have neither moved
        nor attacked in the current round.
        """
        return [u for u in self.units_near(location) if not u.attacked and \
                not u.moved and u.can_move(location)]

    def n_invading_units_near(self, location):
        """
        Returns number of units belonging to self that have neither
        moved nor attacked in the current round.
        """
        return len(self.attacking_units_near(location))

    def wizards_in_range_of(self, location):
        """
        Returns list of wizards that can attack location.
        """
        pass

    def n_wizards_in_range_of(self, location):
        """
        Returns number of wizards that can attack location.
        """
        pass

    def can_invade(self, location):
        """
        Returns True if self can invade tile at location.
        """
        target = self.game[location]
        occupation = target.occupied()
        if not occupation:
            return True
        elif occupation[0].name == self.name:
            return True
        elif self.n_invading_units_near(location) >\
             target.defended_by:
            return True
        else:
            return False             

    def add_unit(u_type, base):
        """
        Adds a unit of type u_type = 'oaf' or 'wizard' on one of
        the player's bases.
        """
        pass
        

    def place_base(self, location):
        """
        Places a new base on location.
        """
        test_base = self.game[location].can_add_base(self)
        if test_base:
            self.game[location].make_base(self)

    def rotate(self, location, angle):
        """
        Rotates tile at location by angle.
        """
        pass

    def oaf_reenforce(self, locations, numbers):
        """
        Reenforces oafs. Takes locations and numbers as length 3
        lists. Locations must be locations where the player has a
        base.
        """
        pass

    def wizard_reenforce(self, location, split = False):
        """
        Reenforces wizards. Takes locations and numbers as length
        3 lists. Locations must be locations where the player has
        a base.
        """
        pass

    def trade_tiles(self, location1, location2):
        """
        Swaps the positions of orthogonally adjacent tiles at
        location1 and location2 including everything on them
        (walls, units, bases).
        """
        pass

    def place_wall(self, location, direction):
        """
        Attempts to add wall at location on side direction. Fails
        if a wall already present.
        """
        pass

    def remove_wall(self, location, direction):
        """
        Attempts to remove a wall at location from side direction.
        Fails if no wall already present.
        """
        pass
