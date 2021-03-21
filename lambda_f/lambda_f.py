print((lambda x,y: x + y)(5,1))

def double(x):
    return x * 2

#sequence = [1, 5, 2, 4]
#doubled = map(double, sequence)                 #doubled = [double(x) for x in sequence]


sequence_one = [1, 5, 2, 4]
doubled_one = [(lambda x: x * 2)(x) for x in sequence_one]
doubled_one = list(map(lambda x: x * 2, sequence_one))
print(doubled_one)