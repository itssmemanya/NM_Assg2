import math

# True values
true_value_pi = math.pi
true_value_e = math.e
true_value_8fact = math.factorial(8)
true_value_sqrt2 = math.sqrt(2)
true_value_10pi = 10**math.pi

# Approximate values
approximate_value_pi = 3.141 * 10**0
approximate_value_e = 2.718 * 10**0
approximate_value_8fact = 4.032 * 10**4
approximate_value_sqrt2 = 1.414 * 10**0
approximate_value_10pi = 1.385 * 10**3

# Absolute Error
absolute_error_pi = abs(true_value_pi - approximate_value_pi)
absolute_error_e = abs(true_value_e - approximate_value_e)
absolute_error_8fact = abs(true_value_8fact - approximate_value_8fact)
absolute_error_sqrt2 = abs(true_value_sqrt2 - approximate_value_sqrt2)
absolute_error_10pi = abs(true_value_10pi - approximate_value_10pi)

# Relative Error
relative_error_pi = absolute_error_pi / true_value_pi
relative_error_e = absolute_error_e / true_value_e
relative_error_8fact = absolute_error_8fact / true_value_8fact
relative_error_sqrt2 = absolute_error_sqrt2 / true_value_sqrt2
relative_error_10pi = absolute_error_10pi / true_value_10pi

# Displaying the results
print(f" True Value of π : {true_value_pi}")
print(f" Approximate Value : {approximate_value_pi}")
print(f" Absolute Error : {absolute_error_pi}")
print(f" Relative Error : {relative_error_pi}")
print()
print(f" True Value of e : {true_value_e}")
print(f" Approximate Value : {approximate_value_e}")
print(f" Absolute Error : {absolute_error_e}")
print(f" Relative Error : {relative_error_e}")
print()
print(f" True Value of 8! : {true_value_8fact}")
print(f" Approximate Value : {approximate_value_8fact}")
print(f" Absolute Error : {absolute_error_8fact}")
print(f" Relative Error : {relative_error_8fact}")
print()
print(f" True Value of square root 2 : {true_value_sqrt2}")
print(f" Approximate Value : {approximate_value_sqrt2}")
print(f" Absolute Error : {absolute_error_sqrt2}")
print(f" Relative Error : {relative_error_sqrt2}")
print()
print(f" True Value of 10^π : {true_value_10pi}")
print(f" Approximate Value : {approximate_value_10pi}")
print(f" Absolute Error : {absolute_error_10pi}")
print(f" Relative Error : {relative_error_10pi}")

