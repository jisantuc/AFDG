module View exposing (root)

import Html exposing (Html, button, div, text)
import Html.Attributes as HA
import Html.Events exposing (onClick)
import Messages exposing (..)
import Types exposing (..)
import Tile.View as TileView


mkButton : String -> Maybe Msg -> Html Msg
mkButton label msg =
    let
        s =
            [ HA.style [ ( "flex", "auto" ) ] ]
    in
        case msg of
            Just m ->
                button (onClick m :: s) [ text label ]

            Nothing ->
                button s [ text label ]


root : Model -> Html Msg
root model =
    div
        [ HA.style
            [ ( "display", "flex" )
            , ( "flex-direction", "column" )
            ]
        ]
        [ div [ HA.style [ ( "display", "flex" ), ( "flex-grow", "1" ) ] ]
            [ mkButton "Neighbors Mode" (NewMode Neighbors |> Just)
            , mkButton "Reachable Mode" (NewMode Reachable |> Just)
            , mkButton "Nothing Mode" (NewMode Inactive |> Just)
            ]
        , div
            [ HA.style
                [ ( "display", "flex" )
                , ( "flex-grow", "5" )
                , ( "flex-flow", "row wrap" )
                ]
            , HA.width 500
            ]
          <|
            List.map
                TileView.view
                model.tiles
        ]
