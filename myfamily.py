# Question1 - Write a program myfamily.py and try out the following piece of code. 

myfamily = ("mother", "father", "sister", "brother", "sister") 

print(myfamily) 

# 1. Use type()to check the type of the object myfamily 

print(type(myfamily))

# 2. Access tuple items sister by using index numbers 

print(myfamily[2], myfamily[4])

# 3. Check whether we can add an item me by using the append() method.

# myfamily.append('me')  ->  It gives us an output: "AttributeError: 'tuple' object has no attribute 'append'"
# So, we can not use the append() method.

# We can use a little trick to add an item into a tuple:

family = list(myfamily)
family.append('me')
myfamily = tuple(family)

print(myfamily)

# 4. Check whether we can remove the item brother by using the pop() method.

# myfamily.pop('brother')  ->  AttributeError: 'tuple' object has no attribute 'pop'
# So, we can use another way:

# family = list(myfamily) (It already exists, so we do not need to create a new one.)
family.pop(3)
myfamily = tuple(family)

print(myfamily)