module Geom.Types exposing (Color(..), Coord)

{-| Color and geometry types for other modules
-}


{-| Type alias (kind of, since it wasn't getting exported for some reason) for colors
-}
type Color
    = Color String


{-| Alias for point-like coordinates
-}
type alias Coord =
    { x : Int
    , y : Int
    }
