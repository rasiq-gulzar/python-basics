# the syntax of the tuple is ()
# 1. the items stored in the tuple are ordered: indexing ane position
# 2. and immutable: non changable 
# example 
# tuple=('hello','go ', 'no')
# print(tuple)
# tuple[1]='keep'
# print(tuple) # the error is related to the unchangeable like: TypeError: 'tuple' object does not support item assignment
#3. Heterogininty: we can store differnt types of datatypes in the tuple
#4. it allows redundency in the tuple: allows duplicates
#5. Hashable: tuples are immutalble, they can be used as keys in dictionaries, unlike lists, which are mutalble.

# the operations on the tuple 
# # 1. accessing of elements:
#     example: 
# tuple=[1,2,3]
# print(tuple[:])

# #2. slicing: taking a small portion form a tuple 
# tuple=[1,2,3,4,5]
# print(tuple[1:4])

# #3. packing in the tuple: assigning the multiple values to a tuple is called packing 
# example:
# tuple=10,20,30
# print(tuple)

# #4. unpacking: accessing the values stored in the tuple example
# x,y,z=(10,20,30)
# print(x,y,z)

# #accesssing the multiple packed elements using the astrick sign(*)
# a,*b,c=(1,2,3,4,5,8)
# print()
# numbers=()
# num1=int(input("enter number 1: "))

# num2=int(input("enter number 2: "))

# num3=int(input("enter number 3: "))

# numbers=num1,num2,num3

# print(numbers)

#given a list of numbers find the sum and average 
#create a prog that takes a temp in celcius and converts into farehniet
#implenmt a prog that converts the a given number of minutes into hours and minutes
#create a prog to calculate the vovels in a given string 
#tuple comprehension: example
# tuple1=(1,2,3,4)
# newtuple=tuple(i for i in tuple1 if i>2)
# print(newtuple)
