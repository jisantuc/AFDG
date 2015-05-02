from afdg import Game

g = Game.Game()

for t in g.tiles:
    for d in ['north', 'south', 'east', 'west']:
        t.remove_wall(d)

g.players[0].place_base((2,2))
g.players[0].add_unit('oaf', (2,2), 4)
g.players[0].add_unit('wizard', (2,2), 2)
