# # #operations and the implementations of the string 
# # name="my name is azra . my father's name is Mr Malik"
# # print(name)

# # #lenght of the string
# # print(len(name))

# # #we will check of the string
# # print("free" in name)

# # #slicing of the strings: to divide them  in the single pieces
# # print(name[2:5])
# # print(name[:5])

# # #negative indexing in python
# # print(name[-5:-10])

# # #concetation of strings
# # a="1"
# # b="2"
# # print(a+b)

# # #capitalize the string
# # x="hellow world"
# # print(x.upper())

# # #lowercase the strings
# # print(x.lower())

# # #capitalize the every first word or the string
# # z="hii i m rasiq"
# # print(z.capitalize())
 
# # #strip: to exclude the spaces in the string or remove them by using the strip
# # obj="hello  "
# # print(obj.strip())

# # #replaced the words in the string
# # str="hello world"
# # print(str.replace("h","H"))

# # #spilit the string like all the words will be divide into in the list form
# # str2="hellow, world"
# # print(str2.split(","))

# # #escape sequence of the strings like (\n, \t)
# # print("hello,\t world"+"\nhello \n world")

# # #formatted string using the (f) alphabet
# # fruits=["banana",'mango','apple']
# # person=f"my favourite fruits are {fruits}"
# # print(person)

# # #reverse of the string
# # str3="abcdefghi"
# # reversed_string=str3[::-1]
# # print(reversed_string)

# # #accessing the specific word in a string
# # print(str2[3])

# # #to check that whether the string starts or ends with the given words
# # print(name.startswith("my"))
# # print(name.endswith("Malik"))

# #joining the multiple strings by using th join
# bucket=['hello', 'rasiq', 'and', 'ai']
# new_joined=" ".join(bucket)
# print(new_joined)

# # # #to check the where the string is numeric or not
# # # my_string="1234"
# # # print(my_string.digits())

# # # write a prog how that counts how many times the leter a is appearing in a string
# # # wop python function that will reverse a given string
# # # wop that conerts a string to a list of words

# # # write a prog how that counts how many times the leter a is appearing in a string
# # new_string="so we are here to announce that today we are going to learn the opreation and the implementations of the string"
# # print("the letter a is in this string are:",new_string.find("a"))

# # wop python function that will reverse a given string
# str4="welcome to the programmming world"
# # reversed=str4[::-1]
# # print(reversed)

# # wop that conerts a string to a list of words
# print(str4.split())

# Write a function that takes a name and an age as input, and returns a string in the format "My name is {name} and I am {age} years old."
# name='Rasiq'
# age=24
# print(f'my name is {name} and i am {age} years old.')

# # #wop that takes the digits as a string and convert them and apply them operations 
# digit_one=input("enter the digit one as a string: ")
# digit_two=input('enter the digit two as a string: ')
# new_digit_one=int(digit_one)
# new_digit_two=int(digit_two)
# print("after conversion the the sum of the two given string digits is: ",new_digit_one+new_digit_two)

# #wop to calculate the volume of a sphere the formulla is 4/3 pie r^^^
# radii=int(input("enter the radius of the sphere: "))
# pie=3.14
# # volume_of_the_sphere=4/3*pie*radii*radii*radii
# # print("the volume of the sphere is : ",volume_of_the_sphere)

# #wop curve surfade area of the cone prl(l+r)
# radius=int(input("enter the radius of a cone: "))
# length=int(input("enter the lenght of a cone: "))
# curved_surface_of_cone=pie*radius*length*length+radius
# print("the curved surface area of the cone is:",curved_surface_of_cone)
# palindrome=input("enter a string to check whether the string is palindrome or not: ")
# new_palidrome=palindrome[::-1]
# for i in palindrome:
#     for j in new_palidrome:
#         if(list(i)==list(j)):
#             print(f"the given string {palindrome} is a palindrome..")
#             break
#         else:
#             print(f"the given string {palindrome} is not a palindrome...")
#             break
#     break
#i have to extract the world for this string
string='Futrelle, Mrs. Jacques Heath (Lily May Peel)'
print(string.split(",")[1].split(".")[0])
#waht are these [1] and [0] are doing here in the split function tell me about them
#i have to extract the world for this string 
string='Futrelle, Mrs. Jacques Heath (Lily May Peel)'
# df['Name'].str.split(",")[1].split(".")[0]
#what will be the scenerio for this if we apply this to this dataframe
#i have to extract the world for this string
df['Name'].str.split(",")[1].split(".")[0]
