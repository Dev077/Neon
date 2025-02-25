# backend/src/test_websocket.py

import asyncio
import websockets
import json

async def test_websocket():
    """Simple WebSocket client to test our endpoint"""
    uri = "ws://localhost:8000/ws"
    async with websockets.connect(uri) as websocket:
        # Test with text command
        message = {"text": "What time is it?"}
        print(f"Sending: {message}")
        await websocket.send(json.dumps(message))
        
        # Receive response
        response = await websocket.recv()
        print(f"Received: {response}")
        
        # Add a small delay to prevent immediate disconnect
        await asyncio.sleep(0.1)

if __name__ == "__main__":
    asyncio.run(test_websocket())