from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import json
from core.neon import Neon

router = APIRouter()
neon = Neon()  # Get the singleton instance

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time communication"""
    await websocket.accept()
    try:
        while True:
            # Receive message
            data = await websocket.receive_text()
            
            # Parse JSON
            try:
                message = json.loads(data)
                if "text" in message:
                    # Text command
                    command = message["text"]
                    result = await neon.handle_command(command)
                    await websocket.send_json(result)
                elif "bytes" in message:
                    # We'll handle binary data differently
                    await websocket.send_json({"status": "error", "message": "Binary data not yet supported"})
            except json.JSONDecodeError:
                # Handle plain text fallback
                result = await neon.handle_command(data)
                await websocket.send_json(result)
                
    except WebSocketDisconnect:
        print("Client disconnected")
