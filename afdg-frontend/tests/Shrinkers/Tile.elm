module Shrinkers.Tile exposing (..)

import Lazy.List
    exposing
        ( (:::)
        , empty
        )
import Shrink
    exposing
        ( Shrinker
        , map
        , andMap
        , bool
        , list
        , maybe
        )
import Shrinkers.Base exposing (base_)
import Shrinkers.GameUnit exposing (gameUnit)
import Shrinkers.Geom exposing (coord, color_)
import Tile.Types exposing (..)


border : Shrinker Border
border b =
    case b of
        North ->
            East ::: South ::: West ::: empty

        East ->
            South ::: West ::: empty

        South ->
            West ::: empty

        West ->
            empty


tile : Shrinker Tile
tile { location, fillColor, focused, walls, base, units } =
    map Tile (coord location)
        |> andMap (color_ fillColor)
        |> andMap (bool focused)
        |> andMap (list border <| walls)
        |> andMap (maybe base_ <| base)
        |> andMap (list gameUnit <| units)
