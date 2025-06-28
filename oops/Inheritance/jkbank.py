class JKBank:
    def createAccount(self):
        name=input("Enter your name: ")
        account_number=int(input("Enter your account number: "))
        balance=int(input("Enter your amount to deposit: "))
        account_holder_names.append(name)
        account_numbers.append(account_number)
        balances.append(balance)
        print("Account created successfully")
        press=input('Press y to check your account details: ')
        return self.con()
    
    
        
    def con(self):
        y=input('do you want to continue plase enter(y):')
        if y=='y' or y=='yes' or y=='YES':
            return start()
        else:
            print("Thank you for banking with us")
        
    def display_details(self):
        for i in range(len(account_numbers)):
            print("Name: ",account_holder_names[i])
            print("Account Number: ",account_numbers[i])
            print("Balance: ",balances[i])
            return self.con()
            
    def check_balance(self):
        account_number=int(input("Enter your account number: "))
        for i in range(len(account_numbers)):
            if account_number==account_numbers[i]:
                print("Balance: ",balances[i])
                return self.con()
        else:
            print("Account number not found first create your account or check your account number again")
            press=input("Press c to create your account first: ")
            if press=='c':
                return self.createAccount()
            else:
                return self.check_balance()
        
    def withdraw(self):
        account_number=int(input("Enter your account number: "))
        amount=int(input("Enter the amount to withdraw: "))
        for i in range(len(account_numbers)):
            if account_number==account_numbers[i]:
                if amount<=balances[i]:
                    balances[i]-=amount
                    print("Amount withdrawn successfully")
                    print("Balance: ",balances[i])
                else:
                    print("Insufficient balance to withdraw")
                    return self.withdraw()
                break
        else:
            print("Account number not found")
            return self.withdraw()
        
    def deposit(self):
        account_number=int(input("Enter your account number: "))
        amount=int(input("Enter the amount to deposit: "))
        for i in range(len(account_numbers)):
            if account_number==account_numbers[i]:
                balances[i]+=amount
                print("Amount deposited successfully")
                print("Balance: ",balances[i])
                return self.con()
        else:
            print("Account number not found first create your account or check your account number again")
            press=input("Press c to create your account first: ")
            if press=='c':
                return self.createAccount()
            else:
                return self.deposit()
        
    def transfer(self):
        account_number=int(input("Enter your account number: "))
        transfer_account_number=int(input("Enter the account number to transfer: "))
        amount=int(input("Enter the amount to transfer: "))
        for i in range(len(account_numbers)):
            if account_number==account_numbers[i]:
                if amount<=balances[i]:
                    balances[i]-=amount
                    print(f"Amount transferred successfully to {transfer_account_number} with the amount of {amount}")
                    print(f'Your balance: {balances[i]}')
                    return self.con()	
                else:
                    print("Insufficient balance")
                break
        else:
            print("Account number not found first create your account or check your account number again")
            press=input("Press c to create your account first: ")
            if press=='c':
                return self.createAccount()
            else:
                return self.transfer()
            
    def check_your_account_details(self):
        account_number=int(input("Enter your account number: "))
        for i in range(len(account_numbers)):
            if account_number==account_numbers[i]:
                print("Name: ",account_holder_names[i])
                print("Account Number: ",account_numbers[i])
                print("Balance: ",balances[i])
                return self.con()
        else:
            print("Account number not found first create your account or check your account number again")
            press=input("Press c to create your account first: ")
            if press=='c':
                return self.createAccount()
            else:
                return self.check_your_account_details()
            
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
            return self.con()

account_numbers=[]
account_holder_names=[]
balances=[]   
pin_container=[1212]
def start():
    print("Welcome to JK Bank")
    print("1. Create Account")
    print("2. Check Balance")
    print('3. Deposit')
    print('4. Withdraw')
    print('5. Transfer')
    print('6. Check your account details')
    print('7. Change Mpin')
    print("8. Exit")
    choice = int(input("Enter your choice: "))
    jk = JKBank()
    if choice==1:
        jk.createAccount()
        jk.display_details()
        return start()
    elif choice==2:
        jk.check_balance()
        return start()
    elif choice==3:
        jk.deposit()
        return start()
    elif choice==4:
        jk.withdraw()
        return start()
    elif choice==5:
        jk.transfer()
        return start()
    elif choice==6:
        jk.check_your_account_details()
        return start()
    elif choice==7:
        jk.change_pin()
        return start()
    elif choice==8:
        print('Thank you for banking with us') 
    else:
        print("Invalid choice")
        return start()
start()