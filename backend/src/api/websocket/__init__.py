from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from core.neon import Neon

router = APIRouter()
neon = Neon()  # Get the singleton instance

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()

            if "text" in data:
                command = data["text"] # Text data (commands, status updates)
                result = await neon.handle_command(command)
                await websocket.send_json(result)

            elif "bytes" in data:
                audio_data = data["bytes"]  # Binary data (audio)
                result = await neon.process_voice_command(audio_data)
                await websocket.send_json(result)

    except WebSocketDisconnect:
        pass # Handle disconnect gracefully
