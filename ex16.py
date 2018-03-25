from sys import argv

script, filename = argv

print(f"We are going to erase {filename}")
print("if you want to cancle operation press CTRL+C (^C)")
print("if you want to continue, press return")

input("?")
print(f"Opening the file {filename}")
target = open (filename, 'w')

print("Truncating file Goodbye !")
target.truncate()

print("Now I'm going to ask to write three lines ")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write there to file")


target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()
