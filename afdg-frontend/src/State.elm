module State exposing (init, rotatePlayers, setSwitchSource)

{-| Methods for working with main application state


# Helpers

@doc initialModel

-}

import Messages exposing (..)
import Task
import Tile.Types exposing (Tile)
import Tile.Util exposing (someTiles)
import Types exposing (..)
import User.Util exposing (user1, user2)


init : () -> ( Model, Cmd Msg )
init _ =
    ( initialModel, Cmd.none )


{-| The starting state for the application
-}
initialModel : Model
initialModel =
    { tiles = someTiles
    , activeMode = Inactive
    , activeUser = user1
    , users = [ user1, user2 ]
    , switchSource = Nothing
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


setSwitchSource : Tile -> Model -> ( Model, Cmd Msg )
setSwitchSource tile state =
    case state.switchSource of
        Nothing ->
            ( { state | switchSource = Just tile }
            , Task.succeed (NewMode SelectSwitchTileTarget) |> Task.perform identity
            )

        Just _ ->
            ( state, Cmd.none )
