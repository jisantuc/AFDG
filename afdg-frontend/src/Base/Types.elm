module Base.Types exposing (..)

import User.Types exposing (User)


type alias Base =
    { ownedBy : User }
