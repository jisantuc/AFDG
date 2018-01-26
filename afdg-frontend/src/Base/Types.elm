module Base.Types exposing (..)

{-| Types to support working with Bases


# Exported Types

@doc Base

-}

import User.Types exposing (User)


type alias Base =
    { ownedBy : User }
