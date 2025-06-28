# # wop to take the number for user and convet them into words
# dict1={0:'zero',
#       1:'one',
#       2:'two',
#       3:'three',
#       4:'four',
#       5:'five',
#       6:'six',
#       7:'seven',
#       8:'eight',
#       9:'nine'    
# }
# j=0
# number=int(input('enter integers to convert them into words: '))
# words=str(number)
# list1=list(words)

# while j<len(list1):
#     numbers=int(list1[j])
#     print(dict1[numbers],end=' ')
#     j+=1

# #wop to taking take continuous input form user to get the numbers until user not type to stop and after that it should show the +ve and -ve numbers
# positive_numbers=[]
# negative_numbers=[]
# while(True):
#       number=int(input("for stoping the loop enter 00 and for contunuing enter numbers: "))
#       if number==00:
#             break
#       elif number>0:
#             positive_numbers.append(number)
#       else:
#             negative_numbers.append(number)
            
# print(f"Positive number are {positive_numbers}")
# print(f"Negative number are {negative_numbers}")

# #wop to print the series like 105,98,.....,7
# start=112
# i=0
# while i<=start:
#       start=start-7
#       print(start,end=' ')
#       i+=1

#wop to convert the numbers int decimal to binary    
# number=10
# binary=bin(number)
# print(binary)

#wop to check whether the number is palindrome or not 
# number=int(input('enter a number to check it for palindrome or not : '))
# str2=str(number)
# list1=list(str2)
# i=0
# newlist=[]
# newlist=list1[::-1]
# count=len(newlist)
# while i<len(newlist):
#       if list1[i] in newlist[i]:
#             print("palindrome")
#             break
#       else:
#             print('not palindrome')
#             break
#       i+=1

#wop to take 10 numbers from user and display its average
# list1=[]
# sum=0
# i=0
# stop=10
# while i<=stop:
#       number=int(input('enter number: '))
#       list1.append(number)
#       count=len(list1)
#       sum+=number
#       average=sum/count
#       i+=1
      
# print(f'áverage is {average}')

# #wop to take 10 numbers from user and display the smallest and largest number
# list1=[]
# sum=0
# i=0
# while i<=10:
#       number=int(input('enter number: '))
#       list1.append(number)
#       i+=1
    
# max=max(list1)
# min=min(list1)
# print(f'maximum is {max} and minimum is {min}')

#wop to print the numbers which are divisible by 13 but not by 3
# end=500
# list1=[]
# i=100
# while i<500:
#     if i%13==0 and i%3!=0:
#         list1.append(i)
#     i+=1
# print(list1)

#wop to display the folowing series 2, 22, 222, ....., 2222
# list2=[]
# i=0
# while i<=10:
#     print("2"*i,end=' ')
#     i+=1
   
#wop to print the following series like 1, 4, 9, 16, 25 
# i=0
# while i<=5:
#     print(i**2,end=' ')
#     i+=1

#wop to print the sum of  the following series like 1, 4-9, 16-25, 36-49
# i=0
# list1=[]
# list2=[]
# while i<=5:
#     if i%2==0:
#         list1.append(i**2)
#     else:
#        list2.append(i**2) 
#     i+=1
    
# print(list1)
# print(list2)
# sum=0
# j=0
# while j < len(list1):
#     sum+=list1[j]-list2[j]
#     j+=1
# print(sum)

#wop a program to print the serires like 
# 1     50
# 2     49
# .     .
# .     .
# 50    1

# i=1
# j=49
# while i<=49 and j>=0:
#     print(i,'______',j)
#     i+=1
#     j-=1

#wop to print all the factors of a number
# number=int(input('enter a number to get the all factors of the number: '))
# i=1
# list1=[]
# while i<number:
#     if number%i==0:
#         print(i,end=',')
#     i=i+1

#wop to print the sum of the series like 
# number=int(input('enter number to get the sum of factorial series of the number: '))
# i=1
# fact=1
# sum=0
# while i<=number:
#     fact*=i
#     sum+=fact
#     i+=1
    
# print(f'the sum of the factorail serires is {sum}')

#wop to print the sum of the series like 1+8+27
# i=0
# sum=0
# cube=1
# while i<=3:
#     sum+=i**3
#     i+=1
# print(sum)

# wop to print the folowing lieke PYTHON word in one by one charecter
# string='PYTHON'
# i=0
# while i<=len(string)-1:
#     print(string[i])
#     i+=1
    
# Write a program to print only odd numbers from the given list using while loop. L = [23, 45, 32, 25, 46, 33, 71, 90]
# L= [23, 45, 32, 25, 46, 33, 71, 90]
# i=0
# odd_listt=[]
# while i<len(L):
#     if L[i]%2!=0:
#         odd_listt.append(L[i])
#     i+=1
# print(f'odd numbers from the given list {L} is {odd_listt}')

# wop to print the sum of the following seires like 1+2/1!+2**2/2!+3**3/3!+4**4/4!+5**5/n!
# number=int(input('enter the nubmer: '))
# x=int(input('enter the value of x: '))
# i=1
# j=0
# sum=1
# fact=1
# list1=[]
# list2=[]
# while i<=number:
#     list1.append(i)
#     i+=1
    
# while j<len(list1):
#     fact*=list1[j]
#     list2.append(fact)
#     sum+=x**i/fact
#     j+=1
# print(list2)
# print(sum)

# wop to print the sum of the following seires like 1+2/1+2/2+3**3/3+4**4/4+5**5/n
# number=int(input('enter the nubmer: '))
# x=int(input('enter the value of x: '))
# one=1
# j=0
# i=1
# sum=1
# list1=[]
# list2=[]
# while i<=number:
#     sum+=x**i/i
#     i+=1
# print(sum)

# Write a program that prints all the numbers from 1 to 100, but for multiples of 3, 
# print "Fizz" instead of the number, for multiples of 5, print "Buzz", 
# and for numbers that are multiples of both 3 and 5, print "FizzBuzz".
# Use a "while" loop to solve this. DO THIS AS WELL
# num=100
# i=1
# while i<num:
#     if i%3==0 and i%5==0:
#         print("FizzBuzz",i)
#     elif i%5==0:
#         print('Buzz',i)
#     elif i%3==0:
#         print("Fizz",i)
#     i+=1


# string=input('enter a string: ')
# list1=list(string)
# list2=list1[::-1]
# print(list2)
# if list1 is list2:
#     print('palindrome..')
# else:
#     print('not palindrome')
# if list1==list2:
#     print('palindrome')
# else:
#     print('not palindrome')

# list1=[]
# list1.append(1)
# list1.append(2)
# print(list1)
# # list1.pop()
# list1.remove(1)
# print(list1)
