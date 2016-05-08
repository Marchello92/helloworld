import sys

def greeting (name):
   print ("Hello " + name + "!")
   return

if  1 == len(sys.argv):
    greeting (name = "World!")
else:
    greeting (name = sys.argv[1])
