import subprocess
import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
env = os.environ.copy()
env["PYTHONPATH"] = PROJECT_ROOT

print("Starting Controller Server...")

subprocess.run(
    [sys.executable, "controller/controller_server.py"],
    env=env
)