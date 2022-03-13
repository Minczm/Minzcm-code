# 引入参数变量argv
from sys import argv
# 解包给四个变量
script, first, ssecond, third = argv

print("The scrip is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", ssecond)
print("Your third variable is:", third)
