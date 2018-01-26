module User.Util exposing (user1, user2)

{-| Utilities for working with users


# Helpers

@doc user1, user2

-}

import Geom.Types exposing (Color(..))
import User.Types exposing (User)


{-| "Player 1"-style user
-}
user1 : User
user1 =
    { name = "player1"
    , id = 1
    , color = Color "red"
    }


{-| "Player 2"-style user
-}
user2 : User
user2 =
    { name = "player2"
    , id = 1
    , color = Color "blue"
    }
