module Fuzzers.Util exposing (randomString)

import Char
import String
    exposing
        ( concat
        , fromChar
        )
import Random.Pcg as Random


{-| This has to be a joke -- taken from the Random.Pcg docs
-}
lowercaseLetter : Random.Generator Char
lowercaseLetter =
    Random.map (\n -> Char.fromCode (n + 97)) (Random.int 0 25)


{-| Random.Pcg doesn't have built-in support for generating random strings,
so this is a nice stop-gap until that obviously necessary feature is in the
core library. I'm probably going to forget about it though :(
-}
randomString : Random.Generator String
randomString =
    Random.map concat (Random.map (List.map fromChar) <| Random.list 10 lowercaseLetter)
