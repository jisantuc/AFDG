module Tile.State exposing (..)

{-| State transformations for grid information

@doc addUnit, borders, neighbors, reachable, highlightTiles, update

-}

import Types exposing (Mode(..))
import GameUnit.Util exposing (..)
import Base.Types exposing (Base)
import GameUnit.Types exposing (GameUnit(..))
import Geom.Types exposing (Coord, Color(..))
import Tile.Types exposing (..)
import User.Types exposing (User)


{-| Check whether two tiles border each other
-}
borders : Tile -> Tile -> Bool
borders tile other =
    let
        xDist =
            abs <| tile.location.x - other.location.x

        yDist =
            abs <| tile.location.y - other.location.y

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
                        Color "blue"
                    else if x == tile then
                        Color "red"
                    else
                        Color "none"
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
                    tile.location.x - other.location.x

                yDiff =
                    tile.location.y - other.location.y
            in
                case ( xDiff, yDiff ) of
                    ( 1, _ ) ->
                        not <| List.member West tile.walls || List.member East other.walls

                    ( -1, _ ) ->
                        not <| List.member East tile.walls || List.member West other.walls

                    ( _, -1 ) ->
                        not <| List.member South tile.walls || List.member North other.walls

                    ( _, 1 ) ->
                        not <| List.member North tile.walls || List.member South other.walls

                    _ ->
                        False


{-| Increase the number of units on this tile by one
-}
addUnit : (Coord -> Color -> GameUnit) -> User -> Tile -> List Tile -> List Tile
addUnit f user tile tiles =
    case Maybe.map .ownedBy tile.base of
        Nothing ->
            tiles

        Just user ->
            List.map
                (\x ->
                    if (x == tile) then
                        { x | units = f tile.location user.color :: x.units }
                    else
                        x
                )
                tiles


{-| Put a base on the clicked on tile for the current player if it doesn't have one
-}
addBase : User -> Tile -> List Tile -> List Tile
addBase user tile tiles =
    let
        addBaseToTile tile =
            List.map
                (\x ->
                    if (x == tile) then
                        { x | base = Base user |> Just }
                    else
                        x
                )
    in
        case ( tile.base, .units tile |> List.head ) of
            ( Nothing, Nothing ) ->
                addBaseToTile tile tiles

            ( Nothing, Just gameUnit ) ->
                if (getColor gameUnit == user.color) then
                    addBaseToTile tile tiles
                else
                    tiles

            ( Just _, _ ) ->
                tiles


{-| Remove a base from the clicked on tile if it has one
-}
removeBase : Tile -> List Tile -> List Tile
removeBase tile tiles =
    List.map
        (\x ->
            if (x == tile) then
                { x | base = Nothing }
            else
                x
        )
        tiles


{-| Remove a border from this tile
-}
removeBorder : Tile -> Border -> List Tile -> List Tile
removeBorder tile border tiles =
    List.map
        (\x ->
            if (x == tile) then
                { x | walls = List.filter ((/=) border) x.walls }
            else
                x
        )
        tiles


{-| Add a border to this tile
-}
addBorder : Tile -> Border -> List Tile -> List Tile
addBorder tile border tiles =
    let
        -- awww yeah let's get it point-free
        hasBorder =
            (flip List.member) << .walls
    in
        case hasBorder tile border of
            True ->
                tiles

            False ->
                List.map
                    (\x ->
                        if (x == tile) then
                            { x | walls = border :: x.walls }
                        else
                            x
                    )
                    tiles


{-| Switch two tiles that border each other
-}
switchTiles : List Tile -> Tile -> Tile -> List Tile
switchTiles tiles source target =
    let
        subTile t =
            case ( t == source, t == target ) of
                ( True, False ) ->
                    { target | location = source.location }

                ( False, True ) ->
                    { source | location = target.location }

                _ ->
                    t
    in
        List.map subTile tiles


{-| Maybe switch two tiles, provided the source tile is available
-}
maybeSwitchTiles : List Tile -> Maybe Tile -> Tile -> List Tile
maybeSwitchTiles tiles maybeSourceTile tile =
    case maybeSourceTile of
        Nothing ->
            tiles

        Just source ->
            if ((borders tile source) |> not) then
                tiles
            else
                switchTiles tiles source tile



-- UPDATE


update : Mode -> Maybe Border -> Tile -> List Tile -> List Tile
update mode mbBorder tile tiles =
    case ( mode, mbBorder ) of
        ( Inactive, Nothing ) ->
            List.map (\x -> { x | fillColor = Color "none" }) tiles

        ( Neighbors, Nothing ) ->
            highlightTiles borders tile tiles

        ( Reachable, Nothing ) ->
            highlightTiles reachable tile tiles

        ( AddOafs user, Nothing ) ->
            addUnit newOaf user tile tiles

        ( AddWizards user, Nothing ) ->
            addUnit newWizard user tile tiles

        ( AddBases user, Nothing ) ->
            addBase user tile tiles

        ( RemoveBases, Nothing ) ->
            removeBase tile tiles

        ( AddBorders, Just border ) ->
            addBorder tile border tiles

        ( RemoveBorders, Just border ) ->
            removeBorder tile border tiles

        _ ->
            tiles
