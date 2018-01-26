module Base.View exposing (view)

{-| Methods for rendering bases to SVG


# Renderers

@doc view

-}

import Svg exposing (Svg, line, rect)
import Svg.Attributes
    exposing
        ( x
        , y
        , width
        , height
        , stroke
        , strokeWidth
        , fill
        , fillOpacity
        )
import Messages exposing (Msg)
import Base.Types exposing (Base)
import Geom.Util exposing (colorToString)


view : Base -> Svg Msg
view base =
    let
        color =
            colorToString base.ownedBy.color
    in
        rect
            [ stroke color
            , strokeWidth "2"
            , fill color
            , fillOpacity "0.1"
            , x "10%"
            , y "10%"
            , width "80%"
            , height "80%"
            ]
            []
