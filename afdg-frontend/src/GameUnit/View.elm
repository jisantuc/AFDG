module GameUnit.View exposing (mkOafsMarker, mkWizardsMarker, textAtPoint, view)

{-| Functions for rendering gameUnits


# Renderers

@doc mkOafsMarker, mkWizardsMarker, view

#Helpers

@doc textAtPoint

-}

import GameUnit.Types exposing (..)
import GameUnit.Util exposing (isOaf, isWizard)
import Geom.Types exposing (Color(..), Coord)
import Messages exposing (Msg)
import Svg exposing (Svg, circle, rect, text, text_)
import Svg.Attributes
    exposing
        ( cx
        , cy
        , fill
        , fillOpacity
        , fontFamily
        , fontSize
        , height
        , r
        , stroke
        , strokeWidth
        , textAnchor
        , width
        , x
        , y
        )


{-| Write a message in a consistent style at a coord
-}
textAtPoint : String -> Coord -> Svg Msg
textAtPoint s c =
    text_
        [ x <| String.fromInt c.x
        , y <| String.fromInt c.y
        , stroke "none"
        , fill "black"
        , fontSize "2rem"
        , fontFamily "sans-serif"
        , textAnchor "middle"
        ]
        [ text s ]


{-| Create a marker showing how many oafs of a certain color
-}
mkOafsMarker : Int -> Color -> List (Svg Msg)
mkOafsMarker n (Color color) =
    case n of
        0 ->
            []

        -- TODO: this is total in intent, but partial in handled cases
        -- e.g., negatives shouldn't be possible but they're unhandled
        positiveN ->
            rect
                [ x "60"
                , y "60"
                , width "130"
                , height "130"
                , fillOpacity "70%"
                , fill color
                , stroke "black"
                , strokeWidth "3"
                ]
                []
                :: [ textAtPoint (String.fromInt n) <| Coord 125 125 ]


{-| Create a marker showing how many wizards of a certain color
-}
mkWizardsMarker : Int -> Color -> List (Svg Msg)
mkWizardsMarker n (Color color) =
    case n of
        0 ->
            []

        positiveN ->
            circle
                [ cx "280"
                , cy "280"
                , r "70"
                , fillOpacity "70%"
                , fill color
                , stroke "black"
                , strokeWidth "3"
                ]
                []
                :: [ textAtPoint (String.fromInt n) <| Coord 280 280 ]


view : List GameUnit -> List (Svg Msg)
view units =
    let
        ( nOafs, nWizards ) =
            List.foldl
                (\x z ->
                    case ( isOaf x, isWizard x ) of
                        ( True, _ ) ->
                            ( Tuple.first z + 1, Tuple.second z )

                        ( _, True ) ->
                            ( Tuple.first z, Tuple.second z + 1 )

                        ( _, _ ) ->
                            z
                )
                ( 0, 0 )
                units

        color =
            case List.head units of
                Nothing ->
                    Color "none"

                Just (Oaf obj) ->
                    obj.color

                Just (Wizard obj) ->
                    obj.color
    in
    mkWizardsMarker nWizards color ++ mkOafsMarker nOafs color
