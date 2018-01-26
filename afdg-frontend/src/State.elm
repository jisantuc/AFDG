module State exposing (initialModel)

{-| Methods for working with main application state


# Helpers

@doc initialModel

-}

import Types exposing (..)
import Tile.Util exposing (someTiles)


{-| The starting state for the application
-}
initialModel : Model
initialModel =
    { tiles = someTiles
    , activeMode = Inactive
    }
