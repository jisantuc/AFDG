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

def move_units():
    g = Game.Game()
    no_walls = {'north': False,
                'south': False,
                'east': False,
                'west': False}

    for t in g.tiles:
        t.set_walls(no_walls)

    g.players[0].place_base((2,2))
    g.players[0].add_unit('oaf',(2,2))

    def info(loc):
        print g[loc].has_oaf
        print g[loc].occupied()

    g[2,2].units[0].move('north')
    info((2,2))
    info((2,1))
    
    g[2,1].units[0].move('east')
    info((3,1))
    info((2,1))

    g[3,1].units[0].move('south')
    info((3,2))
    info((3,1))

    g[3,2].units[0].move('west')
    info((2,2))
    info((3,2))

    bad = g[2,2].units[0].move((5,5))
    print bad
    
        
