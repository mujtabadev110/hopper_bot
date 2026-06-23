import pandas as pd
import matplotlib.pyplot as plt
import os


class TelemetryPlotter:

    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self.data = pd.read_csv(csv_path)

    def plot_all(self, save_dir="telemetry/plots"):

        os.makedirs(save_dir, exist_ok=True)

        t = self.data["time"]

        # 1. Joint Positions
        plt.figure()
        plt.plot(t, self.data["hip_pos"], label="Hip")
        plt.plot(t, self.data["knee_pos"], label="Knee")
        plt.title("Joint Positions")
        plt.xlabel("Time (s)")
        plt.ylabel("Position (rad)")
        plt.legend()
        plt.grid()
        plt.savefig(f"{save_dir}/joint_positions.png")
        plt.close()

        # 2. Joint Velocities
        plt.figure()
        plt.plot(t, self.data["hip_vel"], label="Hip")
        plt.plot(t, self.data["knee_vel"], label="Knee")
        plt.title("Joint Velocities")
        plt.xlabel("Time (s)")
        plt.ylabel("Velocity (rad/s)")
        plt.legend()
        plt.grid()
        plt.savefig(f"{save_dir}/joint_velocities.png")
        plt.close()


        # 3. Control Torques
        plt.figure()
        plt.plot(t, self.data["hip_tau"], label="Hip Torque")
        plt.plot(t, self.data["knee_tau"], label="Knee Torque")
        plt.title("Control Torques")
        plt.xlabel("Time (s)")
        plt.ylabel("Torque (Nm)")
        plt.legend()
        plt.grid()
        plt.savefig(f"{save_dir}/joint_torques.png")
        plt.close()

        print(f"Plots saved in: {save_dir}")