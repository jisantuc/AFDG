module Types exposing (Model, Mode(..))

import Tile.Types exposing (Tile)


type Mode
    = Neighbors
    | Reachable
    | Inactive
    | AddOafs
    | AddWizards


type alias Model =
    { tiles : List Tile
    , activeMode : Mode
    }
