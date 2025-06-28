#calculate the sum of first natrual numbers
# def sum_of_first_n_numbers(n):
#     sum=0
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return sum_of_first_n_numbers(n-1)+n
# print(sum_of_first_n_numbers(10))

#write a recursive fun to find the sum of all elements in a list
# def sum_of_elements_list(list1):
#     if len(list1)==0:
#         return 0
#     else:
#         return list1[0]+sum_of_elements_list(list1[1:])
# list2=[1,2,3,4,5]
# print(sum_of_elements_list(list2))


#whethere is sring is palindrome or not 
# def palindrome(string):
#     if len(string) <= 1: 
#         return 'palindrome'
#     else:
#         if string[0] == string[-1]: 
#             return palindrome(string[1:-1]) 
#         else:
#             return 'not palindrome'

# print(palindrome('racecar')) 


##generate all substrings of a strings of string

# def generate_substrings(s, start=0, current=''):
#     if start == len(s):
#         print(current)
#         return
#     if current:
#         print(current)
#     for i in range(start, len(s)): 
#         generate_substrings(s, i + 1, current + s[i])
# generate_substrings('abcd')


#wop to count the charecters in a string and occurences of a charecter
# def count_char(s, index=0, count=None):
#     if count is None:
#         count = {}
#     if index == len(s):
#         return count
#     char = s[index]
#     if char in count:
#         count[char] = count[char] + 1
#     else:
#         count[char] = 1
#     return count_char(s, index + 1, count)

# string = "azraw"
# result = count_char(string)

# sum = 0
# for char, fre in result.items():
#     print(f'{char}: {fre}')
#     sum = sum + fre

# print(sum)

#find the permutations of a string using the recursion
