module GameUnit.Util exposing (..)

{-| Utilities for working with game units


# Helpers

@doc newOaf, newWizard, isOaf, isWizard

-}

import Geom.Types exposing (..)
import GameUnit.Types exposing (..)


{-| Create a new oaf at a location with a given color
-}
newOaf : Coord -> Color -> GameUnit
newOaf p c =
    Oaf
        { location = p
        , color = c
        , hasMoved = False
        }


{-| Create a new wizard at a location with a given color
-}
newWizard : Coord -> Color -> GameUnit
newWizard p c =
    Wizard
        { location = p
        , color = c
        , hasMoved = False
        , hasAttacked = False
        }


{-| Check whether a unit is an Oaf
-}
isOaf : GameUnit -> Bool
isOaf u =
    case u of
        Oaf _ ->
            True

        _ ->
            False


{-| Check whether a unit is a Wizard
-}
isWizard : GameUnit -> Bool
isWizard u =
    case u of
        Wizard _ ->
            True

        _ ->
            False
