# 车的数量
cars = 100
# 每辆车的空间
space_in_a_car = 4
# 司机数量
drivers = 30
# 乘客数量
passengers = 90
# 不开车的司机数量
cars_not_driven = cars - drivers
# 开车司机数量
cars_driven = drivers
# 承载数量
carpool_capacity = cars_driven * space_in_a_car
# 每辆车的乘客数量
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
