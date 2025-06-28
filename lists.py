#  the decleration of the list is to store them within the square brackets like [].
#  they are used to store multiple items in a single variable.
#  lists items: ordered, changeable, allow Duplicate
#  example for the ordered: anzar=['Rasiq',  'rasiq', 'azra']
#  example for the changaeable/mutable: fruits=['apple','orange', 'kiwi', 'pinaapple']
#  and if want to store the another fruit on the index like 0
#  fruits[0]='banana'
#  example of the duplicate : fruits['kiwi', 'kiwi', 'orange']
 
#  accessing the list items:
#      list=[1,2,3,4,5]
# #      print(list[-1]): output will be the 5
# #printing the elements of the list by silicing or by indexing 
# fruits=['apple','orange', 'kiwi', 'pinaapple']
# print(fruits[0:3])#this one is silcing 
# print(fruits[0])#this one is indexing 

# #insertion of the lists

# list=['apple','orange', 'kiwi', 'pinaapple']
# list.insert(1,'gauva')
# print(list)

# #pop the any of the element form list by using tyeh pop()
# list.pop(1) this is the index number 
# print(list)

# #appent the elements of the list by using the append() fun
# movies=[]
# movie1=input('enter the movie one : ')
# movie2=input('enter the movie two: ')
# movie3=input('enter the movie three: ')
# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)
# print(movies)

# #removing the elements in the list by using the remove() fun
# list=[1,2,3,4,5,7,8,9]
# list.remove(2)
# print(list)

# #clear the elements of the list by using the clear() fun
# list.clear()
# print(list)

#operations of the lists combining the two lists
# list1=[1,2,3]
# list2=[4,5,6]
# newlist=list1+list2
# print(newlist)

# #by product 
# list1=[1,2,3]
# newlist=list1*3
# print(newlist)

# #calculating the elements of the list
# list1=[1,2,3,4,5]
# print(len(list1))

# #list comprehension: it provides us the way to make a new list from the old list in  consize way example
# list1=[1,2, 23, 7, 8, 9]
# newlist=[i**2 for i in list1 if i%2==0]
# print(newlist)

# list1=[1,2, 23, 7, 8, 9]
# newlist=[i**2 for i in list1 if i%2==1]
# print(newlist)

#sorting the list either in the ascending or the decending list 
# list=[1,5,6,3,4,2]
# list.sort()
# print(list)

# # now for the reverse it will be like this 
# list.sort(reverse=True)
# print(list)

# #creating the xerox of the previous list 
# newlist=list.copy()
# print(newlist)

# #counting the the elements of the list by check the each element how many time the element is repeated in this list
# list=[1,2,3,2,5,2]
# list.count(2)
# print(list)

# #list comprehension: we can check whether the given words are palindrome or not 
# words=['madam', 'mam', 'rasiq', 'url', 'racecar']
# palindrome=[word for word in words if word in word[::-1]]
# print(palindrome)

# # #using the list comprehension we can check how many number of vovels are in a string 
# # sentence='i am learning python'
# # vovels= [vol for vol in sentence if vol in 'aeiou']
# # print(vovels)

# #program to find the index of any of the number 
# list=[1,2,3]
# print(list.index(1))
# newlist=list[::-1]
# print(newlist)
# # to find the sum of the total elemtnt in the list
# list=[1,2,3,4]
# sum=0
# for i in list:
#     sum=sum+i
# print(sum)

# # program to find the maximum and the minimum in a list 
# list=[5,1,3,2,0,-1]
# min=0
# max=0
# for i in list:
#     if(i>max):
#         max=i
#     elif(i<min):
#         min=i
# print(f"the {max} is maximum in the list...")
# print(f'the {min} is the minimum in the list..')

# #finding the average of the elements of the list
# list=[1,2,3,4]
# sum=0
# for i in list:
#     sum=sum+i
# print(sum)
# count=len(list)
# print(count)
# print(f"the average of the total given {list} is : ",sum/count)

# #merging the multiple lists into one list
# list1=[1,2,3,4]
# list2=[1,2,3,4]
# list3=[1,5,6,8]
# print(list1+list2+list3)

# # removing the duplicates from a list we can use this same approach for this union of the list like 
# # first to comnbine the lists and then use the duplicates login and print the result
# list=[1,2,3,5,7,5,6]
# newlist=[]
# for i in list:
#     if i not in newlist:
#         newlist.append(i)
# print(newlist)
        
#program to find the intersection of the two lists
list1=[1,2,3,5,6]
list2=[1,2,3,8,6]
newlist=[]
for i in list1:
    if i in list2:
        newlist.append(i)   
print(newlist)

# # program check whehter the element is present or not 
# list=[1,2,3]
# number=1
# for i in list:
#     if number in list:
#         print("present..")
#         break
#     else:
#         print("not present..")
#         break
    

