from afdg import Game, Unit, Tile, Player

def trade_tiles():

    g = Game.Game()

    def tile_info(location):
        """
        Prints game tile at location, whether that tile is a
        base, who owns it, and any units on that tile.
        """

        print g[location]
        print g[location].is_base
        print g[location].owned_by
        print g[location].units

    g[1,2].add_wall('north')
    g[2,2].add_wall('south')

    g.players[0].place_base((1,2))
    g.players[0].add_unit('oaf',(1,2))

    tile_info((1,2))
    tile_info((2,2))

    print 'TRADING TILES (1,2) AND (2,2)'

    g.players[0].trade_tiles((1,2),(2,2))

    tile_info((1,2))
    tile_info((2,2))
