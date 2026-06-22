import sys
import os
import asyncio
import json
import time

import mujoco
import mujoco.viewer
import websockets

# project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from communication.protocol import RobotState


class HopperSimulator:

    def __init__(self, xml_path="models/hopper_robot.xml"):

        self.model = mujoco.MjModel.from_xml_path(xml_path)
        self.data = mujoco.MjData(self.model)

        self.qadr = {
            "hip": self.model.jnt_qposadr[self.model.joint("hip").id],
            "knee": self.model.jnt_qposadr[self.model.joint("knee").id]
        }

        self.vadr = {
            "hip": self.model.jnt_dofadr[self.model.joint("hip").id],
            "knee": self.model.jnt_dofadr[self.model.joint("knee").id]
        }

        self.data.qpos[self.qadr["hip"]] = -0.5
        self.data.qpos[self.qadr["knee"]] = 0.8

        mujoco.mj_forward(self.model, self.data)

    async def run(self):

        uri = "ws://localhost:8765"

        async with websockets.connect(uri) as websocket:

            viewer = mujoco.viewer.launch_passive(self.model, self.data)
            timestep = self.model.opt.timestep

            while viewer.is_running():

                state = RobotState(
                    self.data.time,
                    self.data.qpos[self.qadr["hip"]],
                    self.data.qpos[self.qadr["knee"]],
                    self.data.qvel[self.vadr["hip"]],
                    self.data.qvel[self.vadr["knee"]]
                )

                await websocket.send(state.to_json())

                reply = await websocket.recv()
                cmd = json.loads(reply)

                hip_tau = cmd["hip_tau"]
                knee_tau = cmd["knee_tau"]

                self.data.ctrl[0] = hip_tau
                self.data.ctrl[1] = knee_tau

                mujoco.mj_step(self.model, self.data)


                viewer.sync()

                time.sleep(timestep)

            viewer.close()


if __name__ == "__main__":
    sim = HopperSimulator()
    asyncio.run(sim.run())