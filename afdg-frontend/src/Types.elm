module Types exposing (Model, Mode(..))

{-| Types for working with the main application


# Exported Types

@doc Mode, Neighbors, Reachable, Inactive, AddOafs, AddWizards, Model

-}

import Tile.Types exposing (Border, Tile)
import User.Types exposing (User)


type Mode
    = Neighbors
    | Reachable
    | Inactive
    | AddOafs User
    | AddWizards User
    | RemoveBases
    | AddBases User
    | RemoveBorders
    | AddBorders


type alias Model =
    { tiles : List Tile
    , activeMode : Mode
    , activeUser : User
    , users : List User
    }
