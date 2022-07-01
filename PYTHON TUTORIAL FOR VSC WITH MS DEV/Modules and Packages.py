# What's Module?
#-A python file with functions, classes and other components
#Why use modules?
#- Break code down into reusable structures

#helpers.py
# def display (mesage, is_warning=False):
#     if is_warning:
#         print ("Warning!")
#     print (message)
# all of these three method do same thing
# import module as namespace
import helpers  # it's importing all functions in helpers
helpers.display ("Not a warning") #helpers. after dot you can type the function you want in helpers

#import all into current namespace
from helpers import *  # * is importing all functions in helpers
display("message: ",is_warning=True)

#import specific items into current namespace
from helpers import display
display ("Not a warning")


# Packages
# install an individual package
# pip install colorama

# #install from a list of Packages
# pip install -r requirements.txt

# #requirements.txt
# colorama


