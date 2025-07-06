from dataclasses import dataclass
from enum import Enum, auto

class CombatType(Enum):
    Quantum = auto()
    Physical = auto()
    Wind = auto()
    Fire = auto()
    Imaginary = auto()
    Lightning = auto()
    Ice = auto()
    Null = auto()
    
class Path(Enum):
    Destruction = auto()
    Hunt = auto()
    Erudition = auto()
    Harmony = auto()
    Nihility = auto()
    Preservation = auto()
    Abundance = auto()
    Remembrance = auto()
    Null = auto()

@dataclass
class Character:
    chinese_name: str = ""
    name: str = ""
    combat_type: CombatType = CombatType.Null
    path: Path = Path.Null
    splash: str = ""
    avatar: str = ""

    @classmethod
    def create(cls):
        return cls()
    
    def set_chinese_name(self, chinese_name: str):
        self.chinese_name = chinese_name
        return self
    
    def set_name(self, name: str):
        self.name = name
        return self
    
    def set_combat_type(self, combat_type: CombatType):
        if isinstance(combat_type, CombatType):
            self.combat_type = combat_type
        else:
            raise ValueError("combat_type must be an instance of CombatType Enum")
        return self

    def set_path(self, path: Path):
        if isinstance(path, Path):
            self.path = path
        else:
            raise ValueError("path must be an instance of Path Enum")
        return self
    
    def set_splash(self, splash: str):
        self.splash = splash
        return self
    
    def set_avatar(self, avatar: str):
        self.avatar = avatar
        return self

    def build(self):
        return self
