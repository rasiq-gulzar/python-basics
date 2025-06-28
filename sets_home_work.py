#program that checks if two sets have elements in common
set_one={1,2,3,5,7,8,10}
set_two={1,3,5,4,9,10}
for i in set_one:
    if i in set_two:
        print(f"the comman elemetns are {set_one & set_two}")
        break
    else:
        print("there are no common elements in the given set")
        
        
# #difference of two sets
difference_set=set()
for i in set_one:
    if i not in set_two:
        difference_set.add(i)
print(difference_set)

# #function that takes a list of strings and returns a set of unique characters present in all strings
string_one=input("enter string one: ")
string_two=input("enter string two: ")
string_three=input("enter string three: ")
unique_characters=set()
for i in string_one:
    for j in string_two:
        for k in string_three:
            if i or j or k not in unique_characters:
                unique_characters.add(i)
                unique_characters.add(j)
                unique_characters.add(k)
    
print(unique_characters)


