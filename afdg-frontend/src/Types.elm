module Types exposing (Model, Mode(..))

{-| Types for working with the main application


# Exported Types

@doc Mode, Neighbors, Reachable, Inactive, AddOafs, AddWizards, Model

-}

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
