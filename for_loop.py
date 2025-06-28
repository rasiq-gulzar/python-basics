# for loop:
#     basic concepts:
#         when to use for loop: simple iteration in sequence example:
#             fruits=['mango','banan','apple']
#             for fruit in fruits:
#                 print(fruit)
# fruits=['mango','banan','apple']
# for fruit in fruits:
#      print(fruit)
     
# #iterating over a string
# string='hello'
# for i in string: 
#     print(i)

#range in for loop range() fun have there things inside it like range(start, stop, step) example
# for i in range(2,10,2):#print the even numbers
#     print(i)
# for i in range(0,10,4):
#     print(i)

#in loops we can use the break, continue and pass
# for i in range(5):
#     if i==2 or i==4:#this will skip the 2 and 4 using the contuine
#         continue
#     print(i)
# for i in range(5):
#     if i==3:
#         break
#     print(i)
# for i in range(5):
#     pass

# nested for loops
# for i in range(5):
#     for j in range(i):
#         print(f'{i}{j}')
# items1=['yellow','blue','orange','white']
# items2=['sunflower','sky','sun','pillow']
# list1={}
# for i in range(len(items1)):
#     list1[items1[i]]=items2[i]

# print(list1)
        
#for with else class
# for i in range(5):
#     print(i)
# else:
#     print('loop ends without break')

#the enumerate inbuilt function in python gives us the like a counter for counting the items in a list and
#as well as gives access the items in a list itself.
# fruits=['mango','banana','apple']
# for index,fruit in enumerate(fruits):
#     print(f'index {index}: {fruit}')


# def summation():
#     sum=0
#     for i in range(1,6):
#         sum+=i
#     return sum

# print(summation())

# def primeOrNot(n):
#     is_prime=True
#     for i in range(1,n):
#         for j in range(2, i):
#             if i%j==0:
#                 is_prime=False
#     if is_prime==True:
#         print('prime')
        
              
# number=int(input('enter a range to get the prime numbers: '))

# print(primeOrNot(number))

