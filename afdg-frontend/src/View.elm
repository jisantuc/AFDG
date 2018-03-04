module View exposing (root)

import Html exposing (Html, button, div, text)
import Html.Attributes as HA
import Html.Events exposing (onClick)
import Messages exposing (Msg(..))
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
            , mkButton "Add Oafs" (NewMode (AddOafs model.activeUser) |> Just)
            , mkButton "Add Wizards" (NewMode (AddWizards model.activeUser) |> Just)
            , mkButton "Add Borders" (NewMode AddBorders |> Just)
            , mkButton "Remove Borders" (NewMode RemoveBorders |> Just)
            , mkButton "Remove a base" (NewMode RemoveBases |> Just)
            , mkButton "Add a base" (NewMode (AddBases model.activeUser) |> Just)
            , mkButton "Switch players" (SwitchUsers model |> Just)
            , mkButton "Nothing Mode" (NewMode Inactive |> Just)
            , mkButton "Clear" (Clear |> Just)
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
                (TileView.view model.activeMode)
                model.tiles
        ]
