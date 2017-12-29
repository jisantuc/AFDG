module Main exposing (main)

import Html exposing (Html, div, text)
import Messages exposing (Msg(..))


main : Program Never Model Msg
main =
    Html.beginnerProgram
        { view = view
        , update = update
        , model = model
        }



-- MODEL


type alias Model =
    { name : String
    }


model : Model
model =
    Model "World"


update : Msg -> Model -> Model
update action model =
    case action of
        Reset ->
            model



-- VIEW


view : Model -> Html Msg
view model =
    div [] [ text ("Hello " ++ model.name) ]
