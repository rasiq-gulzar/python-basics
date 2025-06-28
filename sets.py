# sets are inbuilt data structure that stores unordered data in python or we can see it is a collection of unique elements 
# # we can store different types of data like string, float, int etc.
# # how to create a set:
# my_set=set() #creataing the empty set in python
# print(type(my_set))

# #storing the elements in a set
# my_set1={1,2,3}
# print(type(my_set1))

#converting the list into set
# list=set([1,2,3])
# print(list)
# print(type(list))

# properties of sets:
#     1. unordered:
#     2. unique elements: it wont gonna allow the duplicates in the set
#     3. immutable: the elemtents in a set are immutable but the set itself is mutable.
#     4. There is no indexing or scilicing 
# opertions on sets:

# #adding the elements in a set
# my_set={1,2,3}
# my_set.add(9)
# print(my_set)

# #removing the elements in a set
# my_set.remove(78) #to solve the errro we can uset the discard() fun
# print(my_set)

# #important example 
# my_set2={1,2,3,4,5,4,5,True, 0, False}
# print(my_set2)
# #calculating the lenght of a set 
# print(len(my_set2))

# #union of two sets
# my_set2={1,2,3,4,5,4,5,True, 0, False}
# set1={1,2,3}
# # union_set=my_set2 | set1
# # print(union_set)

# # #printing common elements of tow sets
# # intersection1=my_set2.intersection(set1)
# intersection1=my_set2 & (set1)
# # intersection1=my_set2 ^ (set1) #it removes the common elements in both the sets simultaneaously
# print(intersection1)


# #subset of a set
# subset={1,2}
# supersat={1,2,3,4}
# print(subset.issubset(supersat))

# #supersat of a set
# rasiq={1,2}
# anzar={3,4}
# # print(anzar.issuperset(rasiq))

# #disjoint in a set
# print(anzar.isdisjoint(rasiq))

# #set comprehension 
# list=[1,2,3,4]
# squares={i**2 for i in list if i>2}
# print(squares)

# set=[1,2,3,4,5]
# largest=max(set)
# minimum=min(set)
# print(largest, minimum)

# str=("i, am, learning, python")
# # new_set=tuple({str})
# list1=str.split(",")
# set=set(list1)
# print(set)
# print(type(set))


# def isPrime(n):
#     is_prime=True
#     for i in range(2,n):
#         if n%i==0:
#             is_prime=False
        
#     if is_prime:
#         print(n)
        
        
# def printingPrimeNumbers(r):
#     for i in range(1,r):
#         isPrime(i)
    
# num=int(input("Enter the range of prime numbers you want to print: "))    
# printingPrimeNumbers(num)

def powerSeries(num):
    sum=0
    for i in range(1,num):
        print(i**i,end=' ')
        sum+=i**i
    print(f'\nthe sumation of the all prime numbers is {sum}')
        
powerSeries(10)