from typing import Optional, Dict, Any
from .config import get_settings
from .state import NeonState

class Neon:
    _instance = None # singleton instance

    def __new__(cls): # singleton pattern implementation, ensures only one instance of Neon is created
        if cls._instance is None:
            cls._instance = super(Neon, cls).__new__(cls)
        return cls._instance

    def __init__(self):# only initialize once
        self.settings = get_settings()
        self.state = NeonState()
        self._initialized = True

    async def priccess_voice_command(self, voice_data: bytes) -> Dict[str, Any]: # for proccessing voice commands
        return {"status": "processing", "command": "placeholder"} # Placeholder for voice processing

    async def handle_command(self, command: str) -> Dict[str, Any]: #  Handle processed commands
        return {"statues": "success", "response": f"Processed command: {command}"} # Placeholder for command handling

    def update_state(self, new_state: Dict[str, Any]) -> None: #update Neon's internal State
        elf.state.update(new_state) # Update the state of the application

        



