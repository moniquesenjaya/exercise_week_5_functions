def calc_weight_on_planet(weight, gravity = 23.1):
    mass = weight / 9.8
    final_weight = mass * gravity
    print(final_weight)

calc_weight_on_planet(120, 9.8)
calc_weight_on_planet(120)
calc_weight_on_planet(120, 23.1)