# Define the constraints
machine_constraints = [
    (2, 1, 2, 180),  # Machine I constraint (minutes)
    (1, 3, 1, 300), # Machine II constraint (minutes)
    (1, 2, 2, 240)   # Machine III constraint (minutes)
]

# Define the objective function
def objective_function(x, y, z):
    return x + y + z

# Initialize variables
best_solution = None
max_devices = 0

# Iterate over all possible combinations of devices
for x in range(1,181):  # Type A devices
    for y in range(1,301):  # Type B devices
        for z in range(1,241):  # Type C devices
            # Check if the current combination satisfies all constraints
            constraints_satisfied = all(
                (a*x + b*y + c*z <= limit) for a, b, c, limit in machine_constraints
            )
            if constraints_satisfied:
                # Calculate the objective function value for the current combination
                current_devices = objective_function(x, y, z)

                # Update the best solution if the current combination yields more devices
                if current_devices > max_devices:
                    max_devices = current_devices
                    best_solution = (x, y, z)

# Print the optimal solution
print("Number of Type A souvenirs:", best_solution[0])
print("Number of Type B souvenirs:", best_solution[1])
print("Number of Type C souvenirs:", best_solution[2])
