module Geom.Util exposing (colorToString)

{-| Conversions for geometry and color


# Helpers

@doc colorToString

-}

import Geom.Types exposing (Color(..))


colorToString : Color -> String
colorToString (Color c) =
    c
