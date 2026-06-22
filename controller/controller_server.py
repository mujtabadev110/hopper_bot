import asyncio
import json
import websockets

from communication.protocol import RobotState

from controller.lqr_controller import LQRController
# from controller.sinusoidal_controller import SinusoidalController

controller = LQRController()


async def handler(websocket):

    print("Simulator connected")

    try:

        async for message in websocket:

            data = json.loads(message)

            state = RobotState(
                data["time"],
                data["hip_pos"],
                data["knee_pos"],
                data["hip_vel"],
                data["knee_vel"]
            )

            hip_tau, knee_tau = controller.compute(state)

            await websocket.send(json.dumps({
                "hip_tau": float(hip_tau),
                "knee_tau": float(knee_tau)
            }))

    except websockets.ConnectionClosed:
        print("Simulator disconnected")


async def main():

    print("Controller running on ws://localhost:8765")

    async with websockets.serve(
        handler,
        "localhost",
        8765
    ):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())