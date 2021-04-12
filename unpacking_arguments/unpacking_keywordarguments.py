
def named(**kwargs):
    print(kwargs)

#named(name="Bob", age=25)

details = {"name": "Bob", "age": 29}

named(**details)


def named(name, age):
    print(name, age)

details = {"name": "Elvis", "age": 17}

named(**details)


def named(**kwargs):
    print(kwargs)

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name="Elvis", age=17)

   