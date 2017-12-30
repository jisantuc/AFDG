module State exposing (initialModel)

import Types exposing (..)
import Tile.Util exposing (someTiles)


initialModel : Model
initialModel =
    { tiles = someTiles
    , activeMode = Inactive
    }
