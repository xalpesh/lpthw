#this one is like script wit hargv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#*args has problem, lets try this way
def print_two_again(arg1,arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this takes only one args
def print_one(arg1):
    print(f"arg1: {arg1}")

#this takes no arguments
def print_none():
    print("I got nothing to print")

print_two("Kalpesh","Patel")
print_two_again("Kalpesh","Patel1")
print_one("Only with one args")
print_none()