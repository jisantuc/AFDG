module Tile.View exposing (..)

{-| Render tiles to html
-}

import Html exposing (Html, div)
import Html.Attributes as HA
import Html.Events exposing (onClick)
import Svg exposing (Svg, line, rect, svg)
import Svg.Attributes
    exposing
        ( x
        , y
        , x1
        , y1
        , x2
        , y2
        , rx
        , ry
        , stroke
        , strokeWidth
        , height
        , width
        , fill
        , viewBox
        )
import Messages exposing (..)
import Base.View
import GameUnit.View as GU
import Geom.Types exposing (Coord)
import Tile.Types exposing (..)
import Geom.Util exposing (colorToString)


drawLine : Coord -> Coord -> Svg Msg
drawLine c1 c2 =
    line
        [ toString c1.x |> x1
        , toString c2.x |> x2
        , toString c1.y |> y1
        , toString c2.y |> y2
        , strokeWidth "3"
        , stroke "black"
        ]
        []


mkLine : Border -> Svg Msg
mkLine bord =
    case bord of
        North ->
            drawLine (Coord 25 25) (Coord 375 25)

        East ->
            drawLine (Coord 375 25) (Coord 375 375)

        West ->
            drawLine (Coord 25 25) (Coord 25 375)

        South ->
            drawLine (Coord 25 375) (Coord 375 375)


{-| Draw lines for a tile's walls
-}
lines : Tile -> List (Svg Msg)
lines tile =
    List.map mkLine tile.walls


{-| Draw this tile's base, if it has one
-}
base : Tile -> List (Svg Msg)
base tile =
    case Maybe.map Base.View.view tile.base of
        Nothing ->
            []

        Just elem ->
            [ elem ]


units : Tile -> List (Svg Msg)
units tile =
    GU.view tile.units


{-| Show a tile as an SVG rectangle
-}
view : Tile -> Html Msg
view tile =
    div
        [ HA.style
            [ ( "display", "flex" )
            , ( "padding", "8px" )
            , ( "flex-basis", "23%" )
            ]
        ]
        [ svg
            [ viewBox "0 0 400 400"
            , onClick (TileSelect tile)
            ]
          <|
            [ rect
                [ x "0"
                , y "0"
                , rx "5%"
                , ry "5%"
                , width "100%"
                , height "100%"
                , fill <| colorToString tile.fillColor
                , stroke "red"
                , strokeWidth "6"
                ]
                []
            ]
                ++ lines tile
                ++ base tile
                ++ units tile
        ]
