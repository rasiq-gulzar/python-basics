from abc import ABC, abstractmethod
class SocialMedia():
    @abstractmethod
    def getdetails(self):
        pass
    def add_email_pass(self):
        pass
    def login(self):
        pass
    def singUP(self):
        pass

class Facebook(SocialMedia):
    email_container=[]
    pass_container=[]
    def __init__(self,email,password):
        self.__email=email
        self.__password=password
        
    def getdetails(self):
        return self.__email,self.__password
    
    def add_email_pass(self):
        self.email_container.append(self._Facebook__email)#using name mangling
        self.pass_container.append(self._Facebook__password)
        return self.email_container, self.pass_container
    
    def singUP(self):
        email=input('Enter email: ')
        password=input('Enter password: ')
        fb=Facebook(email,password)
        fb.add_email_pass()
        print('Signup successful')
        return start()
        
    def login(self):
        if self.email_container==[]:
            print('you have not created your acc')
            press=input('Press 1 to create an account: ')
            if press=='1':
                self.singUP()
            else:
                return start()
        else:
            email=input('Enter email: ')
            password=input('Enter password: ')
            fb=Facebook(email,password)
            for i in range(len(self.email_container)):
                if email==self.email_container[i]:
                    if password==self.pass_container[i]:
                        print('Login successful')
                        return start()
                    else:
                        print('worng password')
                        return self.login()
                else:
                    print('wrong email, please check your email')
                    return self.login()
            
class Instagram(SocialMedia):
    email_container=[]
    pass_container=[]
    def __init__(self,email,password):
        self.__email=email
        self.__password=password
        
    def getdetails(self):
        return self.__email,self.__password
    
    def add_email_pass(self):
        self.email_container.append(self._Instagram__email)#using name mangling
        self.pass_container.append(self._Instagram__password)
        return self.email_container, self.pass_container
    
    def singUP(self):
        email=input('Enter email: ')
        password=input('Enter password: ')
        insta=Instagram(email,password)
        insta.add_email_pass()
        print('Signup successful')
        return start()
        
    def login(self):
        email=input('Enter email: ')
        password=input('Enter password: ')
        insta=Instagram(email,password)
        if email in self.email_container and password in self.pass_container:
            print('Login successful')
            return start()
        else:
            print('Login failed create an account')
            press=input('Press 1 to create an account: ')
            if press=='1':
                self.singUP()
            else:
                return start()
            
class Twitter(SocialMedia):
    email_container=[]
    pass_container=[]
    def __init__(self,email,password):
        self.__email=email
        self.__password=password
        
    def getdetails(self):
        return self.__email,self.__password
    
    def add_email_pass(self):
        self.email_container.append(self._Twitter__email)#using name mangling
        self.pass_container.append(self._Twitter__password)
        return self.email_container, self.pass_container
    
    def singUP(self):
        email=input('Enter email: ')
        password=input('Enter password: ')
        twit=Twitter(email,password)
        twit.add_email_pass()
        print('Signup successful')
        return start()
        
    def login(self):
        email=input('Enter email: ')
        password=input('Enter password: ')
        twit=Twitter(email,password)
        if email in self.email_container and password in self.pass_container:
            print('Login successful')
            return start()
        else:
            print('Login failed create an account')
            press=input('Press 1 to create an account: ')
            if press=='1':
                self.singUP()
            else:
                return start()
            
class LinkedIn(SocialMedia):
    email_container=[]
    pass_container=[]
    def __init__(self,email,password):
        self.__email=email
        self.__password=password
        
    def getdetails(self):
        return self.__email,self.__password
    
    def add_email_pass(self):
        self.email_container.append(self._LinkedIn__email)#using name mangling
        self.pass_container.append(self._LinkedIn__password)
        return self.email_container, self.pass_container
    
    def singUP(self):
        email=input('Enter email: ')
        password=input('Enter password: ')
        link=LinkedIn(email,password)
        link.add_email_pass()
        print('Signup successful')
        return start()
        
    def login(self):
        email=input('Enter email: ')
        password=input('Enter password: ')
        link=LinkedIn(email,password)
        if email in self.email_container and password in self.pass_container:
            print('Login successful')
            return start()
        else:
            print('Login failed create an account')
            press=input('Press 1 to create an account: ')
            if press=='1':
                self.singUP()
            else:
                return start() 
            
class Snapchat(SocialMedia):
    email_container=[]
    pass_container=[]
    def __init__(self,email,password):
        self.__email=email
        self.__password=password
        
    def getdetails(self):
        return self.__email,self.__password
    
    def add_email_pass(self):
        self.email_container.append(self._Snapchat__email)#using name mangling
        self.pass_container.append(self._Snapchat__password)
        return self.email_container, self.pass_container
    
    def singUP(self):
        email=input('Enter email: ')
        password=input('Enter password: ')
        snap=Snapchat(email,password)
        snap.add_email_pass()
        print('Signup successful')
        return start()
        
    def login(self):
        email=input('Enter email: ')
        password=input('Enter password: ')
        snap=Snapchat(email,password)
        if email in self.email_container and password in self.pass_container:
            print('Login successful')
            return start()
        else:
            print('Login failed create an account')
            press=input('Press 1 to create an account: ')
            if press=='1':
                self.singUP()
            else:
                return start()
            

            
def start():
    print('Welcome to Social Media')
    print('1. Facebook')
    print('2. Instagram')
    print('3. Twitter')
    print('4. LinkedIn')
    print('5. Snapchat')
    print('3. Exit')
    choice=input('Enter your choice: ')
    if choice=='1':
        print('1. Signup')
        print('2. Login')
        choice=input('Enter your choice: ')
        if choice=='1':
            fb=Facebook('','')
            fb.singUP()
        elif choice=='2':
            fb=Facebook('','')
            fb.login()
        else:
            print('Invalid choice')
            return start()
    elif choice=='2':
        print('1. Signup')
        print('2. Login')
        choice=input('Enter your choice: ')
        if choice=='1':
            insta=Instagram('','')
            insta.singUP()
        elif choice=='2':
            insta=Instagram('','')
            insta.login()
        else:
            print('Invalid choice')
            return start()
    elif choice=='3':
        print('1. Signup')
        print('2. Login')
        choice=input('Enter your choice: ')
        if choice=='1':
            twit=Twitter('','')
            twit.singUP()
        elif choice=='2':
            twit=Twitter('','')
            twit.login()
        else:
            print('Invalid choice')
            return start() 
    elif choice=='4':
        print('1. Signup')
        print('2. Login')
        choice=input('Enter your choice: ')
        if choice=='1':
            link=LinkedIn('','')
            link.singUP()
        elif choice=='2':
            link=LinkedIn('','')
            link.login()
        else:
            print('Invalid choice')
            return start()
    elif choice=='5':
        print('1. Signup')
        print('2. Login')
        choice=input('Enter your choice: ')
        if choice=='1':
            snap=Snapchat('','')
            snap.singUP()
        elif choice=='2':
            snap=Snapchat('','')
            snap.login()
        else:
            print('Invalid choice')
            return start()
    else:
        print('Thank you for using Social Media')
        exit()
    
start() 
