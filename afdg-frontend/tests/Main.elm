module Main exposing (..)

import Expect exposing (Expectation)
import Test exposing (..)


suite : Test
suite =
    describe "Tests"
        [ test "Tests should run at all" <|
            \_ -> Expect.equal () ()
        ]
