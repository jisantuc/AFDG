module Base.View exposing (view)

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


view : Base -> Svg Msg
view base =
    let
        color =
            base.ownedBy.color
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
