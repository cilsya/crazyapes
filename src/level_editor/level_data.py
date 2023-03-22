# NPC means non-playable character
NPC = []


class Enum_Entity(object):
    # ------------------
    # Static Member variables
    # (Start)
    # ------------------

    SPRITE_PLAYER = 0
    SPRITE_ENEMY = 1
    SPRITE_FIREBALL = 2

    # ------------------
    # Static Member variables
    # (End)
    # ------------------


class Enum(object):
    # ------------------
    # Static Member variables
    # (Start)
    # ------------------

    TILE_EMPTY = 0
    TILE_WALL = 1

    # ------------------
    # Static Member variables
    # (End)
    # ------------------


class Enum_GameState(object):
    # ------------------
    # Static Member variables
    # (Start)
    # ------------------

    # There is no game
    STATE_NULL = 0
    STATE_GAME_IN_PROGRESS = 1
    STATE_GAME_OVER = 2
    STATE_PLAYER_WON = 3

    # ------------------
    # Static Member variables
    # (End)
    # ------------------


class Enum_Tile_IDS(object):
    # ------------------
    # Static Member variables
    # (Start)
    # ------------------

    TILE_EMPTY = 0
    TILE_WALL = 1
    TILE_PLAYER = 2
    TILE_ENEMY = 3

    # ------------------
    # Static Member variables
    # (End)
    # ------------------
