#Goal of the Game

Accumulate as much territory by the end of the game's final turn as possible. The player with the most territory at the end of the game is declared the winner. Ties are broken by which player has the most units remaining.

#Data of the Game

At any given point the state of the game can be described by:

- the size of the playing area (4x4 or 5x5)
- where units are
- where walls are
- where bases are
- what phase it is
- whose turn it is
- what actions are allowed for each player

#Classes

Pursuant to the above, the classes necessary to implement the game are:

- a `Game` class that tracks turns, phases, and grid size
- a `Player` class that takes actions and stores which actions are not allowed
- a `Tile` class that tracks walls (NSEW), present units, and whether a base is present
- a `Unit` class (with `Wizard` and `Oaf` subclasses) that understands movement and attack rules

##Game

The game class has to do six things:

9. Track what turn it is
9. Track game state after each action and allow taking actions back
9. Initialize walls on tiles and allow players to draft base locations
9. Pass phasing player back and forth between players in the appropriate order
9. Move between phases at the appropriate time
9. Resolve turn order changes at the end of each round

It should optionally do some additional things:

9. Support loading from arbitrary game states, specified in a common format
9. Rate moves based on E[WPA+]. This should be trackable in the tracking after each action/after each turn log

Should be initialized with a grid size (default 4x4, but no reason to be restrictive about this). Should also be initialized with n walls, which should have a default, but should be changeable to allow different tests for game quality with levels of restrictiveness.

###Tracking What Turn It Is

This shouldn't be complicated. Should be accomplished with a `turn()` method that takes no parameters and calls all other methods (which do take parameters) and increments on completion.

###Initializing Walls and Bases

This needs to happen only if the turn number is 1. n_walls locations need to be chosen for walls (because we have a fixed number of walls from the `__init__` call).

##Player
##Tile
##Unit

#Possible Variants

- 6x6 w/ two actions per action round? (declaring 0, 1, or 2 to be not allowed next turn)
