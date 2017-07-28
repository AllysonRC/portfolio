
from random import *


#Create the list of words you want to choose from.
line1 = ["soft like a meadow", "haikus can be weird", "who are you today"]
line2 = ["and often times don't make sense,", "you are a mystery here", "you finally learn to love"]
line3 = ["refridgerator", "blowing like the wind", "are you lost today?"]

#Generates a random integer.
x = randint(0, len(line1)-1)
y = randint(0, len(line2)-1)
z = randint(0, len(line3)-1)

print("here's a haiku:")
print (line1[x])
print(line2[y])
print(line3[z])
