module View exposing (root)

import Html exposing (Html, button, div, text)
import Html.Attributes as HA
import Messages exposing (..)
import Types exposing (Model)
import Tile.View as TileView


root : Model -> Html Msg
root model =
    div
        [ HA.style
            [ ( "display", "flex" )
            , ( "flex-direction", "column" )
            ]
        ]
        [ div [ HA.style [ ( "display", "flex" ), ( "flex-grow", "1" ) ] ]
            [ button [ HA.style [ ( "flex", "auto" ) ] ] [ text "a button would go here" ]
            , button [ HA.style [ ( "flex", "auto" ) ] ] [ text "also here" ]
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
