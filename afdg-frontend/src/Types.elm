module Types exposing (Model, Mode(..))

import Tile.Types exposing (Tile)


type Mode
    = Neighbors
    | Reachable
    | Inactive


type alias Model =
    { tiles : List Tile
    , activeMode : Mode
    }
