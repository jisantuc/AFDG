module TileTests exposing (..)

import Expect exposing (Expectation)
import Test exposing (..)
import Geom.Types exposing (Color(..), Coord)
import GameUnit.Util exposing (newWizard, newOaf)
import Tile.Types exposing (Tile, Border(..))
import Tile.State exposing (addUnit, borders, reachable)
import User.Util exposing (user1)
import Fuzzers.Tile exposing (tileF, tileListF)


testBorders : Test
testBorders =
    let
        tileAtPoint x y =
            Tile { x = x, y = y } (Color "none") False [] Nothing []

        tile00 =
            tileAtPoint 0 0

        tile01 =
            tileAtPoint 0 1

        tile11 =
            tileAtPoint 1 1

        tile99 =
            tileAtPoint 9 9
    in
        describe "Border tests"
            [ fuzz2 tileF tileF "The bordering relation should be commutative" <|
                \t1 t2 ->
                    Expect.true
                        (toString t1.location ++ toString t2.location)
                        (borders t1 t2 == borders t2 t1)
            , test "Adjacent tiles should compute to bordering each other" <|
                \_ ->
                    Expect.all
                        [ \_ -> Expect.true "Tile00 and Tile01" (borders tile00 tile01)
                        , \_ -> Expect.true "Tile01 and Tile11" (borders tile01 tile11)
                        ]
                        ()
            , test "Non-adjacent tiles should compute to not bordering each other" <|
                \_ ->
                    Expect.all
                        [ \_ -> Expect.false "Tile00 and Tile11" (borders tile00 tile11)
                        , \_ -> Expect.false "Tile00 and Tile99" (borders tile00 tile99)
                        , \_ -> Expect.false "Tile01 and Tile99" (borders tile01 tile99)
                        , \_ -> Expect.false "Tile11 and Tile99" (borders tile11 tile99)
                        ]
                        ()
            ]


testReachable : Test
testReachable =
    let
        tileAtPointWithBorders : Int -> Int -> List Border -> Tile
        tileAtPointWithBorders x y bs =
            Tile { x = x, y = y } (Color "none") False bs Nothing []

        tile00 =
            tileAtPointWithBorders 0 0 []

        tile01 =
            tileAtPointWithBorders 0 1 []

        tile02 =
            tileAtPointWithBorders 0 2 []

        tile10 =
            tileAtPointWithBorders 1 0 []

        tile11 =
            tileAtPointWithBorders 1 1 [ North, South, East, West ]

        tile12 =
            tileAtPointWithBorders 1 2 []

        tile20 =
            tileAtPointWithBorders 2 0 []

        tile21 =
            tileAtPointWithBorders 2 1 []

        tile22 =
            tileAtPointWithBorders 2 2 []

        allTiles =
            [ tile00
            , tile01
            , tile02
            , tile10
            , tile11
            , tile12
            , tile20
            , tile21
            , tile22
            ]

        others t =
            List.filter (\x -> t /= x) allTiles
    in
        describe "Reachable tests"
            [ test "Nothing should be reachable from the fully walled in tile" <|
                \_ ->
                    Expect.all
                        (List.map
                            (\x _ ->
                                Expect.false ("Reachable from middle" ++ toString x.location) <|
                                    reachable tile11 x
                            )
                            (others tile11)
                        )
                        ()
            , fuzz2 tileF tileF "The reachable relation should be commutative" <|
                \t1 t2 ->
                    Expect.true
                        (toString t1.location ++ toString t2.location)
                        (reachable t1 t2 == reachable t2 t1)
            , test "Neighboring pairs of tiles without walls between them should be reachable" <|
                \_ ->
                    Expect.all
                        (List.map
                            (\x ->
                                \_ ->
                                    if (x == tile11) then
                                        Expect.true "Center can reach nothing" (List.all (not << reachable x) (others x))
                                    else
                                        Expect.true
                                            "Tiles border their neighbors except the walled off tile"
                                            (((List.map
                                                (\y ->
                                                    if (y == tile11) then
                                                        not <| reachable x y
                                                    else
                                                        (reachable x y == borders x y)
                                                )
                                              )
                                                (others x)
                                             )
                                                |> List.foldl
                                                    (&&)
                                                    True
                                            )
                            )
                            allTiles
                        )
                        ()
            ]


testAddUnits : Test
testAddUnits =
    let
        tileAtPoint x y =
            Tile { x = x, y = y } (Color "none") False [] Nothing []

        tile00 =
            tileAtPoint 0 0

        tile01 =
            tileAtPoint 0 1

        tiles =
            [ tile00
            , tile01
            ]

        getAllUnits =
            List.foldl (++) [] << List.map .units
    in
        describe "Game unit state with tiles tests"
            [ test "Units can't be added to non-bases" <|
                \_ ->
                    Expect.all
                        [ \_ ->
                            Expect.equal (getAllUnits <| addUnit newWizard user1 tile00 tiles) []
                        , \_ ->
                            Expect.equal (getAllUnits <| addUnit newOaf user1 tile00 tiles) []
                        , \_ ->
                            Expect.equal (getAllUnits <| addUnit newWizard user1 tile01 tiles) []
                        , \_ ->
                            Expect.equal (getAllUnits <| addUnit newOaf user1 tile01 tiles) []
                        ]
                        ()
            , fuzz tileListF "Adding units only affects the target tile" <|
                \ts ->
                    let
                        firstTile =
                            List.head tiles

                        addOafToTile =
                            flip (addUnit newOaf user1) ts

                        addWizardToTile =
                            flip (addUnit newWizard user1) ts

                        testFromUnitAdd f ft =
                            case ft of
                                -- This is a trivial case that can't be exercised
                                -- in real life
                                Nothing ->
                                    Expect.true "Trivial" True

                                Just t ->
                                    Expect.equal
                                        (List.map2 (\x y -> .units x == .units y) (f t) ts)
                                        (List.map (\x -> .location x /= .location t) ts)
                    in
                        Expect.all
                            [ \_ ->
                                testFromUnitAdd addOafToTile firstTile
                            , \_ ->
                                testFromUnitAdd addWizardToTile firstTile
                            ]
                            ()
            , fuzz tileF "Adding a unit adds exactly one unit" <|
                \tile ->
                    let
                        nUnits ts =
                            (List.map (List.length << .units) ts) |> List.sum
                    in
                        Expect.all
                            [ \_ ->
                                Expect.equal
                                    (addUnit newOaf user1 tile [ tile ] |> nUnits)
                                    (nUnits [ tile ] + 1)
                            , \_ ->
                                Expect.equal
                                    (addUnit newWizard user1 tile [ tile ] |> nUnits)
                                    (nUnits [ tile ] + 1)
                            ]
                            ()
            ]
