import numpy as np
import matplotlib.pyplot as plt

# Set parameters for simulation
arena_size = 10  # size of the square arena
step_size = 0.1  # size of each step taken by the robot
num_steps = 1000  # number of steps to simulate

# Initialize robot position at center of arena
robot_pos = np.array([arena_size / 2, arena_size / 2])

# Initialize empty arrays to store robot position over time
x_values = np.zeros(num_steps)
y_values = np.zeros(num_steps)

# Simulate robot motion
for i in range(num_steps):
    # Calculate random angle for robot to turn
    theta = np.random.uniform(-np.pi, np.pi)

    # Calculate new robot position after taking a step in the current direction
    step_vec = step_size * np.array([np.cos(theta), np.sin(theta)])
    new_pos = robot_pos + step_vec

    # Check if robot has collided with the arena boundary
    if (new_pos < 0).any() or (new_pos > arena_size).any():
        # If so, don't update robot position but rotate robot for a random duration
        theta_rot = np.random.uniform(-np.pi, np.pi)
        step_vec_rot = step_size * \
            np.array([np.cos(theta_rot), np.sin(theta_rot)])
        new_pos = robot_pos + step_vec_rot

    # Update robot position
    robot_pos = new_pos
    x_values[i] = robot_pos[0]
    y_values[i] = robot_pos[1]

# Plot robot motion
fig, ax = plt.subplots()
ax.plot(x_values, y_values)
ax.set_xlim([0, arena_size])
ax.set_ylim([0, arena_size])
ax.set_aspect('equal')
ax.set_title('Brownian Motion Simulation')
ax.set_xlabel('X position')
ax.set_ylabel('Y position')
plt.show()
