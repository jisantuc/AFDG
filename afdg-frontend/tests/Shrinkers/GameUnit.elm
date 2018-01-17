module Shrinkers.GameUnit exposing (..)

import Shrink
    exposing
        ( Shrinker
        , map
        , andMap
        , bool
        )
import Shrinkers.Geom exposing (color_, coord)
import GameUnit.Types exposing (GameUnit(..), OafRecord, WizardRecord)


oafRecord : Shrinker OafRecord
oafRecord { location, color, hasMoved } =
    map OafRecord (coord location)
        |> andMap (color_ color)
        |> andMap (bool hasMoved)


wizardRecord : Shrinker WizardRecord
wizardRecord { location, color, hasMoved, hasAttacked } =
    map WizardRecord (coord location)
        |> andMap (color_ color)
        |> andMap (bool hasMoved)
        |> andMap (bool hasAttacked)


gameUnit : Shrinker GameUnit
gameUnit unit =
    case unit of
        Oaf obj ->
            map Oaf (oafRecord obj)

        Wizard obj ->
            map Wizard (wizardRecord obj)
