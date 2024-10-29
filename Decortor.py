#we saw first class functions that enable us to treat a function as a normal object
#pass it to a function or return it from a function

#a decorator is very similar to closure.
#it is a function that takes another function as an argument
#and adds functionality without changing the passed function

from typing import Any


def decorator_func(plaine_function): #print a message like the old closure
    def wrapper_func(*args, **kwargs):
        print("ran from inside the decorator")
        return plaine_function(*args, **kwargs)    #instead of printing, execute a function and return the result
    return wrapper_func             #return the inner function

def display():
    print('display func ran!')

decorated_var = decorator_func(display) 
decorated_var()

##------ Syntax -------##
@decorator_func         #means decorate the following function
def display2():         #pass it as an argument to decorator_fun
    print("display2 ran@")  #exactly as saying "display = decorator_func(display)"
display2()

##------ Arguments in the plaine function ------##

#the wrapper function does not accept any argument at the moment
#add *args and **kwargs >> accept any number of positional arguments and keyword arguments
#in the inner function
@decorator_func
def display_info(name, age):
    print(f"ran display info: args {name}, {age}")

display_info("john", 25)

##------- Classes as Decorator -------##
#instead of using a function, we can use classes to decorate
class decorate_class(object):
    def __init__(self, plaine_func):    #the constructor just defines the original function
        self.plaine_func = plaine_func
    def __call__(self, *args, **kwargs):    
        print("Class call method ran as decorator")
        return self.plaine_func(*args, **kwargs)
        
@decorate_class
def display3(name,age):
    print('class decorated {},{}'.format(name,age))

display3('tarek',26)

##------ Logging Example -----##
#create a logging function that logs how many times a function has ran with what args 
import datetime
def my_logger(original_func):
    import logging
    logging.basicConfig(
        filename=f'{original_func.__name__}-{datetime.datetime.now().strftime("%d%m%y")}.log',
        level=logging.INFO
        )
    def wrapper(*args,**kwargs):
        logging.info(
            f'{datetime.datetime.now().strftime("%H:%M:%S")}-{original_func.__name__}: Ran with args:{args} and kwargs:{kwargs}'
        )
        return original_func(*args,**kwargs)
    return wrapper

@my_logger
def display4(name, age):
   print("try the new logger: {}, {}".format(name,age))

display4('tarek', 26)
#check the log file

##----- example timing ----##
#check how many seconds it took a function to run
import time
def timing(original_func):
    def wrapper(*args, **kwargs):
        t1=time.time()
        result = original_func(*args, **kwargs)
        t2=time.time()
        print(f'it took {t2-t1} to run {original_func.__name__}')
        return result
    return wrapper

@timing
def display5():
    time.sleep(1)
    print("Ty")

display5()

##----- Stacking Decorators -----#
#we can simply do
@my_logger
@timing
def display7():
    print("stack decorators")
#but notice that the log file is called wrapper and not the original function name when
#putting the logger function above 
#"display7 = mylogger(timing(display7))" == "display7 = mylogger(wrapper)"
#so it will log wrapper
display7()

#a solution is to use a decorator called wraps
#to preserve the original names
from functools import wraps
#now inside each higher order function, go to the wrapper (inner func) and decorate it with
#@wraps(original_func)
#this will envoke the __name__ to return the name of the original function instead of the inner func
def example(original_func):
    @wraps(original_func)
    def wrapper(*args, **kwargs):
        print("Hello from inside stacked decorator")
        return original_func(*args, **kwargs)
    return wrapper

def display8():
    print("hell")
display8 = example(display8)

display8()
print(display8.__name__) # it will return display8 and not the inner wrapper

##------Decorator with an argument-----##
#if you want the decorator to customise the code that decorates the function 
#using a set of arguments
def prefix_function(prefix):
    def decorator_function(original_function):
        def wrapper(*args,**kwargs):
            print(prefix, 'some code before the function')
            result = original_function(*args, **kwargs)
            print(prefix, 'some code after the function')
            return result
        return wrapper
    return decorator_function
#the extra level is just a way to take the arguments

@prefix_function('LOG: ')
def display9(name, age):
    print(f'arguments in the decorator: args ({name}, {age})')

display9('tarek',88)



