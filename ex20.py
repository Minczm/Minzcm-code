from sys import argv
script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())
# 储存打开的文件内容
current_file = open(input_file)

print("First let's print the whole file:\n")
# 打印文件内容
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
# 调用rewind方法
rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file )

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)