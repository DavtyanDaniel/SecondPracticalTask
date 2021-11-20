import websockets
import datetime as dt
import asyncio
from pyngrok import ngrok
import constants
from moon import Moon


async def coordinates_to_send():
    moon = Moon()
    moon_coordinates = await moon.computing_the_coordinates()
    return str(moon_coordinates)


async def
