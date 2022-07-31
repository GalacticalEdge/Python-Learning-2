if 14 > 13.5:
    print("14 is greater than 13.5")

x = 5
x = "lifes left"
y = 3.545453
z = 1j

print(x)

# Left off on Python Variable Names

myvariable = "Joey"

print(myvariable)

print("Here are some grouped value")

ac, bc, cc = "Soda", "Juice", "Water"

print(ac)
print(bc)
print(cc)

print("Here is an unpacked collection")

colors = ["red", "orange", "yellow"]
aa, ab, ac = colors
print(aa)
print(ab)
print(ac)

print("Here are some output variables")

zx = "Python"
zy = "is"
zz = "life"
print(zx, zy, zz)

print("Here is a global variable")

rr = " cool"

def myfunc():
    print("Python is" + rr)
myfunc()

# Left off on Python Data Types

print(type(x))
print(type(y))
print(type(z))

import random

print(random.randrange(1, 10))

# Left off on Python Casting

yy = int(3.5) # This number will be 3 since it's looking for an integer
print(yy)

w = float(1) # This number will 1.0 since float adds a decimal to the number
print(w)

g = str("s7") # This does not affect the number regardless of it's format
print(g)

p = "Hello, World!"
print(p[0]) # This will print out a letter from 'p' depending on the variable in this line

pp = "Hello, World!"
print(pp[random.randrange(-1, 13)]) # And for fun, let's add this random letter thingy from earlier

for uu in "apples": # This will print out the word "apples" vertically instead of horizontally
    print(uu)      

print(len(p)) # This will tell us the length of the variable 'p' which is "Hello, World!"

txt = "The best things in life are free!" 
print("free" in txt) # This will tell us if there is the world "free" in the variable 'txt'

if "free" in txt:
    print("Yes, 'free' is present") # But for something better, we can have it print out what we ask it for if the world "free" is present

print("expensive" not in txt) # This will tell us if the word "expensive" is not in the variable 'txt'

if "expensive" not in txt:
  print("No, 'expensive' is not present in the variable 'txt'.") # But again, we can tell it to print something we want if the word "expensive" is not present

# Left off on Python Slicing Strings 