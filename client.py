import websockets
import asyncio
from aioconsole import aprint

uri = "ws://8.tcp.ngrok.io:14844"


async def receiver(websocket):
    """listener for client"""
    while True:
        message = await websocket.recv()
        await aprint(message)


async def main():
    """Driver code for client module"""
    async with websockets.connect(uri) as websocket:
        task1 = asyncio.create_task(receiver(websocket))
        await task1

asyncio.run(main())