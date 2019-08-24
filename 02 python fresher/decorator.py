# A decorator is just a function that gets called before another function

import functools  # function tools

def my_decorator(f):
    @functools.wraps(f)
    def function_that_runs_f():
        print("Hello!")
        f()
        print("After!")
    return function_that_runs_f

@my_decorator
def a():
    print("I'm in the function.")

a()
