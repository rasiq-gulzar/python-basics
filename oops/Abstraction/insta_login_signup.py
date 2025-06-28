from abc import ABC, abstractmethod
class SocialMedia:
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def singnUp(self):
        pass

class Instagram(SocialMedia):
    def login(self):
        if email_container == []:
            print('You have not created your account kindly create an acccount')
            press=input('do you want to create your account first kindly enter (y): ')
            if press=='y':
                return self.signUP()
            else:
                return start()
        else:
            email=input('Enter email: ')
            password=input('Enter password: ')
            for i in range(len(email_container)):
                if email == email_container[i]:
                    if password == password_container[i]:
                        print('you have sucessfully login..thankuu')
                        return start()
                    else:
                        print('wrong pass try again')
                        return self.login()
            else:
                print('wrong email')
                return self.login()
        
    def signUP(self):
        ins_email = input('Enter your email: ')
        ins_password = input('Enter your password: ')
        email_container.append(ins_email)
        password_container.append(ins_password)
        # print(email_container)
        # print(password_container)
        print('Your account has been created successfully')
        return start()
    
class Facebook(SocialMedia):
    def login(self):
        if fb_email_container == []:
            print('You have not created your account kindly create an acccount')
            press=input('do you want to create your account first kindly enter (y): ')
            if press=='y':
                return self.signUp()
            else:
                return start()
        else:
            email=input('Enter email: ')
            password=input('Enter password: ')
            for i in range(len(fb_email_container)):
                if email == fb_email_container[i]:
                    if password == fb_email_container[i]:
                        print('you have sucessfully login..thankuu')
                        return start()
                    else:
                        print('wrong pass try again')
                        return self.login()
                else:
                    print('wrong email')
                    return self.login()
            
    def signUp(self):
        fb_email = input('Enter your email: ')
        fb_password = input('Enter your password: ')
        fb_email_container.append(fb_email)
        fb_password_container.append(fb_password)
        # print(email_container)
        # print(password_container)
        print('Your account has been created successfully')
        return start()
    
class LinkedIn(SocialMedia):
    def login(self):
        if linked_email_container == []:
            print('You have not created your account kindly create an acccount')
            press=input('do you want to create your account first kindly enter (y): ')
            if press=='y':
                return self.signUp()
            else:
                return start()
        else:
            email=input('Enter email: ')
            password=input('Enter password: ')
            for i in range(len(linked_email_container)):
                if email == linked_email_container[i]:
                    if password == linked_password_container[i]:
                        print('you have sucessfully login..thankuu')
                        return start()
                    else:
                        print('wrong pass try again')
                        return self.login()
                else:
                    print('wrong email')
                    return self.login()
            
    def signUp(self):
        lin_email = input('Enter your email: ')
        lin_password = input('Enter your password: ')
        linked_email_container.append(lin_email)
        linked_password_container.append(lin_password)
        # print(email_container)
        # print(password_container)
        print('Your account has been created successfully')
        return start()

class Twitter(SocialMedia):
    def login(self):
        if twitter_email_container == []:
            print('You have not created your account kindly create an acccount')
            press=input('do you want to create your account first kindly enter (y): ')
            if press=='y':
                return self.signUp()
            else:
                return start()
        else:
            email=input('Enter email: ')
            password=input('Enter password: ')
            for i in range(len(twitter_email_container)):
                if email == twitter_email_container[i]:
                    if password == twitter_password_container[i]:
                        print('you have sucessfully login..thankuu')
                        return start()
                    else:
                        print('wrong pass try again')
                        return self.login()
                else:
                    print('wrong email')
                    return self.login()
            
    def signUp(self):
        twi_email = input('Enter your email: ')
        twi_password = input('Enter your password: ')
        twitter_email_container.append(twi_email)
        twitter_password_container.append(twi_password)
        # print(email_container)
        # print(password_container)
        print('Your account has been created successfully')
        return start()

class Snapchat(SocialMedia):
    def login(self):
        if snapchat_email_container == []:
            print('You have not created your account kindly create an acccount')
            press=input('do you want to create your account first kindly enter (y): ')
            if press=='y':
                return self.signUp()
            else:
                return start()
        else:
            email=input('Enter email: ')
            password=input('Enter password: ')
            for i in range(len(snapchat_email_container)):
                if email == snapchat_email_container[i]:
                    if password == snapchat_password_container[i]:
                        print('you have sucessfully login..thankuu')
                        return start()
                    else:
                        print('wrong pass try again')
                        return self.login()
                else:
                    print('wrong email')
                    return self.login()
            
    def signUp(self):
        snap_email = input('Enter your email: ')
        snap_password = input('Enter your password: ')
        snapchat_email_container.append(snap_email)
        snapchat_password_container.append(snap_password)
        # print(email_container)
        # print(password_container)
        print('Your account has been created successfully')
        return start()
 
email_container=[]
password_container=[]

fb_email_container=[]
fb_password_container=[]

linked_email_container=[]
linked_password_container=[]

twitter_email_container=[]
twitter_password_container=[]

snapchat_email_container=[]
snapchat_password_container=[]

def start():
    print("Welcome to Socail media platform")
    print('1. Instagram')
    print('2. Facebook')
    print('3. LinkedIn')
    print('4. Twitter')
    print('5. Snapchat')
    print('6. Exit')
    choice = input('Enter your choice: ')
    instagram=Instagram()
    facebook=Facebook()
    linkedIN=LinkedIn()
    twitter=Twitter()
    snapchat=Snapchat()
    if choice=='1':
        print('1. Login')
        print('2. SignUp')
        choice = input('Enter your choice: ')
        if choice=='1':
            instagram.login()
        elif choice=='2':
            instagram.signUP()
        else:
            print('Invalid choice')
            return start()
    elif choice=='2':
        print('1. Login')
        print('2. SignUp')
        choice = input('Enter your choice: ')
        if choice=='1':
            facebook.login()
        elif choice=='2':
            facebook.signUp()
        else:
            print('Invalid choice')
            return start()
    elif choice=='3':
        print('1. Login')
        print('2. SignUp')
        choice = input('Enter your choice: ')
        if choice=='1':
            linkedIN.login()
        elif choice=='2':
            linkedIN.signUp()
        else:
            print('Invalid choice')
            return start()
    elif choice=='4':
        print('1. Login')
        print('2. SignUp')
        choice = input('Enter your choice: ')
        if choice=='1':
            twitter.login()
        elif choice=='2':
            twitter.signUp()
        else:
            print('Invalid choice')
            return start()
    elif choice=='5':
        print('1. Login')
        print('2. SignUp')
        choice = input('Enter your choice: ')
        if choice=='1':
            snapchat.login()
        elif choice=='2':
            snapchat.signUp()
        else:
            print('Invalid choice')
            return start()
    elif choice=='6':
        print('Thank you for using our service')
    else:
        print('Invalid choice')
        return start()
        
      
start()


