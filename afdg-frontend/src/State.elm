module State exposing (initialModel)

import Types exposing (Model)
import Tile.Util exposing (someTiles)


initialModel : Model
initialModel =
    { tiles = someTiles
    }
