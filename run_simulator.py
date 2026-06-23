import subprocess
import os
import time

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

env = os.environ.copy()
env["PYTHONPATH"] = PROJECT_ROOT

print("Waiting for controller to start...")
time.sleep(2)

print("Starting Simulator...")

subprocess.run(
    ["mjpython", "simulator/simulator.py"],
    cwd=PROJECT_ROOT,
    env=env
)