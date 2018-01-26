A Fairly Dangerous Game
==============

Web app implementation of A Fairly Dangerous Game, an area control board game
on a magic island.

Setup
-----

Development work is currently focused on the frontend only.

### Frontend Development ###

You'll need:

- [elm](elm-lang.org)
- [elm-test](package.elm-lang.org/elm-community/elm-test)

Then `cd` to `afdg-frontend`.

To launch the application, run `elm-reactor`, navigate to `localhost:8000`,
then navigate to `src/App.elm`. You'll need to restart `elm-reactor` if you
make any changes because tooling for elm is only _almost_ perfect.

To run tests, run `elm-test`. Running tests requires an internet connection
for some reason, so don't bother trying it on an airplane unless you're a fancy
in-air wifi person.

Ignore the docker-compose setup and the fetus of a django backend. The django
backend is going away and the docker-compose setup isn't a priority right
now.
