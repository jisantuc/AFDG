module Tile.State exposing (..)

{-| Types and methods for grid information


# Exported Types

@doc Tile, Coord, Border


# Helpers

@doc borders, neighbors, reachable, view

-}

import Types exposing (Mode(..))
import GameUnit.Util exposing (..)
import GameUnit.Types exposing (GameUnit)
import Geom.Types exposing (Coord, Color)
import Tile.Types exposing (..)


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


{-| Color a reference tile red and tiles that meet some condition blue
-}
highlightTiles : (Tile -> Tile -> Bool) -> Tile -> List Tile -> List Tile
highlightTiles cond tile tiles =
    List.map
        (\x ->
            { x
                | fillColor =
                    if (cond x tile) then
                        "blue"
                    else if x == tile then
                        "red"
                    else
                        "none"
            }
        )
        tiles


{-| Check whether a tile is reachable from another tile (no walls)
-}
reachable : Tile -> Tile -> Bool
reachable tile other =
    case (borders tile other) of
        False ->
            False

        True ->
            let
                xDiff =
                    tile.coord.x - other.coord.x

                yDiff =
                    tile.coord.y - other.coord.y
            in
                case ( xDiff, yDiff ) of
                    ( 1, _ ) ->
                        not <| List.member West tile.walls || List.member East other.walls

                    ( -1, _ ) ->
                        not <| List.member East tile.walls || List.member West other.walls

                    ( _, 1 ) ->
                        not <| List.member South tile.walls || List.member North other.walls

                    ( _, -1 ) ->
                        not <| List.member North tile.walls || List.member South other.walls

                    _ ->
                        False


{-| Increase the number of units on this tile by one
-}
addUnit : (Coord -> Color -> GameUnit) -> Tile -> List Tile -> List Tile
addUnit f tile tiles =
    case tile.base of
        Nothing ->
            tiles

        Just b ->
            List.map
                (\x ->
                    if (x == tile) then
                        { x | units = f tile.coord b.ownedBy.color :: x.units }
                    else
                        x
                )
                tiles



-- UPDATE


update : Mode -> Tile -> List Tile -> List Tile
update mode tile tiles =
    case mode of
        Inactive ->
            List.map (\x -> { x | fillColor = "none" }) tiles

        Neighbors ->
            highlightTiles borders tile tiles

        Reachable ->
            highlightTiles reachable tile tiles

        AddOafs ->
            addUnit newOaf tile tiles

        AddWizards ->
            addUnit newWizard tile tiles
