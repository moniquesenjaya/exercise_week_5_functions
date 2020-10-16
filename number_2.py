def calc_weight_on_planet(weight, gravity = 23.1):
    mass = weight / 9.8
    final_weight = mass * gravity
    return final_weight

print(calc_weight_on_planet(120, 9.8))
print(calc_weight_on_planet(120))
print(calc_weight_on_planet(120, 23.1))