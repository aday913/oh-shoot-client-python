import asyncio
import websockets

async def send_and_receive():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        print(f"Connected to {uri}")

        async def send():
            while True:
                msg = input("You: ")
                await websocket.send(msg)

        async def receive():
            async for message in websocket:
                print(f"\nReceived: {message}")

        await asyncio.gather(send(), receive())

if __name__ == "__main__":
    asyncio.run(send_and_receive())


