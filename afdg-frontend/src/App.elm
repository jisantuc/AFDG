module App exposing (main)

import Html exposing (Html)
import Messages exposing (..)
import State exposing (initialModel)
import Types exposing (Model)
import View exposing (root)
import Tile.State as T


main : Program Never Model Msg
main =
    Html.program
        { view = root
        , update = update
        , init = ( initialModel, Cmd.none )
        , subscriptions = subscriptions
        }


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        TileMouseIn tile ->
            let
                updatedTiles =
                    T.update Focus tile model.tiles
            in
                ( { model | tiles = updatedTiles }, Cmd.none )

        TileMouseOut tile ->
            let
                updatedTiles =
                    T.update UnFocus tile model.tiles
            in
                ( { model | tiles = updatedTiles }, Cmd.none )

        _ ->
            ( model, Cmd.none )


subscriptions : Model -> Sub Msg
subscriptions _ =
    Sub.none
