if 14 > 13.5:
    print("14 is greater than 13.5") # This will tell you which number is greater

x = 5
y = 3.545453
z = 1           # These are variables (in this cases, these are str, which is short for string)

print(x) # This will print out x, which is 5

# Left off on Python Variable Names

myvariable = "Joey"

print(myvariable)

ac, bc, cc = "Soda", "Juice", "Water" # This is a grouped variable

print(ac)
print(bc)
print(cc)

colors = ["red", "orange", "yellow"] # This is an unpacked collection
aa, ab, ac = colors
print(aa)
print(ab)
print(ac)

zx = "Python"
zy = "is"
zz = "life"
print(zx, zy, zz) # These are output variables

rr = " cool"

def myfunc(): # This is a global variable
    print("Python is" + rr)
myfunc()

# Left off on Python Data Types

print(type(x))
print(type(y))
print(type(z))

from queue import Empty
import random # This will import a Python module, which is "random" in this case

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

grocerylist.insert(1, "Cherry") # This command will insert the item in the listed order.
print(grocerylist)

clothes = ["Pants", "Shirts", "Socks"]

grocerylist.extend(clothes) # This will combine the "grocerylist" and "clothes" variables
print(grocerylist)

# Left off on Python Remove List Items

grocerylist.remove("Socks") # This will remove the item you type in to be removed
print(grocerylist)

grocerylist.pop(5) # Another way to remove an item from a list is by using 'pop' to remove an item by what order it is in.
print(grocerylist)

grocerylist.pop() # But 'pop' alone will delete the last item on the list
print(grocerylist)

del grocerylist[0] # The 'del' command can be used to delete certain items from a list based on it's order in the list.
print(grocerylist)

del clothes # But adding a 'del' command without specifying which item you want delete will remove the whole list. This will result in errors if you try to call this list later.

dellist = ["Mana", "Karma", "Sandbox"]
dellist.clear() # A more proper way to delete lists are through clear. The list still exists, but has no contents in it.
print(dellist)

for x in grocerylist: # A way to print lists vertically is through loops, which will print the list, one by one
    print(x)

print("Here is something to seperate the two")

for i in range(len(grocerylist)): # This is how we can print items by referring to their index number
  print(grocerylist[i])

print("Here is something to seperate the two")

z = 3
while z < len(grocerylist): # Print all items, using a while loop to go through all the index numbers
    print(grocerylist[z])
    z = z + 1

print("Here is something to seperate the two")

[print(z) for z in grocerylist] # A short hand for loop that will print all items in a list

# Left off on Python List Comprehension

cities = ["New York", "Tokyo", "Lima", "Cairo", "Paris", "Syndey"]
emplst = []

for lp in cities: # This can be used so the list only prints out items that contain an "o" in it
    if "o" in lp:
        emplst.append(lp)

print(emplst)

eplst2 = [ip for ip in cities if "o" in ip] # But a more efficient way of doing this is using this
print(eplst2)

emplst3 = [kp for kp in cities if kp !="Tokyo"] # This list will tell us to exclude certain words, such as "Tokyo" in this case
print(emplst3)

emplst4 = [hp for hp in range(10)] # This will list the first 10 numbers, starting with 0
print(emplst4)

emplst5 = [gp for gp in range(10) if gp < 5] # This will only print up to the first 5 numbers, even though we are asking for 10 (And once again, it will start with 0)
print(emplst5)

emplst6 = [fp.upper() for fp in cities] # Here, we just made all words fully uppercase
print(emplst6)

emplst7 = ['Rome' for dp in cities] # This one will replace everything in the list with "Rome"
print(emplst7)

emplst8 = [sp if sp !="New York" else "Los Angeles" for sp in cities] # Here, we are replacing "New York" with "Los Angeles"
print(emplst8)

# Left off on Python Sort Lists

cities.sort() # This will sort out the "cities" list in alphabetical order
print(cities) 

ordnums = [65, 234, 45, 10, 345]
ordnums.sort() # The sorting feature can also be used to order numbers
print(ordnums)

cities.sort(reverse = True) # It's also possible to have lists be sorted in reverse order
print(cities)

ordnums.sort(reverse = True) # Same can be done for numbers, have the numbers be sorted in reverse order
print(ordnums) 

def myfunc(n):
    return abs(n - 50) # It's also possible to sort numbers based on how close they are to the number 50
 
ordnums.sort(key = myfunc) 
print(ordnums)

cities.sort(key = str.lower) # Normally, lists are case sensitive, but this can be used to make them not case sensitive
print(cities)

cities.reverse() # This can be used to make a list go in reverse
print(cities)