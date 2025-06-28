number1=int(input("enter number one: "))
number2=int(input('enter number two: '))
i=1
j=1
hcf=[]
hcf2=[]
highest=[]
while i<number1:
    if number1%i==0:
        hcf.append(i)
    
    i+=1

while j<number2:
    if number2%j==0:
        hcf2.append(j)
    
    j+=1
    
print(hcf,hcf2)

for k in hcf:
    for l in hcf2:
        if k==l:
            highest=k,l
            
print(highest)