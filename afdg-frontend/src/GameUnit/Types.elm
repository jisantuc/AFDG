module GameUnit.Types exposing (..)

{-| Types to support Oaf and Wizard units
-}

import Geom.Types exposing (Color, Coord)


type GameUnit
    = Oaf OafRecord
    | Wizard WizardRecord


type alias OafRecord =
    { location : Coord
    , color : Color
    , hasMoved : Bool
    }


type alias WizardRecord =
    { location : Coord
    , color : Color
    , hasMoved : Bool
    , hasAttacked : Bool
    }
