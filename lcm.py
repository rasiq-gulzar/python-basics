number1=int(input("enter number 1: "))
number2=int(input('enter number 2: '))
lcm=1
if number1>number2:
    greater=number1
else:
    greater=number2
while(True):
    if greater%number1==0 and greater%number2==0:
        lcm=greater
        break
    greater+=1
        
print(lcm)