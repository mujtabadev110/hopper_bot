import numpy as np


class LQRController:

    def __init__(self):

        self.K = 0.5 * np.array([
            [20.0,  0.0,  4.0,  0.0],   # hip
            [0.0,  35.0,  0.0,  6.0]    # knee
        ])

        self.hip_amp = 50.0
        self.knee_amp = 70.0
        self.frequency = 2.0
        self.hip_phase = 0.0
        self.knee_phase = np.pi

        # desired equilibrium (upright-ish)
        self.x_ref = np.array([
            -0.3,   # hip angle target
             1.2,   # knee angle target
             0.0,
             0.0
        ])

    def compute(self, state):


        x = np.array([
            state.hip_pos,
            state.knee_pos,
            state.hip_vel,
            state.knee_vel
        ])

        x_error = x - self.x_ref
        u_lqr = -self.K @ x_error


        t = state.time
        w = 2 * np.pi * self.frequency

        hip_gait = self.hip_amp * np.sin(w * t + self.hip_phase)
        knee_gait = self.knee_amp * np.sin(w * t + self.knee_phase)

        hip_tau = u_lqr[0] + hip_gait
        knee_tau = u_lqr[1] + knee_gait

        return hip_tau, knee_tau