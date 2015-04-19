class Player:

    def __init__(self, name, n_units = 0):
        """
        Initializes a player with a name and a counter for
        number of units. Because players start with zero units
        on the board, this value starts at zero.
        """

        self.name = name
        self.n_units = n_units
