module Tile.Util exposing (..)

import Base.Util exposing (user1Base, user2Base)
import Geom.Types exposing (Coord)
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
                    if x % 2 == 0 then
                        user1Base
                    else
                        user2Base
                )
            <|
                List.range 0 15

        coords =
            List.map2 Coord xs ys
    in
        List.map2 (\c b -> Tile c "none" False [ North, South ] (Just b) []) coords bases


nullTile : Tile
nullTile =
    Tile { x = -9, y = -9 } "none" False [] Nothing []
