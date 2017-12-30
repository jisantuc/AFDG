module Tile.Util exposing (..)

import Tile.Types exposing (..)


someTiles : List Tile
someTiles =
    let
        xs =
            List.concat <| List.repeat 4 <| List.range 0 3

        ys =
            List.concat <| List.map (List.repeat 4) <| List.range 0 3

        coords =
            List.map2 Coord xs ys
    in
        List.map (\c -> Tile c "red" []) coords
