# Task 1: Given the list of temperatures:
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
secWeekTemperatures = temperatures[7:14]
print("Temperatures for the second week:", secWeekTemperatures)
highTemperatures = [temp for temp in temperatures if temp > 100]
print("the temperatures above 100 in this month is", highTemperatures)
