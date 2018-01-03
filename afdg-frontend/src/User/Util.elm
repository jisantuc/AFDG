module User.Util exposing (user1, user2)

import User.Types exposing (User, Color)


user1 : User
user1 =
    { name = "player1"
    , id = 1
    , color = "red"
    }


user2 : User
user2 =
    { name = "player2"
    , id = 1
    , color = "blue"
    }
