module User.Types exposing (..)

{-| Types for tracking user information


# Exported Types

@doc User

-}

import Geom.Types exposing (Color)


type alias User =
    { name : String
    , id : Int
    , color : Color
    }
