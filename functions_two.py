# def even(num):
#     print(num)
#     if num==0:
#         return num
#     else:
#         return even(num-2)   
# even(8)
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
    
# num=int(input('enter a number to get the factorail: '))
# print(factorial(num))

# def expo(b,r):
#     if r==0:
#         return 1
#     else:
#         return b*expo(b,r-1)   
# result=expo(2,3)
# print(result)

#wop to print  the fibnoccie series using the recursion
# def fobnoccie(num):
#     if num==0:
#         return 0
#     elif num==1:
#         return 1
#     else:
#         return fobnoccie(num-1)+fobnoccie(num-2)
    
# print(fobnoccie(20))

# def sum_of_digits(num):
#     if num==0:
#         return 0
#     else:
#         return num%10 +sum_of_digits(num//10)
# print(sum_of_digits(123))

#reverse a string using the recursion
# def string_reverse(string):
#     if len(string) == 0:
#         return ""
#     else:
#         return string_reverse(string[1:]) + string[0]
# print(string_reverse('hello'))

#wop to find the greatest greaetest common divisor
# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)
# print(gcd(56,98))

#write a recursive fun to find the sum of all elements in a list
#write a recursive fun to generate permutations of string
#generate all substrings of a string
#calculate the sum of first natrual numbers
#whethere is sring is palindrome or not
#count the chareacters in a string

