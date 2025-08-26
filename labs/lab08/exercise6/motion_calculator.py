import physics_constants

time = 2.0  # seconds

position = physics_constants.building_height + physics_constants.initial_velocity * time - 0.5 * physics_constants.gravitational_constant * time**2
velocity = physics_constants.initial_velocity - physics_constants.gravitational_constant * time
kinetic_energy = 0.5 * physics_constants.ball_mass * velocity**2

if velocity < 0:
    motion_status = "The ball is falling."
else:
    motion_status = "The ball is rising."

# Display initial conditions
print(f"Initial Position: {physics_constants.building_height:} meters")
print(f"Initial Velocity: {physics_constants.initial_velocity} m/s")
print(f"Time: {time} s")

# Display calculations when time = 2 seconds
print(f"Position: {position:.4f} m")
print(f"Velocity: {velocity:.4f} m/s")

# Display energy analysis when time = 2 seconds
print(f"Kinetic Energy: {kinetic_energy:.4f} J")

print("Motion status:", motion_status)