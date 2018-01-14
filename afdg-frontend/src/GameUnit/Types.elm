module GameUnit.Types exposing (..)

{-| Types to support Oaf and Wizard units
-}

import Geom.Types exposing (Color, Coord)


type GameUnit
    = Oaf
        { location : Coord
        , color : Color
        , hasMoved : Bool
        }
    | Wizard
        { location : Coord
        , color : Color
        , hasMoved : Bool
        , hasAttacked : Bool
        }
