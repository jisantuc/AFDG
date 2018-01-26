module Messages exposing (Msg(..))

{-| This module contains all of the message types that can be used in updates to the
application state


# Exported

@doc Msg, Clear, TileSelect, NewMode

-}

import Types exposing (Mode)
import Tile.Types as TileTypes


{-| Messages that can be sent by user interactions
-}
type Msg
    = Clear
    | TileSelect TileTypes.Tile
    | NewMode Mode
