module Tile.Types exposing (..)

{-| Types to support the Tile module
-}

import Base.Types exposing (Base)


{-| Alias for colors
-}
type alias Color =
    String


{-| Alias for point-like coordinates
-}
type alias Coord =
    { x : Int
    , y : Int
    }


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
    { coord : Coord
    , fillColor : Color
    , focused : Bool
    , walls : List Border
    , base : Maybe Base
    }
