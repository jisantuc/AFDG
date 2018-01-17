module User.Types exposing (..)

import Geom.Types exposing (Color)


type alias User =
    { name : String
    , id : Int
    , color : Color
    }
