from enum import StrEnum, unique, auto


@unique
class RoleEnum(StrEnum):
    @staticmethod
    def _generate_next_value_(name, *args):
        return name.upper()
    
    ADMIN = auto()
    USER = auto()
    SUPPORT = auto()
