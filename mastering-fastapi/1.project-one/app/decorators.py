def fence(func):
    def wrapper():
        print("+" * 10)
        func()
        print("+" * 10)
    return wrapper

@fence
def log():
    print("decorated")

log()

def testing(func1):
    def wrapper_func():
        name = "Eric"
        age = 50
        print(f"Name: {name}, Age: {age}")
        func1()
        name = "Mary"
        age = 30
        print(f"Name: {name}, Age: {age}")
    return wrapper_func

@testing
def display():
    print("Couple Info")

display()