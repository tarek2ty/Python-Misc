#a closure is an inner function that has access to local variables
#of the outer functions

def outer():
    msg = "hi"
    def inner():
        print(msg)
    return inner

my_func = outer()   #executing the outer function will return the closure (inner)

my_func()   
my_func()   #this executes the inner function and it remebers the message even if the outer
            #function has finished execution

## ------ Add Parameters ------ ##
def print_func(msg):
    message = msg
    def inner_func():
        print(message)
    return inner_func

hi = print_func('Hi')           #a closure closes the inner function on a specific local
hello = print_func('Hello')     #variable.

hi()
hello()

#we wrote a more complex example on the first class function which used the html tags

## ----- more complex practical example ----- ##
# loggin which function ran with what arguments for better troubleshooting
import logging
logging.basicConfig(filename='example.log',level=logging.INFO)

def logger(func):   #the outer function logs functions that run
    def log_func(*args):    #accept any number of args *args
        logging.info(f'Executed "{func.__name__}" with arguments {args}')
        print(func(*args))  #execute the function and print to the console
    return log_func

# so this function will log the inner function and then execute it

def add(x,y):
    return x+y
def sub(x,y):
    return x-y

add_logger=logger(add)  #we run this variable as our inner function
sub_logger=logger(sub)

add_logger(3,3)
sub_logger(20,10)
#look at the example.log function and we can find the executed functions along with the args
