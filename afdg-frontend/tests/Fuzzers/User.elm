module Fuzzers.User exposing (..)

import Fuzz exposing (Fuzzer, custom)
import Random.Pcg as Random
import Fuzzers.Util exposing (randomString)
import Shrinkers.User exposing (user)
import Geom.Types exposing (Color(..))
import User.Types exposing (User)


userG : Random.Generator User
userG =
    Random.map3 User randomString (Random.int 0 100) (Random.map Color randomString)


userF : Fuzzer User
userF =
    custom userG user
