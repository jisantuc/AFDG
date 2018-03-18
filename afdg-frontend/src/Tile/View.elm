module Tile.View exposing (..)

{-| Render tiles to html


# Renderers

@doc walls, base, units, view


# Helpers

@doc mkLine, drawLine

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
        , strokeDasharray
        , height
        , width
        , fill
        , viewBox
        )
import Messages exposing (..)
import Types exposing (Mode(AddBorders, RemoveBorders, SelectSwitchTileTarget, SwitchTiles))
import Base.View
import GameUnit.View as GU
import Tile.Types exposing (..)
import Geom.Util exposing (colorToString)
import Tile.Util exposing (borderComplement)


type alias Dashed =
    Bool


type alias SvgStyles =
    List (Svg.Attribute Msg)


{-| Draw an svg line from coord to coord
-}
drawLine : SvgStyles -> Svg Msg
drawLine styles =
    line styles []


getBorderSvgAttributes : Int -> Int -> Int -> Int -> Mode -> Tile -> Border -> SvgStyles
getBorderSvgAttributes xOne yOne xTwo yTwo mode tile border =
    let
        baseStyles =
            [ toString xOne |> x1
            , toString xTwo |> x2
            , toString yOne |> y1
            , toString yTwo |> y2
            , strokeWidth "3"
            , stroke "black"
            ]
    in
        (case ( mode, List.member border tile.walls ) of
            ( RemoveBorders, True ) ->
                [ onClick (RemoveBorder border tile) ]

            ( AddBorders, False ) ->
                [ onClick (AddBorder border tile)
                , strokeDasharray "5, 5"
                ]

            _ ->
                []
        )
            |> (++) baseStyles


{-| Create an SVG line from a Border
-}
mkLine : Mode -> Tile -> Border -> Svg Msg
mkLine mode tile border =
    case border of
        North ->
            getBorderSvgAttributes 25 25 375 25 mode tile border |> (flip line) []

        East ->
            getBorderSvgAttributes 375 25 375 375 mode tile border |> (flip line) []

        West ->
            getBorderSvgAttributes 25 25 25 375 mode tile border |> (flip line) []

        South ->
            getBorderSvgAttributes 25 375 375 375 mode tile border |> (flip line) []


{-| Draw lines for a tile's walls
-}
walls : Mode -> Tile -> List (Svg Msg)
walls mode tile =
    List.map (mkLine mode tile) tile.walls


{-| Draw placeholders for where walls could be added
-}



-- TODO: add test making sure that in all modes other than AddBorder,
-- this returns an empty list


addableWalls : Mode -> Tile -> List (Svg Msg)
addableWalls mode tile =
    case mode of
        AddBorders ->
            borderComplement (tile.walls)
                |> List.map (mkLine mode tile)

        _ ->
            []


{-| Draw this tile's base, if it has one
-}
base : Tile -> List (Svg Msg)
base tile =
    case Maybe.map Base.View.view tile.base of
        Nothing ->
            []

        Just elem ->
            [ elem ]


{-| Convert a tile's units to [Svg Msg]
-}
units : Tile -> List (Svg Msg)
units tile =
    GU.view tile.units


getOnClick : Mode -> (Tile -> Msg)
getOnClick mode =
    case mode of
        SwitchTiles ->
            SelectSwitchSource

        SelectSwitchTileTarget ->
            SwitchWithTile

        _ ->
            TileSelect


{-| Show a tile as an SVG rectangle
-}
view : Mode -> Tile -> Html Msg
view mode tile =
    div
        [ HA.style
            [ ( "display", "flex" )
            , ( "padding", "8px" )
            , ( "flex-basis", "23%" )
            ]
        ]
        [ svg
            [ viewBox "0 0 400 400"
            , (getOnClick mode) tile |> onClick
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
                ++ walls mode tile
                ++ addableWalls mode tile
                ++ base tile
                ++ units tile
        ]
