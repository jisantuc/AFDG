module User.Types exposing (..)


type alias Color =
    String


type alias User =
    { name : String
    , id : Int
    , color : String
    }
