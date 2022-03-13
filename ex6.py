#定义变量人的种类
types_of_people = 10
x = f"There are {types_of_people} types of  people."
#定义变量两种人
binary = "binary" # 二进制
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: {y}")

hilarious = False
joke_evaluation = "Isn't that joke so Funny? {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)