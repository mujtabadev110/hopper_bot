import csv
import os
from datetime import datetime


class TelemetryLogger:

    def __init__(self, folder="telemetry"):
        os.makedirs(folder, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.file_path = os.path.join(folder, f"run_{timestamp}.csv")

        self.file = open(self.file_path, "w", newline="")
        self.writer = csv.writer(self.file)

        # CSV header
        self.writer.writerow([
            "time",
            "hip_pos",
            "knee_pos",
            "hip_vel",
            "knee_vel",
            "hip_tau",
            "knee_tau"
        ])

    def log(self, t, hip_p, knee_p, hip_v, knee_v, hip_tau, knee_tau):
        self.writer.writerow([
            t, hip_p, knee_p, hip_v, knee_v, hip_tau, knee_tau
        ])

    def close(self):
        self.file.close()
        print(f"[Telemetry] Saved → {self.file_path}")