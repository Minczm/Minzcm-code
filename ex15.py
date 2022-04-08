from sys import argv 

script, filename = argv
# txt = 打开的文件内容
txt = open(filename)
# 阅读打开的文件内容
print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())
