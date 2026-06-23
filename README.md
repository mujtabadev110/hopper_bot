# 🤖 Hopper Robot Control using MuJoCo & WebSockets

A modular robotics control framework for a two-link hopping robot simulated in MuJoCo. The project demonstrates a distributed control architecture where the simulator and controller operate as independent processes and exchange data through a real-time WebSocket communication layer.

This design closely resembles real robotic systems, where control software and hardware are separated by a communication interface rather than sharing a single execution loop.

---

## ✨ Features

- Real-time WebSocket communication
- Two-link hopping robot simulation in MuJoCo
- External LQR-based controller
- Hybrid hopping strategy with periodic excitation
- Telemetry logging to CSV
- Automatic plot generation and analysis
- Modular and extensible software architecture

---

## 🏗️ Project Structure

```text
hopper_websocket_control/
│
├── communication/
│   └── protocol.py
│
├── controller/
│   ├── controller_server.py
│   └── lqr_controller.py
│
├── simulator/
│   └── simulator.py
│
├── telemetry/
│   ├── logger.py
│   ├── csv/
│   └── plots/
│
├── models/
│   └── hopper_robot.xml
│
├── run_controller.py
├── run_simulator.py
├── requirements.txt
└── README.md
```

---

## 📖 Overview

Traditional MuJoCo projects often embed control logic directly within the simulation loop. While simple, that approach differs from how robotic systems are deployed in practice.

In this project, the controller and simulator run as separate processes and communicate through WebSockets. This architecture improves modularity, simplifies controller development, and mirrors real-world robot-controller communication.

---

## 🦿 Robot Model

The hopper is implemented in MuJoCo using XML and consists of:

### Base Body

- Horizontal sliding joint (X-axis)
- Vertical sliding joint (Z-axis)

### Leg Mechanism

- Actuated hip joint
- Actuated knee joint
- Contact foot represented by a sphere

### Actuation

- Hip motor actuator
- Knee motor actuator

The robot generates hopping motion by applying torque commands to the hip and knee joints.

---

## 🔄 Communication Architecture

The simulator and controller exchange data through a lightweight WebSocket protocol.

```text
MuJoCo Simulator
        │
        ▼
 Robot State
        │
        ▼
 WebSocket Client
        │
        ▼
 WebSocket Server
        │
        ▼
   Controller
        │
        ▼
 Torque Commands
        │
        ▼
MuJoCo Simulator
```

### Robot State Message

The simulator sends state information to the controller in JSON format:

```json
{
  "time": 0.123,
  "hip_pos": -0.42,
  "knee_pos": 0.81,
  "hip_vel": 0.15,
  "knee_vel": -0.20
}
```

| Field | Description |
|---------|-------------|
| `time` | Simulation time |
| `hip_pos` | Hip joint angle |
| `knee_pos` | Knee joint angle |
| `hip_vel` | Hip joint velocity |
| `knee_vel` | Knee joint velocity |

### Torque Command Message

The controller computes torques and returns:

```json
{
  "hip_tau": 15.2,
  "knee_tau": -8.4
}
```

| Field | Description |
|---------|-------------|
| `hip_tau` | Hip motor torque |
| `knee_tau` | Knee motor torque |

---

## 🎯 Controller Design

### Linear Quadratic Regulator (LQR)

The primary controller is a state-feedback Linear Quadratic Regulator:

```text
u = -Kx
```

where:

- `x` = system state vector
- `K` = feedback gain matrix
- `u` = control input vector

State vector:

```text
x = [
    hip_position,
    knee_position,
    hip_velocity,
    knee_velocity
]
```

The controller is designed to:

- Stabilize the hopper
- Reduce oscillatory behavior
- Maintain a desired leg configuration
- Reject disturbances

### Hybrid Hopping Strategy

A pure LQR controller typically stabilizes the robot near an equilibrium point without producing continuous hopping.

To generate dynamic motion, a periodic excitation term is added:

```text
Torque = LQR Output + Sinusoidal Excitation
```

#### LQR Contribution

- Stability
- Balance
- Disturbance rejection

#### Sinusoidal Contribution

- Periodic leg motion
- Hopping excitation
- Rhythmic actuation

This hybrid approach produces stable hopping behavior while remaining computationally lightweight.

---

## 📊 Telemetry & Logging

The project includes a telemetry subsystem for performance monitoring and analysis.

### Logged Variables

- Time
- Hip position
- Knee position
- Hip velocity
- Knee velocity
- Hip torque
- Knee torque

### CSV Output

```text
telemetry/csv/telemetry.csv
```

### Generated Plots

```text
telemetry/plots/telemetry_plot.png
```

Generated visualizations include:

- Joint positions
- Joint velocities
- Joint torques

These plots are useful for controller tuning and performance evaluation.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| MuJoCo | Physics simulation |
| Python | Core implementation |
| NumPy | Numerical computation |
| WebSockets | Real-time communication |
| Matplotlib | Data visualization |

---

## 🚀 Installation

### Create a Python Environment

```bash
conda create -n mujoco python=3.12
conda activate mujoco
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### 1. Start the Controller

Open a terminal and run:

```bash
python run_controller.py
```

Expected output:

```text
Starting Controller Server...
Controller running on ws://localhost:8765
```

### 2. Launch the Simulator

Open a second terminal and run:

```bash
python run_simulator.py
```

Expected output:

```text
Simulator connected
```

A MuJoCo viewer window should appear.

### 3. Run the Simulation

During execution the simulator will:

1. Read robot state from MuJoCo
2. Send state data to the controller
3. Receive torque commands
4. Apply torques
5. Advance the simulation
6. Record telemetry data

### 4. Analyze Results

After closing the simulator:

#### CSV File

```text
telemetry/csv/telemetry.csv
```

#### Plot File

```text
telemetry/plots/telemetry_plot.png
```

---

## 🔮 Future Improvements

Potential extensions include:

- Model Predictive Control (MPC)
- Reinforcement Learning
- Central Pattern Generators (CPG)
- State Estimation
- ROS 2 Integration
- Trajectory Optimization
- Hardware Deployment

---

## 👥 Authors

**Ghulam Mujtaba**  
**Faizan Laique Khan**  
**Junaid Adil Hussain**

### Academic Context

Robot Programming Course Project  
ITMO University

---

## 📜 License

This project was developed for educational and research purposes as part of the Robot Programming course at ITMO University.
