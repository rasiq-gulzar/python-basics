# factorail of a  number
# number=int(input('enter a number to get the factoral of the number: '))
# i=1
# factorial=1
# while i<=number:
#     factorial*=i
#     i+=1
# print(f'the factorail of a given number {number} is {factorial}')

# while loop to check whthere the number is armsstrong or not
# number=int(input('enter a any armsstrong number to check whether the number is armsstrong or not: '))
# str2=str(number)
# count=len(str2)
# i=0
# cal=0
# while i<count:
#     cal=cal+int(str2[i])**count
#     i+=1
    
# if number==cal:
#     print('the number is armstrong.')

# else:
#     print('the number is not armstrong.')

# #number guessing game 
# while(True):
#     number=int(input('enter number between to guess: '))
#     if number==13:
#         print(f'you won your guessed number is correct i,e {number}')
#         break
#     elif number==3:
#         print(f'you won your guessed number is correct i,e {number}')
#         break
#     elif number==11:
#          print(f'you won your guessed number is correct i,e {number}')
#          break
#     elif number==5:
#          print(f'you won your guessed number is correct i,e {number}')
#          break
#     elif number==9:
#          print(f'you won your guessed number is correct i,e {number}')
#          break
#     elif number==19:
#          print(f'you won your guessed number is correct i,e {number}')
#          break

# #by using the while loop check the vovels and consents in a string 
# alphabet=input("enter an alphabet to check whether the alphabet is vovel or consonent: ")
# vovels=('a','e','i','o','u')
# count=len(alphabet)
# i=0
# while i<count:
#     if alphabet in vovels:
#         print(f"the input alphabet i,e {alphabet} is a vovel")
#         break
#     else:
#         print(f"the input alphabet i,e {alphabet} is consonent..")
#     i+=1

# #multiplication of table using the while loop
# number=int(input('enter a number to get the multiplication table: '))
# i=1
# multiply=1
# while i<=number:
#     print(f'{number} * {i}= ',number*i)
#     i+=1

# #reverse a number 
# number=int(input('enter a big number to reverse it: '))
# str2=str(number)
# list1=list(str2)
# i=0
# newlist=[]
# newlist=list1[::-1]
# count=len(newlist)

# reverse=0
# while i<count:
#     reverse=int(newlist[i])
#     i+=1
#     print(reverse,end='')

# fibnoccie series
# number = int(input('enter a number to generate the fibonacci series: '))
# num1 = 0    
# num2 = 1    

# if number == 1:
#     print(num1)
# elif number == 2:
#     print(num1, num2)
# else:
#     print(num1, num2, end=" ")
#     count = 2   
    
#     while count < number:
#         next_num = num1 + num2  
#         print(next_num, end=" ")
#         num1 = num2             
#         num2 = next_num        
#         count = count + 1

# printing pyramid of stars 
# n=int(input('enter number of rows to print the pyramid of stars: '))
# row = 1
# while row <= n:
#     space = 1
#     while space <= (n-row):
#         print(" ",end='')
#         space+=1
#     star = 1
#     while star <= (2*row-1):
#         print('*',end='')
#         star+=1
    
#     print() 
#     row += 1

# number=6
# sum=0
# fact=1
# i=1
# while i<number:
#     fact=fact*i
#     sum=sum+i/fact
#     i+=1
# print(sum)

# list1=[]
# while(True):
#     number=input('enter a number: ')
#     if number.lower()=="zero" or number.upper()=='ZERO':
#         break 
#     else:
        
#         list1.append(int(number))
#         sum=0
#         for i in list1:
#             sum+=i    
            
# print(sum)


# hcf of numbers
# number1=int(input("enter number one: "))
# number2=int(input('enter number two: '))
# i=1
# j=1
# hcf=[]
# hcf2=[]
# highest=[]
# while i<number1:
#     if number1%i==0:
#         hcf.append(i)
    
#     i+=1

# while j<number2:
#     if number2%j==0:
#         hcf2.append(j)
    
#     j+=1
    
# print(hcf,hcf2)

# for k in hcf:
#     for l in hcf2:
#         if k==l:
#             highest=k,l
            
# print(highest)

# Write a program using a "while" loop that finds the sum of all the prime numbers between 1 and 1000.
# A prime number is a number that is only divisible by 1 and itself.
# num=int(input('enter a range to genrate the prime numbers and sum of the all numbers: '))
# i=1
# list1=[]
# while i<num:
#     if i==5 or i==3 or i==7:
#         list1.append(i)
#     elif i%5==0:
#         pass
#     elif i%2==0:
#         pass
#     elif i%3==0:
#         pass
#     elif i%7==0:
#         pass 
#     else:
#         list1.append(i)
#     i+=1 
# print(list1)

# sum=0
# j=0
# while j<len(list1):
#     sum+=list1[j]
#     j+=1

# print(sum)
