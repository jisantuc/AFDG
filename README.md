#Goal of the Game

Accumulate as much territory by the end of the game's final turn as possible. The player with the most territory at the end of the game is declared the winner. Ties are broken by which player has the most units remaining. Subsequent ties are not broken.

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
9. Rate moves based on E[WPA+]. This should be trackable in the tracking after each action/after each turn log. **This would be really cool but is probably not going to happen soon.**

Should be initialized with a grid size (default 4x4, but no reason to be restrictive about this). Should also be initialized with n walls, which should have a default, but should be changeable to allow different tests for game quality with levels of restrictiveness.

###Tracking What Turn It Is

This shouldn't be complicated. Should be accomplished with a `turn()` method that takes no parameters and calls all other methods (which do take parameters) and increments on completion.

###Initializing Walls and Bases

Walls initialization happens at game initialization. Bases drafting also needs to happen at game initialization but should be handled by the UI.

##Player

The Player class tracks how many units it has, how many tiles it occupies, how many bases it has, which action it took last, and provides functions for moving from one tile, moving from several tiles, adding units, taking each action, attacking with wizards, and doing end-of-turn cleanup.

##Tile

The Tile class contains the data and methods for each tile in the Game's grid. It tracks the locations of its walls, whether it's a base, whether it's occupied, by whom it's occupied, how defended it is, and what happens when it's conquered. It additionally includes its own method for end-of-turn cleanup.

##Unit

The Unit class contains all of the shared methods and data for Oafs and Wizards and those two subclasses. The shared methods are movement, and whether tiles are accessible.

###Oaf

The Oaf class contains the Oaf's special move method, which checks whether the Oaf's old location is still defended by an Oaf and checks whether the Oaf's new location is now defended by an Oaf (spoiler alert: it is). Movement is attacking for Oafs.

###Wizard

The Wizard class contains the Wizard's special move method, which is *not* also its attack. It additionally contains methods for counting walls between the wizard and a target location and attacking (returning the Wizard's attacking strength to attack) a target location. Wizard attacking is implemented in the Player class.