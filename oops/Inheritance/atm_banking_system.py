def start():
    print('WELCOM TO JK BANK ATM')
    print('Press 1 for checking balance.')
    print('Press 2 for withdrawing the amount.')
    print('Press 3 for changing the ATM PIN.')
    print('Press 4 for fund transfer.')
    print('Press 5 for downoading mini statemnt.')
    choice=int(input('ENTER->>:'))
    if choice ==1:
        balance_check()
    elif choice==2:
        withdraw()
    elif choice==3:
        change_pin()
    elif choice==4:
        fundtransfer()
    elif choice==5:
        download_mini_st()
    else:
        print('please enter right input:')
        return start()
    
def balance_check():
    print('select your bank accout type below')
    print('1. Savings')
    print('2. Current')
    print('3. CD')
    select=int(input('ENTER ACCOUNT TYPE: '))
    if select==1:
        print('your current acc balance is 10000.00 cr')
    elif select==2:
        print('your current balance is 20000.00 cr')
    elif select==3:
        print('your current balance is 50000.00 cr')
    else:
        print('please select right option..thankuu.')
        return balance_check()
    
    y=input('do you want to continue plase enter(y):')
    if y=='y' or y=='yes' or y=='YES' or y=='Yes':
        return start()
    else:
        pass
    
def withdraw():
    pin=1212
    savings=10000
    current=20000
    cd=50000
    
    print('select your bank accout type below')
    print('1. Savings')
    print('2. Current')
    print('3. CD')
    select=int(input('ENTER ACCOUNT TYPE: '))
    if select==1:
        savings=10000
        p=int(input('enter your pin: '))
        for i in pin_container:
            pin=i

        if p==pin_container[0] or p==pin_container[-1]:
            bal=int(input('enter you amount to withdraw: '))
            if bal>savings:
                print('your acc bal is 10000.00 cr please enter amout less than your acc bal')
                return withdraw()
            else:
                savings=savings-bal
                print(f'you have successfully withdrawed {bal}.00 cr')
                print(f'your current balance is {savings}.00 cr')
        else:
            print('wrong pin...please try again')
            return withdraw()    
    elif select==2:
        current=20000
        p=int(input('enter your pin: '))
        for i in pin_container:
            pin=i
        if p==pin_container[0] or p==pin_container[-1]:
            bal=int(input('enter you amount to withdraw: '))
            if bal>current:
                print('your acc bal is 20000.00 cr please enter amout less than your acc bal')
                return withdraw()
            else:
                current=current-bal
                print(f'you have successfully withdrawed {bal}.00 cr')
                print(f'your current balance is {current}.00 cr')
        else:
            print('wrong pin...please try again')
            return withdraw()
    elif select==3:
        cd=50000
        p=int(input('enter your pin: '))
        for i in pin_container:
            pin=i
        if p==pin_container[0] or p==pin_container[-1]:
            bal=int(input('enter you amount to withdraw: '))
            if bal>cd:
                print('your acc bal is 50000.00 cr please enter amout less than your acc bal')
                return withdraw()
            else:
                cd=cd-bal
                print(f'you have successfully withdrawed {bal}.00 cr')
                print(f'your current balance is {cd}.00 cr')
        else:
            print('wrong pin...please try again')
            return withdraw()
    else:
        print('please select right option..thankuu.')
        return withdraw()  
            
    y=input('do you want to continue plase enter(y):')
    if y=='y' or y=='yes' or y=='YES':
        return start()
    else:
        pass 

  
pin_container=[1212]
def change_pin():
    pin=int(input('enter you new pin: '))
    pin_container.clear()
    pin_container.append(pin)
    print(pin_container)
    
    print(f'your have successfully chanaged your ATM pin')
    
    y=input('do you want to continue plase enter(y):')
    if y=='y' or y=='yes' or y=='YES' or y=='Yes':
        return start()
    else:
        pass   

def fundtransfer():
     p=int(input('enter your pin: '))
     for i in pin_container:
         pin=i
     if p==pin_container[0] or p==pin_container[-1]:
            print('select your bank accout type below')
            print('1. Savings')
            print('2. Current')
            print('3. CD')
            select=int(input('ENTER ACCOUNT TYPE: '))
            if select==1:
                print('your current acc balance is 10000.00 cr')
                bal=int(input('enter amount to transfer: '))
                if bal>10000:
                    print('your acc bal is 10000.00 cr please enter amout less than your acc bal')
                    return fundtransfer()
                else:
                    print(f'you have successfully transfered {bal}.00 cr')
                    print(f'your current balance is {10000-bal}.00 cr')
            elif select==2:
                print('your current acc balance is 20000.00 cr')
                bal=int(input('enter amount to transfer: '))
                if bal>20000:
                    print('your acc bal is 20000.00 cr please enter amout less than your acc bal')
                    return fundtransfer()
                else:
                    print(f'you have successfully transfered {bal}.00 cr')
                    print(f'your current balance is {20000-bal}.00 cr')
            elif select==3:
                print('your current acc balance is 50000.00 cr')
                bal=int(input('enter amount to transfer: '))
                if bal>50000:
                    print('your acc bal is 50000.00 cr please enter amout less than your acc bal')
                    return fundtransfer()
                else:
                    print(f'you have successfully transfered {bal}.00 cr')
                    print(f'your current balance is {50000-bal}.00 cr')
            else:
                print('please select right option..thankuu.')
                return fundtransfer()
     else:
            print('wrong pin...please try again')
            return fundtransfer()
            
     y=input('do you want to continue plase enter(y):')
     if y=='y' or y=='yes' or y=='YES' or y=='Yes':
        return start()
     else:
        pass
    
def download_mini_st():
    print('select your bank accout type below')
    print('1. Savings')
    print('2. Current')
    print('3. CD')
    select=int(input('ENTER ACCOUNT TYPE: '))
    if select==1:
        print('Statement downoaded successfully of your savings bank...')
    elif select==2:
        print('Statement downloaded successfully of your current bank...')
    elif select==3:
        print('Statement dowloaded successfully of your CD bank...')
    else:
        print('please select right option..thankuu.')
        return balance_check()
    
    
    y=input('do you want to continue plase enter(y):')
    if y=='y' or y=='yes' or y=='YES' or y=='Yes':
        return start()
    else:
        pass
    
start()