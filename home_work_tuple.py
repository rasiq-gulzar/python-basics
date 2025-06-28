# # # given a list of numbers find the sum and average 
tuple1=(1,2,3,4,5)
sum=0
for i in tuple1:
    sum=sum+i

count=len(tuple1)
average=sum/count
print(f"the sum and the average of the given tuple is sum is {sum} and the average is {average}..")

# # # ##create a prog that takes a temp in celcius and converts into farehniet 
temp=int(input("enter the temp for conversion it from celsius to  fahrenhiet: "))
conversion=temp*1.8+32
print(f"the conversion of the given temperature in fahrenhiet is {conversion}")

# # #implenmt a prog that converts the a given number of minutes into hours and minutes
number=int(input("enter the minutes to get that in hours and the minutes: "))
hour=number//60
min=number%60
print(f"out put is {hour} hours and {min} minutes")

# #create a prog to calculate the vovels in a given string 
tuple1=("i m learning python")
vovels=("aeiou")
calculate_vovels=[]
for i in tuple1:
    if i.lower() in vovels:
        calculate_vovels.append(i)
        
length=len(calculate_vovels)
print(f"the following are the vovels detected in the given string i,e {calculate_vovels} and the count of them are {length}")

# # #same prgram in the tuple comprehension
calculate_vovels=tuple(i for i in tuple1 if i in vovels)
length=len(calculate_vovels)
print(f"the following are the vovels detected in the given string i,e {calculate_vovels} and the count of them are {length}")

#to check the palindrome in a tuple
tuple3=("racecar", "rasiq", "madam","level","mam", "truth")
palindrome=tuple(word for word in tuple3 if word in word[::-1])
print(palindrome)

#palindrome using the for i loop in tuple
calculate_words=[]
for i in tuple3:
    if i.lower() in i[::-1]:
     calculate_words.append(i)
     
print(calculate_words)