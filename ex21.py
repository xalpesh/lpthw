def add (a,b):
    print (f"Adding {a} and {b}")
    return a + b

def subtract(a,b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"multiplying {a} * {b}")
    return a * b

def divide (a,b):
    print(f"divide {a} / {b}")
    return a / b

print("Let's do some math with just functions!")
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2 )

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Lets play puzzle")

what = add(age,subtract(height,multiply(weight ,divide(100, 2 ))))

print("That becomes: ", what, "Can you do it by hand?")





