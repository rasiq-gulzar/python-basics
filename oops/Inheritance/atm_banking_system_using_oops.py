class ATM:
    def check_balance(self, savings, current,cd):
        self.savings=savings
        self.current=current
        self.cd=cd     
    def display_balance(self):
        pin=int(input('enter your pin: '))
        for i in pin_container:
            if pin==i:
                print('select your account type')
                print('1. Savings')
                print('2. Current')
                print('3. CD')
                select=int(input('ENTER ACCOUNT TYPE: '))
                if select==1:
                    print(f'Your balance in SB account is  {self.savings}.00')
                    return self.con()
                elif select==2:
                    print(f'Your balance in Current account is  {self.current}.00')
                    return self.con()
                elif select==3:
                    print(f'Your balance in CD account is  {self.cd}.00')
                    return self.con()
                else:
                    print('please select right option..thankuu.')
                    return self.display_balance()
            else:
                print('please enter right pin')
                return self.display_balance()


    def withdraw_amount(self,va):
        self.va=va
        
    def display_withdraa_amount(self):
        pin=int(input('enter your pin: '))
        for i in pin_container:
            if pin==i:
                print(f'your have successfully withdrawed the {self.va}.00')
                return self.con()
            else:
                print('please enter right pin')
                return self.display_withdraa_amount()
        
    def change_pin(self):
        prev_pin=int(input('enter your previous pin: '))
        for i in pin_container:
            if prev_pin==i:
                 pin=int(input('enter you new pin: '))
                 pin_container.clear()
                 pin_container.append(pin)
                 print(pin_container)
                 print(f'your have successfully chanaged your ATM pin')
            else:
                print('your pin is wrong')
                return self.change_pin()
        
    def con(self):
        y=input('do you want to continue plase enter(y):')
        if y=='y' or y=='yes' or y=='YES':
            return start()
        else:
            pass
        
    def fund_transfer(self):
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
                     return self.fund_transfer()
                 else:
                     print(f'you have successfully transfered {bal}.00 cr')
                     print(f'your current balance is {10000-bal}.00 cr')
                     return self.con()
             elif select==2:
                 print('your current acc balance is 20000.00 cr')
                 bal=int(input('enter amount to transfer: '))
                 if bal>20000:
                     print('your acc bal is 20000.00 cr please enter amout less than your acc bal')
                     return self.fund_transfer()
                 else:
                     print(f'you have successfully transfered {bal}.00 cr')
                     print(f'your current balance is {20000-bal}.00 cr')
                     return self.con()
             elif select==3:
                 print('your current acc balance is 50000.00 cr')
                 bal=int(input('enter amount to transfer: '))
                 if bal>50000:
                     print('your acc bal is 50000.00 cr please enter amout less than your acc bal')
                     return self.fund_transfer()
                 else:
                     print(f'you have successfully transfered {bal}.00 cr')
                     print(f'your current balance is {50000-bal}.00 cr')
                     return self.con()
             else:
                 print('please select right option..thankuu.')
                 return self.fund_transfer()
        else:
            print('wrong pin...please try again')
            return self.fund_transfer()
               
def start():
    print('WELCOM TO JK BANK ATM')
    print('Press 1 for checking balance.')
    print('Press 2 for withdrawing the amount.')
    print('Press 3 for changing the ATM PIN.')
    print('Press 4 for fund transfer.')
    # print('Press 5 for downoading mini statemnt.')
    choice=int(input('ENTER->>: '))
    atm=ATM()
    if choice ==1:
        atm.check_balance(10000,30000,50000)
        atm.display_balance()
        return start()
    elif choice==2:
        amount=int(input('enter your amount to withdraw: '))
        atm.withdraw_amount(amount)
        atm.display_withdraa_amount()
    elif choice==3:
        atm.change_pin()
    elif choice==4:
        atm.fund_transfer()
    else:
        print('enter your choice again')
        return start()
  
pin_container=[1212]          
start()