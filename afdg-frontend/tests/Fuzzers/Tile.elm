module Fuzzers.Tile exposing (..)

import Fuzz
    exposing
        ( Fuzzer
        , custom
        )
import Random.Pcg
    exposing
        ( map
        , andMap
        , Generator
        , bool
        , list
        , sample
        )
import Fuzzers.Base exposing (baseG)
import Fuzzers.Geom exposing (colorG, coordG)
import Fuzzers.GameUnit exposing (unitsG)
import Shrinkers.Tile exposing (tile)
import Tile.Types exposing (Tile, Border(..))


borderG : Generator (List Border)
borderG =
    list 2 <|
        (sample [ North, South, East, West ]
            |> map (Maybe.withDefault North)
        )


tileG : Generator Tile
tileG =
    map Tile coordG
        |> andMap colorG
        |> andMap bool
        |> andMap borderG
        |> andMap (map Just baseG)
        |> andMap unitsG


tileF : Fuzzer Tile
tileF =
    custom tileG tile
