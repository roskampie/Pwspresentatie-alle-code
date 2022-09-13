# Import the os module
import os

cwd = os.getcwd()

print("Current working directory: {0}".format(cwd))

print("os.getcwd() returns an object of type: {0}".format(type(cwd)))
