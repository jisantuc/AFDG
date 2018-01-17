module Fuzzers.GameUnit exposing (..)

import Random.Pcg as Random
import Fuzzers.Geom exposing (coordG, colorG)
import GameUnit.Types exposing (GameUnit(..), OafRecord, WizardRecord)


oafRecordG : Random.Generator OafRecord
oafRecordG =
    Random.map3 OafRecord coordG colorG Random.bool


wizardRecordG : Random.Generator WizardRecord
wizardRecordG =
    Random.map4 WizardRecord coordG colorG Random.bool Random.bool


oafG : Random.Generator GameUnit
oafG =
    Random.map Oaf oafRecordG


wizardG : Random.Generator GameUnit
wizardG =
    Random.map Wizard wizardRecordG


unitsG : Random.Generator (List GameUnit)
unitsG =
    Random.list 5 <|
        Random.choices [ oafG, wizardG ]
