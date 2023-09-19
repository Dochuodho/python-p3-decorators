def hello(name):
    print("Hello from the hello() function")

    def greet():
        print("Greetings from the greet() function")

    return greet 

print(hello("Guidoo")())


def decorator(func):
    def wrapper():
        print("I am the output that lets you know the function is about to be called.")
        func()
        print("I am the output that lets you know the function has been called.")
    return wrapper

@decorator

def get_called():
    print("I am the function and I am being called.")

get_called()


def check_working_hours(func):
    def wrapper(time):
        if 1100 < time < 2100:
            func(time)

        else:
            print("I'm off duty!")

    return wrapper

@check_working_hours
def sweep_floors(time):
    print("Sweeping the floors...")
@check_working_hours
def wash_dishes(time):
    print("Washing the dishes...")

@check_working_hours
def chop_vegetables(time):
    print("Chopping the vegetables...")

sweep_floors(800)

wash_dishes(1000)

chop_vegetables(1200)
