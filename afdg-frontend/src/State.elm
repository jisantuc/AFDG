module State exposing (initialModel, rotatePlayers)

{-| Methods for working with main application state


# Helpers

@doc initialModel

-}

import Types exposing (..)
import Tile.Util exposing (someTiles)
import User.Util exposing (user1, user2)


{-| The starting state for the application
-}
initialModel : Model
initialModel =
    { tiles = someTiles
    , activeMode = Inactive
    , activeUser = user1
    , users = [ user1, user2 ]
    }


rotatePlayers : Model -> Model
rotatePlayers model =
    let
        rotateAround user users =
            case List.tail users of
                Just us ->
                    List.singleton user |> List.append us

                Nothing ->
                    [ user ]

        getActiveUser initialUser users =
            case List.head users of
                Just u ->
                    u

                Nothing ->
                    initialUser

        rotated =
            rotateAround model.activeUser model.users
    in
        { model
            | users = rotated
            , activeUser = getActiveUser model.activeUser rotated
        }
