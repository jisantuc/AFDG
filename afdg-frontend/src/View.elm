module View exposing (root)

import Browser exposing (Document)
import Html exposing (Html, button, div, text)
import Html.Events exposing (onClick)
import Messages exposing (Msg(..))
import Tile.View as TileView
import Types exposing (..)


mkButton : String -> Maybe Msg -> Html Msg
mkButton label msg =
    case msg of
        Just m ->
            button [ onClick m ] [ text label ]

        Nothing ->
            button [] [ text label ]


root : Model -> Document Msg
root model =
    { title = "AFDG"
    , body =
        [ div []
            [ mkButton "Neighbors Mode" (NewMode Neighbors |> Just)
            , mkButton "Reachable Mode" (NewMode Reachable |> Just)
            , mkButton "Add Oafs" (NewMode (AddOafs model.activeUser) |> Just)
            , mkButton "Add Wizards" (NewMode (AddWizards model.activeUser) |> Just)
            , mkButton "Add Borders" (NewMode AddBorders |> Just)
            , mkButton "Remove Borders" (NewMode RemoveBorders |> Just)
            , mkButton "Remove a base" (NewMode RemoveBases |> Just)
            , mkButton "Add a base" (NewMode (AddBases model.activeUser) |> Just)
            , mkButton "Switch players" (SwitchUsers model |> Just)
            , mkButton "Switch tiles" (NewMode SwitchTiles |> Just)
            , mkButton "Nothing Mode" (NewMode Inactive |> Just)
            , mkButton "Clear" (Clear |> Just)
            ]
        , div [] <|
            List.map
                (TileView.view model.activeMode)
                model.tiles
        ]
    }
