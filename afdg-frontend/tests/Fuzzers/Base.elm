module Fuzzers.Base exposing (..)

import Random.Pcg as Random
import Fuzz exposing (Fuzzer, custom)
import Base.Types exposing (Base)
import Fuzzers.User exposing (userG)
import Shrinkers.Base exposing (base_)


baseG : Random.Generator Base
baseG =
    Random.map Base userG


baseF : Fuzzer Base
baseF =
    custom baseG base_
