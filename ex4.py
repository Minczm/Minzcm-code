#车数量
cars = 100
#一辆车的容量
space_in_a_car = 4.0
#司机
drivers = 30
#乘客
passengers = 90
#不能使用的车辆数
cars_not_driven = cars - drivers
#能用的车辆数
cars_driven = drivers
#总容纳数
carpool_capacity = cars_driven * space_in_a_car
#平均几个乘客坐一车
average_passengers_per_car = passengers / cars_driven


print("这里有", cars, "辆车能活动.")
print("这里只有", drivers, "名司机.")
print("将有", cars_not_driven, "辆车今天不能使用.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")