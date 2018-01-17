module Shrinkers.User exposing (..)

import Shrink
    exposing
        ( Shrinker
        , map
        , andMap
        , int
        , string
        )
import Shrinkers.Geom exposing (color_)
import User.Types exposing (User)


user : Shrinker User
user { name, id, color } =
    map User (string name)
        |> andMap (int id)
        |> andMap (color_ color)
