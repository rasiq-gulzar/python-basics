# # Creating a set with immutable elements (tuple, string, integer)
my_set = {(1, 2, 3), "hello", 42}
print("Original Set:", my_set)

# Attempting to modify an immutable element directly will fail
# For example, trying to change the tuple (this will not work as expected)
# my_set <sup> </sup> <sup> </sup> = 10  # This will raise a TypeError because tuples are immutable

# However, you can remove and add elements to the set itself (because sets are mutable)
my_set.add("world")  # Adding a new element
print("After adding 'world':", my_set)

my_set.remove((1, 2, 3))  # Removing an element
print("After removing (1, 2, 3):", my_set)

# Trying to add a mutable element (like a list) to the set will raise an error
try:
    my_set.add([4, 5, 6])  # Lists are mutable, so this will fail
except TypeError as e:
    print("Error adding mutable element to set:", e)

# But you can add another immutable element, like another tuple
my_set.add((7, 8, 9))
print("After adding (7, 8, 9):", my_set)
