# Task 2: The Floating Point Trap

precision_check = 0.1 + 0.2 == 0.3
print(f"without rounding check is {precision_check}") # False

float_sum = 0.1 + 0.2
rounded_float_check = round(float_sum, 2) == round(0.3, 2)
print(f"after rounding check is {rounded_float_check}") # True