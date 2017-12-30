module App exposing (main)

import Html exposing (Html)
import Messages exposing (..)
import State exposing (initialModel)
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
                    if m == Inactive then (T.update m nullTile (state.tiles))
                        else state.tiles
            in
                ( { state | activeMode = m, tiles = updatedTiles }, Cmd.none )

        TileSelect tile ->
            let
                updatedTiles =
                    T.update state.activeMode tile state.tiles
            in
                ( { state | tiles = updatedTiles }, Cmd.none )

        _ ->
            ( state, Cmd.none )


subscriptions : Model -> Sub Msg
subscriptions _ =
    Sub.none
