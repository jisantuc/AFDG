module Shrinkers.Base exposing (..)

import Shrink
    exposing
        ( Shrinker
        , map
        )
import Shrinkers.User exposing (user)
import Base.Types exposing (Base)


base_ : Shrinker Base
base_ { ownedBy } =
    map Base (user ownedBy)
