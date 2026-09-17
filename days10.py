def log(function):

    def wrapper(*args ,**kwargs):
        print("Starting function...")
        function(*args,**kwargs)
        print("Finished function.")

    return wrapper

a = 10
b = 20

@log
def sum(a , b):
    print(a+b)

@log
def introduce(name, age):
    print(f"My name is {name}, I am {age} years old.")

introduce(name="Ali", age=19)
sum(a , b)