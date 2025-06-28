# # in dictionary we can store mutiple items in a single Dictionary.
# # they are unordered: collection of items
# # we store the data in the key and withe its value form.
# # in the dict. the keys are unique and the value can be any type.
# # how to create a dict. in python.
# #mutable 
# my_dic={'name': 'rasiq',
#         'adderss':'anantnag',
#         'marks':[22,44,55,99],
#         'hobbies':("reading books", "coding", "playing games"),
#         'fav_color':{"pink", "black","white"},
#         99:'no'
#         }
# for i in my_dic:
#     print(my_dic[i])

# #so we can create the dic by dict keyword this is the second way to create the dictionary
# # my_dict=dict(name="rasiq", address="anantnag")
# # print(my_dict)

# # #accessin the values of a specific key
# # print(my_dic['name'])

# # #accessing the values of a specific key using this so that without facing the error
# # print(my_dic.get("hello",'not found'))

# # #if we have to add elements to a dictionary
# # my_dic['email']='email@gmail.com'
# # my_dic["age"]=90

# # print(my_dic)

# # #remove something in the dic
# # del my_dic['age']
# # del my_dic[99]
# # print(my_dic)

# # #another method to delte the things in a dict is pop()
# # result=my_dic.pop('hobbies')
# # print(result)

# #clear in dictionary
# # my_dic.clear()
# # print(my_dic)

# #checking for existance of keys or values
# # if 'name' in my_dic:
# #     print("name exis...")
    
# # if "jarvis" in my_dic.values():
# #     print("exist")
    
    
# # #dictionary comprehension
# # dict={1:2, 3:4}
# # dict_one={i:i**2 for i in dict if i%2==1}
# # print(dict_one)

# #filtering the keys or vaules
# # #example: eveen numbers
# # list_sq_numbers={1:1, 2:4, 3:9, 4:16, 5:25}
# # even_numbers={key:value for key,value in list_sq_numbers.items() if value%2==0}
# # print(even_numbers)

# # #merging  in dictionaries
# # dic={'name': 'rasiq',
# #         'adderss':24,}
# # dic_two={'address':'anantnag',
# #          'cell no.':87988465476}
# # # dic.update(dic_two)
# # # print(dic)

# # #another method is the | operator
# # resutl=dic | dic_two
# # print(resutl)

# # #nested dictionary: a dictionary in a dictionary syntax is:
# # dict1={"student": {'name':'rasiq', 'sub':'python'}
# # }
# # # print(dict1['student']['name'])

# #we can access all the key values of dic by using thje dic.keys() and for the copy we can use the copy()
# #dictionary is mutable so we can use a method to create a dic and give that a default vlaue to all the keys like 0
# # result=dict1.fromkeys(["a",'b','c'],0) #this uses the 0 as default value to add it to the all given keys
# # print(result)



# #it checks the huge possbile key for a list of dictionary
# # my_dic={2:{'name':'rasiq', 'sub':'python'},
# #         6:{'address':'kulgam', 'age':20}}
# # max_key=0
# # for i in my_dic:
# #     if i>max_key:
# #         max_key=i
        
# # print(max_key)
 


# # occurences={}
# # my_dic={'name':'i m learning python'}
# # string=my_dic['name']
# # count=0
# # for i in string:
# #     if i in occurences:
# #         occurences[i]+=1
# #     else:
# #         occurences[i]=1
# # print(occurences)
# # # for i, count in occurences.items():
# # #     print(f"Character '{i}' appears {count} times.")

# list1=["name",'age']
# list2=['azra','90']
# # merged=dict(zip(list1,list2))
# # print(merged)
# dict1={}

# # for i in list1:
# #     for j  in list2:
# #         if i or j not in dict1:
# #             dict1=i,j
# # print(dict1)
# for i in range(len(list1)):
#     dict1[list2[i]]=list1[i]
    
# print(dict1)

# list1=[1,2,3,4,5,6,7,8,9,10]
# newlist=[x**2 for x in list1]
# print(newlist)
# list1=(1,2,3,4,5,6,7,8,9,10)
# newtuple=(x**2 for x in list1 if x%2==0)
# print(tuple(newtuple))

# words=['hello','world','python']
# newlist=[x.upper() for x in words]
# print(newlist)
# words=['madam','world','python']
# palindrome=[x for x in words if x==x[::-1]]
# print(palindrome)

# list1=[[1,2,3],[4,5,6],[7,8,9]]
# newlist=[x for sublist in list1 for x in sublist]
# print(newlist)

list1=((1,2,3),(4,5,6),(7,8,9))
newlist=(x for sublist in list1 for x in sublist)
print(tuple(newlist))