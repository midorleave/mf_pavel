def add(x, y):
    result = x + y 
    print(result)

add(5, 3)

def say_hello(name, surname):
    print(f"Hello {name} {surname}")

say_hello(name = "Elvis", surname = "SB")

def divide(dividend, divisor):
    if divisor != 0:
         print(dividend / divisor)
    else:
        print("Nope.")


divide(dividend = 15, divisor = 0)

