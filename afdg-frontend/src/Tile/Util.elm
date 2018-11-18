module Tile.Util exposing (borderComplement, nullTile, someTiles)

{-| Utilities related to tiles


# Helpers

@doc someTiles, nullTile

-}

import Base.Util exposing (user1Base, user2Base)
import Geom.Types exposing (Color(..), Coord)
import Tile.Types exposing (..)


someTiles : List Tile
someTiles =
    let
        xs =
            List.concat <| List.repeat 4 <| List.range 0 3

        ys =
            List.concat <| List.map (List.repeat 4) <| List.range 0 3

        bases =
            List.map
                (\x ->
                    if remainderBy 2 x == 0 then
                        user1Base

                    else
                        user2Base
                )
            <|
                List.range 0 15

        coords =
            List.map2 Coord xs ys
    in
    List.map2 (\c b -> Tile c (Color "none") False [ North, South ] (Just b) []) coords bases


nullTile : Tile
nullTile =
    Tile { x = -9, y = -9 } (Color "none") False [] Nothing []


{-| Get border types not present in a list of borders
-}
borderComplement : List Border -> List Border
borderComplement borders =
    List.filter
        (\border -> List.member border borders |> not)
        [ North, South, East, West ]
