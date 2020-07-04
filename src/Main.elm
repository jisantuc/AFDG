module Main exposing (main)

import Browser
import Element
    exposing
        ( Element
        , el
        , text
        )
import Element.Background as Background
import Element.Border as Border



---- MODEL ----


type alias Model =
    {}


init : ( Model, Cmd Msg )
init =
    ( {}, Cmd.none )



---- UPDATE ----


type Msg
    = NoOp


update : Msg -> Model -> ( Model, Cmd Msg )
update _ model =
    ( model, Cmd.none )



---- VIEW ----


player1Color : Element.Color
player1Color =
    Element.rgb255 0 255 255


player2Color : Element.Color
player2Color =
    Element.rgb255 255 0 255


withAlpha : Float -> Element.Color -> Element.Color
withAlpha alpha color =
    let
        baseColor =
            Element.toRgb color
    in
    Element.fromRgb { baseColor | alpha = alpha }


tile : Element.Color -> Element msg
tile color =
    text "I'm a tile!"
        |> el
            [ Background.color (withAlpha 0.2 color)
            , Border.width 3
            , Border.color (withAlpha 0.8 color)
            , Element.width Element.fill
            , Element.height Element.fill
            ]


tileSpacing : Int
tileSpacing =
    8


view : Model -> Browser.Document Msg
view _ =
    { title = "A Fairly Dangerous Game"
    , body =
        [ Element.layout [] <|
            Element.column [ Element.height Element.fill, Element.width Element.fill, Element.spacing tileSpacing ]
                [ Element.row [ Element.height Element.fill, Element.width Element.fill, Element.spacing tileSpacing ]
                    [ tile <| player1Color
                    , tile <| player2Color
                    , tile <| player1Color
                    ]
                , Element.row [ Element.height Element.fill, Element.width Element.fill, Element.spacing tileSpacing ]
                    [ tile <| player2Color
                    , tile <| player1Color
                    , tile <| player2Color
                    ]
                ]
        ]
    }



---- PROGRAM ----


main : Program () Model Msg
main =
    Browser.application
        { view = view
        , init = \_ -> \_ -> \_ -> init
        , update = update
        , subscriptions = always Sub.none
        , onUrlRequest = always NoOp
        , onUrlChange = always NoOp
        }
