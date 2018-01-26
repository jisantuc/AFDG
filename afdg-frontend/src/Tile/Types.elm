module Tile.Types exposing (..)

{-| Types to support the Tile module

# Exported Types

@doc Border, Tile

-}

import Base.Types exposing (Base)
import GameUnit.Types exposing (..)
import Geom.Types exposing (Color, Coord)


{-| Enum type for directions a wall can be in
-}
type Border
    = North
    | East
    | South
    | West


{-| Alias for a record with a location and a (possibly empty) list of walls
-}
type alias Tile =
    { location : Coord
    , fillColor : Color
    , focused : Bool
    , walls : List Border
    , base : Maybe Base
    , units : List GameUnit
    }
