# #wop to print the first 10 natural numbers
# for i in range(1,11):
#     print(i)
# #wop to print the first 10 whole numbers
# for i in range(11):
#     print(i)
#wop to print the first 10 even numbers
# for i in range(1,20):
#     if i%2==0:
#         print(i,end=',')
#odd numbers    
# print()
# for i in range(1,20):
#     if i%2!=0:
#         print(i,end=',')

# #wop to print the firs 10 natural numbers and their squeare
# for i in range(1,11):
#     print(i**2)

# #wop to print the following series 10,20,30,40,......,300
# for i in range(1,31):
#     print(10*i,end=',')

# wop to print the following series like 105,98,91...,7
# list1=[]
# number=112
# for i in range(1,16):
#     number-=7
#     print(number,end=',')

#wop to print the sum of first 10 even numbers
sum=0
for i in range(1,11):
    sum+=i 
print(sum)

# #wop to print the the table of a number entered from a user
# number=int(input('enter a number to get the table of the number '))
# for i in range(1,11):
#     print(f'{number} * {i}={number*i}')

#wop to print the all even numbers that falls between two numbers entered from the user.abs
# start=int(input('enter the starting point: '))
# end=int(input('enter the ending point: '))
# for i in range(start,end):
#     if i%2==0:
#         print(i,end=',')

#wop to program to check whether the number is prime or not 
# number=int(input('enter a number that to check that primr or not: '))

# is_prime=True
# for i in range(2, int(number ** 0.5) + 1):
#     if number%i==0:
#         is_prime=False
        
               
# if is_prime==True:
#     print('prime')
# else:
#     print('not prime')

#wop to find the sum of digits of numbers accepted from user
# number=int(input('enter digits to print the sum: '))
# str2=str(number)
# list1=list(str2)
# sum=0
# for i in range(len(list1)):
#     sum+=int(list1[i])
    
# print(f"sum is {sum}")

#wop to find the product of digits of numbers accepted from user
# number=int(input('enter digits to print the sum: '))
# str2=str(number)
# list1=list(str2)
# product=1
# for i in range(len(list1)):
#     product*=int(list1[i])
    
# print(f"product is{product}")

#wop to reverse a number accepted from user
# number=int(input('enter digits to print the sum: '))
# str2=str(number)
# list1=list(str2)
# newlist=[]
# newlist=list1[::-1]
# print(newlist)
# for i in range(len(newlist)):
#     print(newlist[i],end='')

# # # wop to convert the numbers like 123 into one two three
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

# number=int(input('enter the digits to convert them into figures: '))
# strint=str(number)
# list1=list(strint)
# for i in range(len(list1)):
#     number=int(list1[i])
#     print(dict1[number],end=',')

#wop to print the fibnoccie serires until the user of the number
# num1=0
# num2=1
# number=int(input('enter a number to generate the fibnoccie series: '))
# if number == 1:
#     print(num1)
# elif number == 2:
#     print(num1, num2)
# else:
#     for i in range(number):
#         next_num = num1 + num2  
#         print(next_num, end=" ")
#         num1 = num2             
#         num2 = next_num       
        
#wop to print the factorail of a number accepted from user
# number=int(input('enter a number to print the factorial: '))
# fact=1
# for i in range(1,number+1):
#     fact*=i
# print(f'the factorail is {fact}')


#wop to check whether the given number is armstrong or not \
# number=int(input('enter a number to check it whethere it is an armstrong or not: '))
# string=str(number)
# list1=list(string)
# count=len(list1)
# armstrong=0
# for i in range(len(list1)):
#     armstrong+=int(list1[i])**count
    
# if number==armstrong:
#     print(f'the given number {number} is armstrong')
# else:
#     print(f"the given number {number} is not armstrong.")


#wop to print the sum of the follwing seres like 1/1!+1/2!+...+1/n!
# number=int(input('enter a number: '))
# fact=1
# list1=[]
# for i in range(1,number+1):
#     fact*=i
#     list1.append(fact)
# print(list1)
# sum=0
# for i in range(len(list1)):
#     sum+=1/list1[i]
# print(sum)

#wop to take continous input from user and 
# # if user enters something to stop it should be stopped and it should print the sum of the number entered
# list1=[]
# for i in range(0,100 ):
#     number=int(input('to stop enter 00 and to continue enter number: '))
#     if number==00:
#         break
#     else:
#         list1.append(number)
# sum=0
# for i in range(len(list1)):
#     sum+=list1[i]
# print(sum)

#wop to take continous input from user and 
# if user enters zero to stop it should be stopped and it should print the count of the positive and negative numbers
# list1=[]
# for i in range(0,100 ):
#     number=(input('to stop enter 00 and to continue enter number: '))
#     if number=='zero' or number=='ZERO':
#         break
#     else:
#         list1.append(int(number))
# print(list1)
# count_positive=[]
# count_negative=[]
# for i in list1:
#     if i>0:
#         count_positive.append(i)
#     else:
#         count_negative.append(i)
# count1=len(count_positive)
# count2=len(count_negative)
# print(f"count of +ve is {count1} and count of -ve is {count2}")

# #wop to check whether the string or number is palindrome or not 
# string=input('enter a string to check whether it is palindrome or not: ')
# palindrome=list(string)
# new_list=palindrome[::-1]
# for i in new_list:
#     if new_list==palindrome:
#         print(f'the given string {string} is palindrome')
#         break
#     else:
#         print(f'the given string {string} is not palindrome')
#         break

# #wop to print the take the 10 numbers from user and display the average
# list1=[]
# for i in range(1,11):
#     number=int(input('enter number: '))
#     list1.append(number)
    
# sum=0
# count=len(list1)
# for i in list1:
#     sum+=i
    
# average=sum/count
# print(f'average is {average}')

# for i in range(5+1):
#     for j in range(1,i):
#         print(j,end='')
#     print()

#wop to print he sum of the elements of the two lists
# list1=[1,2]
# list2=[5,6]
# list3=[]
# for i in range(len(list1)):
#     list3.append(list1[i]+list2[i])

  
# print(list3)
#this program finds the possible parirs that can be used to find the sum of the given number
# list1=[1,2,3,4,5,6,8,9,-1]
# number=int(input('enter a number to find the all possible pairs for sum of the given number: '))
# pairs=[]
# s1=set()
# for i in list1:
#     result=number-i
#     if result in s1:
#         pairs.append((result,i))
#     s1.add(i)
# print(s1,':',pairs)

#wop to find the hcf of the two numbers
# number1=int(input('enter number1:'))
# number2=int(input('enter number2: '))
# l1=[]
# l2=[]
# hcf=[]
# for i in range(1,number1+1):
#     if number1%i==0:
#         l1.append(i)
# for j in range(1,number2+1):
#     if number2%j==0:
#         l2.append(j)
 
# for k in l1:
#     for m in l2:
#         if k==m:
#             hcf=k,m
# print(hcf)

#wop to convert decimal to binary
# decimal_number=int(input('enter a number to convet that into binary: '))
# binary=bin(decimal_number)
# print(binary)

# # wop to accept 10 numbers from the user and display the largest and the smallest number
# list1=[]
# for i in range(5):
#     number=int(input('enter number: '))
#     list1.append(number)

# largest=max(list1)
# smallest=min(list1)
# print(f'largest is {largest}')
# print(f'smallest is {smallest}')

# list1.sort()
# print(f'the second larest in the given numbers are {list1[-2]}')

#wop to display the sum of odd numbers and even numbers separetely that falls between the two numbers accepted from the user
# start=int(input('enter start point: '))
# end=int(input('enter the ending point: '))
# odd=[]
# even=[]
# for i in range(start,end):
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
 
# sum1=0   
# for sum_even in even:
#     sum1+=sum_even
# print(f'the sum of the even numbers is {sum1}')
# sum2=0
# for sum_odd in odd:
#     sum2+=sum_odd
# print(f'the sum of the odd numbers is {sum2}')

# #wop to display all the numbers which are divisible by 13 not by 3 between 100 and 500
# num_by_13=[]
# for i in range(100,500):
#     if i%13==0 and i%3!=0:
#         num_by_13.append(i)

# print(num_by_13)

#wop to print the following series like 2,22,222,2222
# for i in range(10):
#     print('2'*i,end=',')

# #wop to print the following series like 1,4,9,16,25
# for i in range(7):
#     print(i*i,end=' ')

## wop to print the sum of the following seires like 1+2/1!+2**2/2!+3**3/3!+4**4/4!+5**5/n!
# fact=[]
# x=int(input('enter the value of x: '))
# n=int(input('enter the value of n: '))
# temp=1
# for i in range(1,n+1):
#     temp*=i
#     fact.append(temp) 
# sum=1
# for j in fact:
#     for k in range(n+1):
#         sum+=x**k/j
# print(sum)

#wop to print the folowing series like x+x**2+.........+x**n/n
# sum=0
# x=4
# temp=0
# for i in range(1,x):
#     temp=x**i/i
#     sum+=temp
# print(sum)

# #wop to find the sum of the series like 1+8+27.....+ n terms
# sum=0
# for i in range(1,4):
#     sum+=i**3
    
# print(sum)

#wop to find the sum of the following series like 1,2,6,24,120,...,m
# list1=[1,2]
# sum=2
# sum2=0
# for i in range(3,6):
#     sum*=i
#     list1.append(sum)
# for j in list1:
#       sum+=i
    
# print(sum)

#wop to convert the binary number into decimal
# num=input('enter a binary number to convet that into decimal: ')
# list1=list(num)
# # print(list1)
# newlist=num[::-1]
# sum=0
# index=[]
# eight_bit={0:1,
#            1:2,
#            2:4,
#            3:8,
#            4:16,
#            5:32,
#            6:64,
#            7:128,
#            8:256}
# for i in range(len(newlist)):
#     if newlist[i]=='1':
#         index.append(i)
# # print(index)

# sum=[]
# for i in index:
#     sum.append(eight_bit[i])
    
# decimal=0
# for i in sum:
#     decimal+=i
    
# print(f'the give binary number i,e {num} has the decimal number {decimal}')