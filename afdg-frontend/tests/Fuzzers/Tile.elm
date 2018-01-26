module Fuzzers.Tile exposing (..)

import List.Extra exposing (uniqueBy)
import Fuzz
    exposing
        ( Fuzzer
        , custom
        )
import Random.Pcg
    exposing
        ( filter
        , map
        , andMap
        , andThen
        , Generator
        , bool
        , list
        , sample
        )
import Fuzzers.Base exposing (baseG)
import Fuzzers.Geom exposing (colorG, coordG)
import Fuzzers.GameUnit exposing (unitsG)
import Shrinkers.Tile exposing (tile, listTile)
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


tileListG : Generator (List Tile)
tileListG =
    let
        tileGen : Generator (List Tile)
        tileGen =
            list 25 tileG

        -- TODO: I think this should be possible in point-free style but
        -- I'm having trouble thinking through the magical applicative (a,a)
        -- instance that I need for that
        tileToComparable : Tile -> ( Int, Int )
        tileToComparable t =
            ( .x << .location <| t, .y << .location <| t )
    in
        map (uniqueBy tileToComparable) tileGen

tileListF : Fuzzer (List Tile)
tileListF =
    custom tileListG listTile
