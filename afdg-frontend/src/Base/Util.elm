module Base.Util exposing (user1Base, user2Base)

{-| Utilities to support working with bases


# Helpers

@doc user1Base, user2Base

-}

import Base.Types exposing (Base)
import User.Util exposing (user1, user2)


{-| A base for user 1
-}
user1Base : Base
user1Base =
    Base user1


{-| A base for user 2
-}
user2Base : Base
user2Base =
    Base user2
