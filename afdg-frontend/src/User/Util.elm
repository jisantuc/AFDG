module User.Util exposing (user1, user2)

import Geom.Types exposing (Color(..))
import User.Types exposing (User)


user1 : User
user1 =
    { name = "player1"
    , id = 1
    , color = Color "red"
    }


user2 : User
user2 =
    { name = "player2"
    , id = 1
    , color = Color "blue"
    }
