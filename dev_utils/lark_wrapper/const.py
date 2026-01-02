from enum import StrEnum

class MsgType(StrEnum):
    TEXT = "text"
    IMAGE = "image"
    INTERACTIVE = "interactive"
    AUDIO = "audio"
    MEDIA = "media"
    STICKER = "sticker"
    

class BotStatus(StrEnum):
    OK = "OK"
    FAILED = "FAILED"

class BotType(StrEnum):
    LARK = "lark"
    

