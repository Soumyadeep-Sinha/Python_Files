print("Program that demonstrate the use of local variables and global variables")
print()
print("LOCAL VARIABLE : ")
# Local Variables
# Local variables are those which are initialized inside a function and belongs only to that particular function. 
# It cannot be accessed anywhere outside the function. 
# Let’s see how to create a local variable.
def loc():
    local_var = "I AM A LOCAL VARIABLE INSIDE THE FUNCTION"
    print(local_var)

loc()
print()
print("GLOBAL VARIABLE : ")
# this will give error

# def local():
#     local_var = "I AM A LOCAL VARIABLE INSIDE THE FUNCTION"
#    print(local_var)

# local()
# print("trying to use the variable outside function.", local_var)

# Global Variables
# The global variables are those which are defined outside any function and which are accessible throughout the program
# i.e.inside and outside of every function Let’s see how to create a global variable.

def glo():
    print("INSIDE THE FUNCTION", global_var)

global_var = "I AM A GLOBAL VARIABLE"

glo()
print("OUTSIDE THE FUNCTION", global_var)

