from enum import IntEnum


class AuthCode(IntEnum):
    LOGIN_ATTEMPT         = 0x10
    LOGIN_CREATE          = 0x20
    LOGIN_CHANGE_PASSWORD = 0x30


class AccountStatus(IntEnum):
    NOACCT = 0x00
    NORMAL = 0x01
    BANNED = 0x02


class LoginResult(IntEnum):
    SUCCESS                 = 0x01
    SUCCESS_CREATE          = 0x03
    SUCCESS_CHANGE_PASSWORD = 0x06
