import sys

def greeting (name):
   print ("Hello " + name + "!")
   return

if  1 == len(sys.argv):
    greeting (name = "to all Coodcoolers")
else:
    greeting (name = sys.argv[1])
