import warnings
import Unit

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
        
        return len(self.invading_units_near(location))

    def wizards_in_range_of(self, location):
        """
        Returns list of wizards that can attack location.
        """
        
        return [u for u in self.units_near(location) if\
                isinstance(u, Unit.Wizard)]

    def n_wizards_in_range_of(self, location):
        """
        Returns number of wizards that can attack location.
        """
        
        return len(self.wizards_in_range_of(location))

    def oafs_on(self, location):
        """
        Returns list of oafs on location.
        """
        
        return [u for u in self.game[location].units if \
                isinstance(u, Unit.Oaf)]

    def n_oafs_on(self, location):
        """
        Counts number of oafs on location.
        """

        return len(self.oafs_on(location))

    def moving_oafs_on(self, location):
        """
        Returns list of oafs on location who can move.
        """

        return [u for u in self.oafs_on(location) if not u.moved]

    def n_moving_oafs_on(self, location):
        """
        Returns number of oafs on location who can move.
        """

        return len(self.moving_oafs_on(location))

    def wizards_on(self, location):
        """
        Returns list of wizards on location.
        """

        return [u for u in self.game[location].units if \
                isinstance(u, Unit.Wizard)]

    def n_wizards_on(self, location):
        """
        Returns number of wizards on location.
        """

        return len(self.wizards_on(location))

    def moving_wizards_on(self, location):
        """
        Returns list of wizards on location who can move.
        """

        return [u for u in self.wizards_on(location) if not u.moved]

    def n_moving_wizards_on(self, location):
        """
        Returns number of wizards on location who can move.
        """

        return len(self.moving_wizards_on(location))

    def attacking_wizards_on(self, location):
        """
        Returns list of wizards on location who can attack.
        """

        return [u for u in self.wizards_on(location) if not u.attacked]

    def n_attacking_wizards_on(self, location):
        """
        Returns number of wizards on location who can attack.
        """

        return len(self.attacking_wizards_on(location))

    def can_invade(self, location, attacking_with=None):
        """
        Returns True if self can invade tile at location.
        """
        
        force = attacking_with if attacking_with else \
                self.n_invading_units_near(location)
        target = self.game[location]
        occupation = target.occupied()

        if not occupation:
            return True
        elif occupation[0].name == self.name:
            return True
        elif force > target.defended_by:
            return True
        else:
            return False             

    def add_unit(self,u_type, base_loc, n = None):
        """
        Adds a unit of type u_type = 'oaf' or 'wizard' on one of
        the player's bases.
        """

        if n:
            for i in range(n):
                self.add_unit(u_type, base_loc)
            return

        if not self.game[base_loc].is_base:
            warnings.warn('Units can only be added on bases.' +\
                          ' Doing nothing.')
            return False
        
        if u_type.lower() == 'oaf':
            to_add = Unit.Oaf(self.game, base_loc, self.name)
            self.game[base_loc].has_oaf = True
        elif u_type.lower() == 'wizard':
            to_add = Unit.Wizard(self.game, base_loc, self.name)
        else:
            warnings.warn('Unknown unit type. Doing nothing.')
            return False
            
        self.units.append(to_add)
        self.game[base_loc].units.append(to_add)        

    def move(self, n_oafs, n_wizards, from_loc, to_loc):
        """
        Moves n_oafs and n_wizards from from_loc to to_loc.
        from_loc and to_loc must be specified as tuples, otherwise
        warns and returns False. If move would fail for any reason,
        does nothing and returns False.
        """

        try:
            assert n_oafs <= self.n_moving_oafs_on(from_loc) and \
                   n_wizards <= self.n_moving_wizards_on(from_loc)
        except AssertionError as e:
            warnings.warn('Inadequate units for command.' +\
                          ' Doing nothing.')
            return False

        try:
            assert isinstance(from_loc, tuple) and \
                   isinstance(to_loc, tuple)
        except AssertionError as e:
            warnings.warn('from_loc and to_loc must be tuples.' +\
                          ' Doing nothing.')
            return False

        if not self.can_invade(to_loc, n_oafs + n_wizards):
            warnings.warn('Inadequate units to invade.' +\
                          ' Doing nothing.')
            return False

        oafs_to_move = self.moving_oafs_on(from_loc)[:n_oafs]
        assert len(oafs_to_move) == n_oafs

        wizards_to_move = self.moving_wizards_on(from_loc)[:n_wizards]
        assert len(wizards_to_move) == n_wizards

        for u in oafs_to_move + wizards_to_move:
            u.move(to_loc)

        ####################################
        # TO ADD:
        # CONQUERED THING FROM move_from_several

    def move_from_several(self, n_oafs, n_wizards, from_locs, to_loc):
        """
        Moves n_oafs and n_wizards from from_locs to to_loc if
        possible. Adds up available units from each and checks to
        make sure invasion is possible with can_invade's
        attacking_with parameter.
        """

        try:
            for i,l in enumerate(from_locs):
                assert n_oafs[i] <= self.n_moving_oafs_on(l) and \
                       n_wizards[i] <= self.n_moving_wizards_on(l)
        except AssertionError as e:
            warnings.warn('Inadequate units on {}.'.format(l) +\
                          ' Doing nothing.')
            return False

        force = sum(n_oafs) + sum(n_wizards)

        if self.can_invade(to_loc, attacking_with = force):
            removed = self.game[to_loc].conquered()
            for i, l in enumerate(from_locs):
                self.move(n_oafs = n_oafs[i], n_wizards = n_wizards[i],
                          from_loc = l, to_loc = to_loc)

            if removed:
                while removed:
                    u = removed[0]
                    new_loc = [int(s) for s in raw_input(
                        'New location\n'
                        ).split(',')]
                    if u.player.add_unit('oaf',new_loc) is None:
                        removed.remove(u)

                    

    def place_base(self, location):
        """
        Places a new base on location.
        """
        
        test_base = self.game[location].can_add_base(self)
        if test_base:
            self.game[location].make_base(self)
        else:
            warnings.warn('Cannot add base on {}.'.format(location) +\
                          ' Doing nothing.')

    def rotate(self, location, angle):
        """
        Rotates tile at location by angle.
        """
        
        self.game[location].rotate(angle)

    def oaf_reenforce(self, location, number):
        """
        Reenforces oafs. Takes locations and numbers as length 3
        lists. Locations must be locations where the player has a
        base.
        """

        try:
            assert len(location) <= 3
        except AssertionError as e:
            warnings.warn('Illegal attempt to add units.' +\
                          ' Doing nothing.')
            return False
        
        if isinstance(location, list) and \
           isinstance(number, list):
            
            if sum(number) != 3 or max(number) > 3:
                warning.warn('Illegal attempt to add units.' +\
                             ' Doing nothing')
                return False

            for loc, n in zip(locations, number):
                self.add_unit('oaf', loc, n)

        elif isinstance(location, tuple) and \
             isinstance(number, int):
            self.add_unit('oaf', location, number)

    def wizard_reenforce(self, location, split = False):
        """
        Reenforces wizards. Takes locations and numbers as length
        3 lists. Locations must be locations where the player has
        a base.
        """
        
        try:
            assert len(location) <= 2
        except AssertionError as e:
            warnings.warn('Illegal attempt to add units.' +\
                          ' Doing nothing.')
            return False
        
        if isinstance(location, list) and \
           isinstance(number, list):
            
            if sum(number) != 2 or max(number) > 2:
                warning.warn('Illegal attempt to add units.' +\
                             ' Doing nothing')
                return False

            for loc, n in zip(locations, number):
                self.add_unit('wizard', loc, n)

        elif isinstance(location, tuple) and \
             isinstance(number, int):
            self.add_unit('wizard', location, number)

    def trade_tiles(self, location1, location2):
        """
        Swaps the positions of orthogonally adjacent tiles at
        location1 and location2 including everything on them
        (walls, units, bases).
        """
        
        if sum([abs(location1[0] - location2[0]),
                abs(location1[1] - location2[1])]) > 1:
            warnings.warn('Tiles not orthogonally adjacent.' +\
                          ' Doing nothing.')
            return False

        chars1 = {'walls': self.game[location1].walls.copy(),
                  'units': self.game[location1].units,
                  'base': self.game[location1].is_base,
                  'owned': self.game[location1].owned_by}

        chars2 = {'walls': self.game[location2].walls.copy(),
                  'units': self.game[location2].units,
                  'base': self.game[location2].is_base,
                  'owned': self.game[location2].owned_by}

        for loc, chars in zip([location1, location2],
                              [chars2, chars1]):
            self.game[loc].set_walls(chars['walls'])
            self.game[loc].set_base(chars['base'])
            self.game[loc].set_owner(chars['owned'])
            self.game[loc].set_units(chars['units'])

            for u in self.game[loc].units:
                u.set_location(loc)

            self.game[loc].update_oaf()
            self.game[loc].defended_by = self.game[loc].count_defenders()
                  

    def place_wall(self, location, direction):
        """
        Attempts to add wall at location on side direction. Fails
        if a wall already present.
        """
        
        self.game[location].add_wall(direction)

    def remove_wall(self, location, direction):
        """
        Attempts to remove a wall at location from side direction.
        Fails if no wall already present.
        """
        
        self.game[location].remove_wall(direction)
