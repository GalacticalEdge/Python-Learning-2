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

o = "Octopus" 
oo = " Octopus "
ooo = "Octopus,wins"
print(o[3:5]) # This will print out the letters between the third and fifth letters in o

print(o[:5]) # This will print up to the fifth letter in o

print(o[2:]) # This will print whatever is after the second letter in o

print(o[-5:-2]) # IDK how to describe this

print(o.upper()) # This will print o, but completely uppercase

print(o.lower()) # This will print o, but completely lowercase

print(oo.strip()) # This removes any whitespace at the beginning or end

print(o.replace("O", "0")) # This will replace the O in "Octopus" with a zero

print(ooo.split(",")) # This will create a split between the coma and the word "wins"

# Left off on Python Format Strings

sales = "Our product sold {} units"
salesnum = "700,000"

print(sales.format(salesnum)) # This will have the "{}" show the "salesnum"

place1 = "Japan"
place2 = "Italy"
place3 = "Eygpt"

visitplaces = "I want to visit {}, {}, and {}"

print(visitplaces.format(place1, place2, place3)) # But we can also add multiple variables to format strings

print("He was a so-called \"hero\" who saved the world") # When using for example double quotes, it conflicts with the double quotes that are already in the string. To fix that, you name to add \"Quote here\" (Escape characters) to the double quotation marks inside like shown in the code

# Left off on Python Booleans

print(300 > 600) # This will compare the values of the two variables and will report if the result is true or false

tt = 89
rr = 212

if tt < rr:
    print("tt is less than rr") # This will appear if the result is true
else:
    print("tt is not less than rr") # This will appear if the result is false

print(bool("Hello")) # These booleans allows us to evaluate any value, and give a true or false in return
print(bool(rr)) # And to let you know, most values are true except for the number 0, "None" and empty values (Such as (), {}, etc.)

# Left off on Python Operators

grocerylist = ["Apple", "Juice", "Bread"]
print(grocerylist) # This will print out the "list"
print(len(grocerylist)) # This will tell us how many items are in the "list"
print(grocerylist[1]) # This will show the item that the listed variable. The order usually starts with 0, so adding "0" here would have gotten us "Apple"
print(grocerylist[-1]) # This will do the same thing as the previous command, but it will do it in the opposite way.
print(grocerylist[1:3]) # This will specify the range we want to list.
print(grocerylist[:2]) # This will specify that we want to list up to the second item in the list.
print(grocerylist[2:]) # This will list items that come after the one we listed in this command
if "Juice" in grocerylist: # We can also check for specific items in lists
    print("We have juice in this list")

grocerylist[1] = "Orange" # We can also change certain items in a list (and they presist)
print(grocerylist)

grocerylist[0:2] = ["Kiwi", "Yogurt"] # It's also possible to change multiple items in a list
print(grocerylist)

grocerylist[1:2] = ["Cereal", "Water"] # If you add more items than you replace, it will be added into the list
print(grocerylist)

grocerylist.insert(2, "Watermelon") # A another (and better) way of adding items into the list is by inserting items, and best of all, you can specify the order.
print(grocerylist)

grocerylist.append("Meat") # Another method that is useful when you don't need to add something into a specific order is using the "append" method. It adds the item at the end of the list
print(grocerylist)

grocerylist.insert(1, "Cherry") # This command will change the item in the listed order.
print(grocerylist)

clothes = ["Pants", "Shirts", "Socks"]

grocerylist.extend(clothes) # This will combine the "grocerylist" and "clothes" variables
print(grocerylist)

# Left off on Python Remove List Items