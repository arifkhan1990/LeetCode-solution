def max_souvenirs():
    machine_constraints = [
        (2, 1, 2, 180),  # Machine I constraint (minutes)
        (1, 3, 1, 300), # Machine II constraint (minutes)
        (1, 2, 2, 240)   # Machine III constraint (minutes)
    ]
    max_souvenir_count = 0
    best_combination = None

    for x in range(1, 180):  # maximum possible value of x based on constraint 1
        for y in range(1, 300):  # maximum possible value of y based on constraint 2
            for z in range(1, 241):  # maximum possible value of z based on constraint 3
                if (2*x + y + 2*z <= 180) and (x + 3*y + 1*z <= 300) and (1*x + 2*y + 2*z <= 240):
                    total_souvenirs = x + y + z
                    if total_souvenirs > max_souvenir_count:
                        max_souvenir_count = total_souvenirs
                        best_combination = (x, y, z)

    return max_souvenir_count, best_combination

max_count, best_combo = max_souvenirs()
print("Maximum number of souvenirs:", max_count)
print("Number of Type A souvenirs:", best_combo[0])
print("Number of Type B souvenirs:", best_combo[1])
print("Number of Type C souvenirs:", best_combo[2])
