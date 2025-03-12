from enum import IntEnum
from typing import Optional

class DebugLevel(IntEnum):
    OFF = 0
    ERROR = 1
    WARN = 2
    INFO = 3
    DEBUG = 4
    TRACE = 5

class DebugManager:
    _instance: Optional['DebugManager'] = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._level = DebugLevel.OFF
        return cls._instance

    @property
    def level(self) -> DebugLevel:
        return self._level

    @level.setter
    def level(self, value: DebugLevel):
        self._level = value

    def should_log(self, level: DebugLevel) -> bool:
        return level <= self._level

    def log(self, level: DebugLevel, component: str, message: str):
        if self.should_log(level):
            level_name = level.name.ljust(5)
            print(f"[{level_name}] [{component}] {message}")

    def error(self, component: str, message: str):
        self.log(DebugLevel.ERROR, component, message)

    def warn(self, component: str, message: str):
        self.log(DebugLevel.WARN, component, message)

    def info(self, component: str, message: str):
        self.log(DebugLevel.INFO, component, message)

    def debug(self, component: str, message: str):
        self.log(DebugLevel.DEBUG, component, message)

    def trace(self, component: str, message: str):
        self.log(DebugLevel.TRACE, component, message)

# Global debug manager instance
debug = DebugManager() 