import warnings
import itertools

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
        self.n_tiles = 0
        self.units = []
        self.n_bases = 0
        self.actions = {
            'rotate': False,
            'place base': False,
            'oafs reenforce': False,
            'wizards reenforce': False,
            'place wall': False,
            'remove wall': False,
            'trade tiles': False
        }
        self.last_action = None

    def __getitem__(self, location):
        """
        Returns units belonging to player on location.
        """
        
        return [u for u in self.units if (u.x, u.y) == location]

    def __repr__(self):
        return self.name

    def count_tiles(self):
        """
        Counts tiles occupied by self.
        """

        return len([t for t in self.game.tiles if t.occupied() and \
                    t.occupied()[0] == self])

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

        
        removed = self.game[to_loc].conquered()
        if removed and self.game[to_loc].owned_by != self.name:
            att_flag = True
            while removed:
                u = removed[0]
                new_loc = tuple([int(s) for s in raw_input(
                    '{}: New location\n'.format(u.player)
                ).lstrip('(').rstrip(')').split(',')])
                if u.player.add_unit('oaf',new_loc) is None:
                    removed.remove(u)
        elif removed and self.game[to_loc].owned_by == self.name:
            att_flag = False
        else:
            att_flag = False

        for u in oafs_to_move + wizards_to_move:
            u.move(to_loc)
            if att_flag and isinstance(u, Unit.Wizard):
                u.attacked = True
        if att_flag:
            self.game[to_loc].set_units(oafs_to_move + wizards_to_move)
        else:
            self.game[to_loc].set_units(
                oafs_to_move + wizards_to_move + removed
            )
        self.game[to_loc].update_owner()
        self.game[from_loc].update_owner()

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
        for l in from_locs:
            self.game[l].update_owner()
        self.game[to_loc].update_owner()

    def attack_with_wizards(self, n_wizards, w_locs, location, targets):
        """
        Attacks location with wizards located on w_locs (list).

        Checks whether units listed in targets ('oaf' or 'wizard')
        are present on location. Returns False if they are not.

        Sets w.attacked = True for all w in n_wizards (list, matching up
        to number of wizards to attack with from each location in
        w_locs).

        Gives defending player the opportunity to redeploy oafs to
        their bases if any oafs are defeated.
        """

        try:
            check_targets = [t in ['oaf','wizard'] for t in targets]
            assert all(check_targets)
        
        except AssertionError:
            warnings.warn('Bad target. Doing nothing.')
            return False

        try:
            wizards = list(itertools.chain(
                *[self.attacking_wizards_on(l)[-n:] for n, l in zip(
                    n_wizards, w_locs
                    )]
                ))

            assert sum([w.attack(location) for w in wizards]) >= len(targets)


        except IndexError:
            warnings.warn('Inadequate wizards on one of those.' +\
                          ' Doing nothing.')
            return False

        except AssertionError:
            warnings.warn('Too many targets for attacking strength.' +\
                          ' Doing nothing.')
            return False

        n_o = len([t for t in targets if t == 'oaf'])
        oafs_attacked = self.game[location].oafs_on()[-n_o:] if n_o else []

        n_w = len([t for t in targets if t == 'wizard'])
        wizards_attacked = self.game[location].wizards_on()[-n_w:] if n_w else []

        for u in oafs_attacked + wizards_attacked:
            u.die()

        for w in wizards:
            w.attacked = True


    def place_base(self, location, initial=False):
        """
        Places a new base on location.
        """
        
        if self.actions['place base']:
            warnings.warn('Cannot take same action twice in a row.' +\
                          ' Doing nothing.')
            return False

        target = self.game[location]
        test_base = target.can_add_base(self)

        if test_base:
            target.make_base(self)
            self.n_bases += 1
        else:
            warnings.warn('Cannot add base on {}.'.format(location) +\
                          ' Doing nothing.')
            return False

        if not initial:
            self.actions['place base'] = True
            self.last_action = 'place base'

    def rotate(self, location, angle, action = False):
        """
        Rotates tile at location by angle.
        """

        #check that if not an action, only 90 degree rotation is specified
        assert not (not action and (angle % 360 != 90 and
                                    angle % 360 != 270))

        if self.actions['rotate']:
            warnings.warn('Cannot take same action twice in a row.' +\
                          ' Doing nothing.')
            return False

        self.game[location].rotate(angle)

        if action:
            self.actions['rotate'] = True
            self.last_action = 'rotate'

    def oaf_reenforce(self, location, number):
        """
        Reenforces oafs. Takes locations and numbers as length 3
        lists. Locations must be locations where the player has a
        base.
        """

        if self.actions['oaf reenforce']:
            warnings.warn('Cannot take same action twice in a row.' +\
                          ' Doing nothing.')
            return False

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

        self.actions['oaf reenforce'] = True
        self.last_action = 'oaf reenforce'

    def wizard_reenforce(self, location, split = False):
        """
        Reenforces wizards. Takes locations and numbers as length
        3 lists. Locations must be locations where the player has
        a base.
        """

        if self.actions['wizards reenforce']:
            warnings.warn('Cannot take same action twice in a row.' +\
                          ' Doing nothing.')
            return False

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

        self.actions['wizards reenforce'] = True
        self.last_action = 'wizards reenforce'

    def trade_tiles(self, location1, location2):
        """
        Swaps the positions of orthogonally adjacent tiles at
        location1 and location2 including everything on them
        (walls, units, bases).
        """

        if self.actions['trade tiles']:
            warnings.warn('Cannot take same action twice in a row.' +\
                          ' Doing nothing.')
            return False
        
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

        self.actions['trade tiles'] = True
        self.last_action = 'trade tiles'

    def place_wall(self, location, direction):
        """
        Attempts to add wall at location on side direction. Fails
        if a wall already present.
        """

        if self.actions['place wall']:
            warnings.warn('Cannot take same action twice in a row.' +\
                          ' Doing nothing.')
            return False
        
        self.game[location].add_wall(direction)

        self.actions['place wall'] = True
        self.last_action = 'place wall'

    def remove_wall(self, location, direction):
        """
        Attempts to remove a wall at location from side direction.
        Fails if no wall already present.
        """

        if self.actions['remove wall']:
            warnings.warn('Cannot take same action twice in a row.' +\
                          ' Doing nothing.')
            return False
        
        self.game[location].remove_wall(direction)

        self.actions['remove wall'] = True
        self.last_action = 'remove wall'

    def cleanup(self):
        """
        Resets self.actions dict to False for everything but last
        action. Counts units.
        """

        for k in self.actions.keys():
            self.actions[k] = True if k == self.last_action else False

        self.n_units = len(self.units)
        for u in self.units:
            u.attacked = False
            u.moved = False
