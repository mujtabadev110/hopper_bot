
import numpy as np


class SinusoidalController:

    def __init__(self):

        # Hip parameters
        self.hip_amp = 30.0
        self.hip_phase = 0.0

        # Knee parameters
        self.knee_amp = 45.0
        self.knee_phase = np.pi

        # Oscillation frequency
        self.frequency = 2.0

    def compute(self, state):

        t = state.time

        omega = 2 * np.pi * self.frequency  

        hip_tau = self.hip_amp * np.sin(
            omega * t + self.hip_phase
        )

        knee_tau = self.knee_amp * np.sin(
            omega * t + self.knee_phase
        )
        hip_tau += 15.0
        knee_tau += 25.0
        return hip_tau, knee_tau