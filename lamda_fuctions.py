# in python: lamda is nothing but a keyword, or we can say it is shorthand or anonymous function 
# lamda arguments: expressions
# example

# add_ten= lambda x:x+10
# print(add_ten(4))

# another way to solve is:
# add_ten= (lambda x:x+10) (4)
# print(add_ten)

# def is_even():
#     for i in range(1,30):
#         if i%2==0:
#             return True
#         else:
#             return False
# print(is_even())

#filter fucntions
# numbers=[1,2,3,4,5]
# even_numbers=filter(lambda x:x%2==0, numbers)
# print(list(even_numbers))

#sorted functions
# pairs=[(1,'one'),(3,'three'),(4,'four')]
# sorted_pairs=sorted(pairs,key=lambda x: x[0])
# print(sorted_pairs)

# pairs=['delhi','agra','mumbai','pak','india','srilanka']

# sorted_pairs= sorted(pairs,key=lambda x:len(x))
# print(list(sorted_pairs))

#using if else and lambda
# max_of_two=lambda x,y:x if x>y else y
# print(max_of_two(1,2))

# def squares():
#     for i in numbers:
#         return i**2
# squares=map(squares(),numbers)
# numbers=[1,2,3,4,5,6]
# print(list(squares))

# def even(x):
#     if x%2==0:
#         return 'even'
# ev=list(filter(even,numbers))
# print(ev)

# even=list(filter(lambda x:x%2==0,numbers))
# print(even)

# pairs=['delhi','agra','mumbai','pak','india','srilanka']

# def sort(x):
#     return len(pairs)

# result=list(sorted(pairs,key=lambda x:len(x)))
# print(result)
