# Simple example of a decorator
def my_decorator_0(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_hello():
    print("Hello!")

# Apply the decorator
decorated_function = my_decorator_0(say_hello)

# Call the decorated function
decorated_function()


# Example of a decorator using the @ symbol
def my_decorator_1(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator_1
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()


# Example of a decorator with arguments
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")


# Example of a decorator with arguments using the @ symbol
def my_decorator(func):  # The decorator accepts a function to decorate
    def wrapper(*args, **kwargs):  # The wrapper can accept any arguments
        print("Something is happening before the function is called.")
        
        # Calls the original function passing all arguments
        result = func(*args, **kwargs)
        
        print("Something is happening after the function is called.")
        return result  # Returns the result of the decorated function
    
    return wrapper  # Returns the wrapper, which replaces the decorated function


@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")

# Utilisation du décorateur
@my_decorator
def greet(name, age=None):
    print(f"Hello, {name}!")
    if age:
        print(f"You're {age} years old.")

# Appeler la fonction décorée
greet("Alice", age=30)



'''
Que font *args et **kwargs dans ce contexte ?

    *args : Permet au décorateur d'accepter un nombre quelconque d'arguments positionnels. Par exemple, si une fonction est appelée comme my_function(1, 2, 3), alors args sera (1, 2, 3).
    **kwargs : Permet au décorateur d'accepter un nombre quelconque d'arguments nommés. Par exemple, si une fonction est appelée comme my_function(a=10, b=20), alors kwargs sera {'a': 10, 'b': 20}
'''

'''
Étapes détaillées :

    Avant l'appel de la fonction :
        Le décorateur remplace greet par wrapper.
        Lorsque vous appelez greet("Alice", age=30), cela exécute en réalité wrapper("Alice", age=30).

    Dans wrapper :
        args devient ("Alice",).
        kwargs devient {'age': 30}.
        La ligne result = func(*args, **kwargs) appelle greet("Alice", age=30).

    Exécution de la fonction originale :
        greet s'exécute normalement avec les arguments fournis.

    Après l'exécution de la fonction :
        Le message "Something is happening after the function is called." est affiché.
'''