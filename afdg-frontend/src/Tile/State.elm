module Tile.State exposing (..)

{-| Types and methods for grid information


# Exported Types

@doc Tile, Coord, Border


# Helpers

@doc borders, neighbors, view

-}

import Messages exposing (Msg(..))
import Tile.Types exposing (..)


model : Tile
model =
    Tile (Coord 1 0) "red" [ West ]


{-| Check whether two tiles border each other
-}
borders : Tile -> Tile -> Bool
borders tile other =
    let
        xDist =
            abs <| tile.coord.x - other.coord.x

        yDist =
            abs <| tile.coord.y - other.coord.y

        totalDist =
            xDist + yDist
    in
        xDist <= 1 && yDist <= 1 && totalDist == 1


{-| Find all tiles that border a tile
-}
neighbors : Tile -> List Tile -> List Tile
neighbors tile =
    List.filter (borders tile)



-- UPDATE


update : Msg -> Tile -> List Tile -> List Tile
update msg tile tiles =
    case msg of
        Focus ->
            List.map
                (\x ->
                    { x
                        | fillColor =
                            if (borders x tile) then
                                "blue"
                            else
                                "red"
                    }
                )
                tiles

        UnFocus ->
            List.map
                (\x -> { x | fillColor = "red" })
                tiles

        _ ->
            tiles
