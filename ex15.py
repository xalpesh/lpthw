from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file name:{filename}")
print(txt.read())

print(f"type your filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
