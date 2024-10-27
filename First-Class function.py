def square(x):
    return x*x
def cube(x):
    return x*x*x
f = square      
#assigning a function to a variable without the parentethis
#means it will not be executed but rahter, the variable will be a reference to
#the function and can execute it
print(square)
print(f(5))
#we can pass functions as args to another function
#or return funcion as the result of another function
#those are called a higher order functions

## ----- pass function as arg-------- ##
def my_map(func, arr):
    res = []
    for i in arr:
        res.append(func(i))
    return res

sq = my_map(cube, [1,2,3,4,5])    #do not use parenthesis since it is an argument
print(sq)

##-------return function-------##
def logger(msg):
    def log_msg():
        print('Log:', msg)
    return log_msg

log_hi = logger('Hi!')
print(log_hi)   #returns a reference to the function log_msg inside function logger
log_hi()        #prints the msg


## ------ Example --------- ##
#we want a function that has accepts an html tag
#and returns a function that accepts a message
#and wraps this message in the tag
def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag,msg))
    return wrap_text

h1 = html_tag('h1')     #now the variable h1 is a refrence of the wrap text function
                        #and needs a message to wrap in the h1 tag
h1('Test h1 tag')
h1('another headline') 



