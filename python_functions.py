# what is a function?
# A fucntion is basically a block of code only when it is called.
# syntax:
#     def my_fuction():
#         some work
# my_fuction(): calling of a Function
# why is use fucntions in python: it decreases redundency or duplicacy and it increases usablility
# # a fucntions have two things.
# 1. Paremeter: they are varaiales and they are used in functions like: 
#     def my_fuction(parameter):
# 2. Argument: they are the things used in main boldy where the function is called 
# my_fuction(argument):
    
# Arbiotary arguments: how many arguments can we pass into our function, add a * before name in the fucntion definition.
# example: 
# def my_function(*kids):
#     print('youngest child is: ', kids[2])
# my_function('rasiq','azra','maria','anzar')

#keyword argument(kwargs)
# we can also send argument withe the key=value. example
# def my_function2(child3,child2,child1):
#     print('the gounges is ',child3)
# my_function2(child1='rasiq',child2='azra',child3='none')

# # Arbitary keyword arguments 

# def my_kids(**kid):
#     print('last name is '+kid['lname'])

#this is a program to pirng the sum of the given inputed numbers
# def summation(*numbers):
#     result=sum(numbers)
#     print(result)

# num1=int(input('enter number 1: '))
# num2=int(input('enter number 2: '))
# num3=int(input('enter number 3: '))
# summation(num1,num2,num3)

# def apply_function(func,value):
#     return func(value)
# #this is called higher order functions
# def squares(x):
#     return x**2
# result=apply_function(squares,4)
# print(result)

# #find the factorail of number using function: 
# def my_factorial(x):
#     fact=1
#     for i in range(1,x+1):
#         fact*=i
#         print(fact)
# my_factorial(5)

#write a function to return the nth fibnacci series
# def my_fibnanie_series(x):
#     num1=0
#     num2=1
#     if x==1:
#         return 1
#     elif x==2:
#         return 1,2
#     else:
#         for i in range(x):
#             next_num=num1+num2
#             print(next_num,end=' ')
#             num1=num2
#             num2=next_num
            
# my_fibnanie_series(10)

# wop that takes a list of numbers and returns a new list of numbers containing the squares of the all numbers
# def squares_of_numbers(list1):
#     squares=[]
#     for i in list1:
#         if i%2==0:
#             squares.append(i*i)
#     return squares
# numbers=[1,5,8,9,54,63,21,23,56,16,14,63]
# result=squares_of_numbers(numbers)
# print(result)

#wop to count the occurence of a spdcific element in a list
# def occurences(num):
#     count=0
#     numbers=[1,5,8,9,5,63,21,21,23,56,5,14,63,63]
#     for i in range(len(numbers)):
#         if numbers[i]==num:
#             count+=1
#     return count

# digit=21
# print(f'the given digit {digit} occured {occurences(digit)} times')

#wop that takes two list of numbers and returns their intersection
# def intersection(list1,list2):
#     newlist=[]
#     for i in list1:
#         for j in list2:
#             if i==j:
#                 newlist.append(i)
#     return newlist

# l1=[1,2,3,4,5,8,9]
# l2=[1,3,2,5,4,7,21]
# print(intersection(l1,l2))

#wop using function that reverses a string 
# def reverse_a_string(string):
#     reversed=string[::-1]
#     return reversed

# print(reverse_a_string('rasiq'))

#wop using functions to check whether the given string is palindrome or not 
# def palindrome(string):
#     reversed=string[::-1]
#     if reversed == string:
#         return 'palindrome'
#     else:
#         return 'not palindrome'
# print(palindrome('madam'))


#recursion: when a fucntion calls it self that function is called recursive function.eample:
# def demo():
#     print('hello')
#     demo()
# demo() #this is the infinidt loop but it has a limeit of like 1k times it will run
# i=0
# def demo():
#     global i
#     i+=1
#     print('hello',i)
#     demo()
# demo()

# 1. basic case:
