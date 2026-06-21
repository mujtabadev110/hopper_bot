import json


class RobotState:

    def __init__(
        self,
        time,
        hip_pos,
        knee_pos,
        hip_vel,
        knee_vel,
    ):
        self.time = float(time)
        self.hip_pos = float(hip_pos)
        self.knee_pos = float(knee_pos)
        self.hip_vel = float(hip_vel)
        self.knee_vel = float(knee_vel)

    def to_json(self):

        return json.dumps({
            "time": self.time,
            "hip_pos": self.hip_pos,
            "knee_pos": self.knee_pos,
            "hip_vel": self.hip_vel,
            "knee_vel": self.knee_vel
        })


class TorqueCommand:

    def __init__(self, hip_tau, knee_tau):

        self.hip_tau = float(hip_tau)
        self.knee_tau = float(knee_tau)

    def to_json(self):

        return json.dumps({

            "hip_tau": self.hip_tau,
            "knee_tau": self.knee_tau

        })

    @staticmethod
    def from_json(msg):

        obj = json.loads(msg)

        return TorqueCommand(
            obj["hip_tau"],
            obj["knee_tau"]
        )