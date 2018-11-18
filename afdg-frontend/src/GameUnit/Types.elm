module GameUnit.Types exposing (GameUnit(..), OafRecord, WizardRecord)

{-| Types to support Oaf and Wizard units


# Exported Types

@doc GameUnit, OafRecord, WizardRecord

-}

import Geom.Types exposing (Color, Coord)


{-| Sum type for all types of units in the game
-}
type GameUnit
    = Oaf OafRecord
    | Wizard WizardRecord


{-| Type alias for the record type of oafs
-}
type alias OafRecord =
    { location : Coord
    , color : Color
    , hasMoved : Bool
    }


{-| Type alias for the record type of wizards

Wizards can move and attack separately, so they have to track
additional state.

-}
type alias WizardRecord =
    { location : Coord
    , color : Color
    , hasMoved : Bool
    , hasAttacked : Bool
    }
