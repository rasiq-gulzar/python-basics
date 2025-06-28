# loops:
# there are three important things in the loop:
#     starting codition:
#     stopping condition:
#     setping condition:

# we have two loops in the python:
#     1. while loop:
#         syntax:
#             while stopping condition:
#                 updation.
                
# while can be a infinite loop:
#     example:
#         index=1
#         while index<=5:
#             print(index)
#             index+=1 #increment

#example of a while loop:
# while(True):
#     print('hello world')  #we can call this do while loop in the python

# #printing the first 10 natural numbers
# sum=0
# i=1
# while i<=30:
#     if i%2==0:
#         sum+=i 
#     else:
#         sum+=i 
#     i+=1
# print(sum)

# #check that whether the give n number is prime or not 
# number=int(input("enter a number: "))
# is_prime=1
# i=2
# while i*i<number:
#     if number%i==0:
#         is_prime=0

#     i+=1
# fibnoccie,find gcd, print pyramid.    
# if is_prime==0:
#     print('not prime')
# else:
#     print('prime')

#wop to print to print the first 10 integers and their squares
# number=int(input('enter a number: '))
# squares=0
# i=1
# print('number        squres')
# while i<=number:
#     print(i,'\t \t',i*i)
#     i+=1

# start=10
# i=0

# while i <=30:
#     print(start*i,end=' ')
#     i+=1
# start=10
# i=start
# sum=0
# while i>=0:
#     print(i,end=' ')
#     sum+=i
#     i-=1

# print(sum)

# start=10
# i=start
# sum=0
# while i>=0:
#     if i%2==0:
#         sum+=i
#     i-=1

# print(sum)

# start=int(input("enter the start point: "))
# end=int(input('enter the end point: '))
# i=start+1
# while i<=end:
#     if i==end:
#         break
#     else:
#         if i%2==0:
#             print(i,end=' ')
#     i+=1

#reverse a number 
# number=int(input('enter a big number to reverse it: '))
# str2=str(number)
# list1=list(str2)
# i=0
# newlist=[]
# newlist=list1[::-1]
# count=len(newlist)
# reverse=0
# while i<count:
#     reverse=reverse+int(newlist[i])
#     i+=1

# print(reverse,end='')

