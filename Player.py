class Player:

    def __init__(self, name, game, n_units = 0):
        """
        Initializes a player with a name and a counter for
        number of units. Because players start with zero units
        on the board, this value starts at zero.
        """

        self.name = name
        self.n_units = n_units
        self.units = []

    def units_near(self, location):
        """
        Finds units near location that are able to move to location.
        """

        pass

    def n_units_near(self, location):
        """
        Counts units near location that are able to move to location.
        """
        return len(self.units_near(location))

    def add_unit(u_type, base):
        """
        Adds a unit of type u_type = 'oaf' or 'wizard' on one of
        the player's bases.
        """
        pass
        
