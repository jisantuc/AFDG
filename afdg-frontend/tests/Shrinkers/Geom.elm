module Shrinkers.Geom exposing (..)

import Shrink
    exposing
        ( Shrinker
        , int
        , string
        , map
        , andMap
        )
import Geom.Types exposing (Color(..), Coord)


color_ : Shrinker Color
color_ (Color c) =
    map Color (string c)


coord : Shrinker Coord
coord { x, y } =
    (map Coord (int x)) |> andMap (int y)
