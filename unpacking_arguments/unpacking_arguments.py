def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total *= arg
    
    return total


print(multiply(2, 4, 6))

def add(x, y, z):
    return x + y + z 

nums = {"x": 2,"y": 4,"z": 6}
print(add(**nums))

def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."

print(apply(1, 2, 3, 4, operator = "+"))
