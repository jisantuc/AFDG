module App exposing (main)

{-| The main application


# Helpers

@doc main

-}

import Html exposing (Html)
import Messages exposing (..)
import State exposing (initialModel, rotatePlayers, setSwitchSource)
import Types exposing (Model, Mode(Inactive))
import View exposing (root)
import Tile.State as T
import Tile.Util exposing (nullTile)


main : Program Never Model Msg
main =
    Html.program
        { view = root
        , update = update
        , init = ( initialModel, Cmd.none )
        , subscriptions = subscriptions
        }


update : Msg -> Model -> ( Model, Cmd Msg )
update msg state =
    case msg of
        NewMode m ->
            let
                updatedTiles =
                    if m == Inactive then
                        (T.update m Nothing nullTile (state.tiles))
                    else
                        state.tiles
            in
                ( { state | activeMode = m, tiles = updatedTiles }, Cmd.none )

        TileSelect tile ->
            let
                updatedTiles =
                    T.update state.activeMode Nothing tile state.tiles
            in
                ( { state | tiles = updatedTiles }, Cmd.none )

        SwitchUsers model ->
            ( rotatePlayers model, Cmd.none )

        AddBorder border tile ->
            let
                updatedTiles =
                    T.update state.activeMode (Just border) tile state.tiles
            in
                ( { state | tiles = updatedTiles }, Cmd.none )

        RemoveBorder border tile ->
            let
                updatedTiles =
                    T.update state.activeMode (Just border) tile state.tiles
            in
                ( { state | tiles = updatedTiles }, Cmd.none )

        SelectSwitchSource tile ->
            setSwitchSource tile state

        SwitchWithTile tile ->
            ( { state
                | tiles = T.maybeSwitchTiles state.tiles state.switchSource tile
                , switchSource = Nothing
              }
            , Cmd.none
            )

        Clear ->
            ( initialModel, Cmd.none )


subscriptions : Model -> Sub Msg
subscriptions _ =
    Sub.none
