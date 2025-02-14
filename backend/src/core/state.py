from typing import Optional, Dict, Any
from datetime import datetime
from enum import Enum

class NeonStatus(Enum):
    IDLE = "idle"
    LISTENING = "listening"
    PROCESSING = "processing"
    RESPONDING =  "responding"
    ERROR = "error"

class NeonState:
    
    def __init__(self):
        self._status : NeonStatus = NeonStatus.IDLE
        self._last_command: Optional[str] = None
        self._last_response: Optional[str] = None
        self._error: Optional[str] = None
        self._state_history: list = []
        self._last_update: datetime = datetime.now()

    @property
    def status(self) -> NeonStatus:
        return self._status
    
    @status.setter
    def status(self, new_status: NeonStatus) -> None:
        self._status = new_status
        self._last_update = datetime.now()
        self._record_state_change()

    def update(self, state_update: Dict[str, Any]) -> None:
        for key, value in state_update.items():
            if hasattr(self, f"_{key}"):
                setattr(self, f"_{key}", value)
        self._last_updated = datetime.now()
        self._record_state_change()

    def _record_state_change(self) -> None:
        state_snapshot = {
            "status": self._status,
            "last_command": self._last_command,
            "timestamp": self._last_updated
        }
        self._state_history.append(state_snapshot)
        # Keep only last 100 state changes
        if len(self._state_history) > 100:
            self._state_history.pop(0)

    def _current_state(self) -> Dict[str, Any]:
        return {
            "status": self._status,
            "last_command": self._last_command,
            "last_response": self._last_response,
            "error": self._error,
            "last_updated": self._last_updated,
        }