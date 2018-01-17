module Fuzzers.Geom exposing (..)

import Random.Pcg as Random
import Fuzzers.Util exposing (randomString)
import Geom.Types exposing (Color(..), Coord)


colorG : Random.Generator Color
colorG =
    Random.map Color randomString


coordG : Random.Generator Coord
coordG =
    Random.map2 Coord (Random.int 0 4) (Random.int 0 4)
