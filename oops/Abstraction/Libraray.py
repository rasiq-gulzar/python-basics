from abc import ABC,abstractmethod
class User:
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def logout(self):
        pass
class Library:
    books_list=['eng','kas','urdu','math','cs']
    def __init__(self,books):
        self.__books=books
    
    def add_books(self):
        self.__books=input('enter book name: ')
        self.books_list.append(self.__books)
        
    def get_books(self):
        return self.__books
    
    def remove_book(self):
        self.__books=input('enter book to remove: ')
        if self.__books in self.books_list:
            self.books_list.remove(self.__books)
        else:
            print('no book found')
        
                
    def list_books(self):
        print(self.books_list)
        

class Product:
    product_container=[]
    def __init__(self,product):
        self.__product=product
        
    def get_private_variables(self):
        return self.product
    
    def set_data(self):
        self.__product=input('product name: ')
        self.product_container.append(self.__product)
        print('product added')
        enter=input('do you want to add more product press 1: ')
        if enter=='1':
            return self.set_data()
        else:
            return self.display_details(), start()
        
        
        
    def display_details(self):
        print(f'the product is {self.product_container}')
        
    def apply_discount(self):
        return self.product*int(0.2)
    
    def display(self):
        print(f'price is {self.__price} name is {self.__name} stock is  {self.__stock}')
        
class Electronics(Product):
    def __init__(self,product,warranty_peroid):
        Product.__init__(self,product)
        self.warranty_peroid=warranty_peroid
            
    def display_details(self):
        print(f'the product is {self.product} and the warranty {self.warranty_peroid} and discount is {self.apply_discount()}')
        
    def apply_discount(self):
        return self.product+self.product*int(0.2)
    
class Admin(User,Product):
    email_id=[]
    password=[]
    def login(self):
        email=input('enter email: ')
        password=input('enter password: ')
        self.email_id.append('admin@123')
        self.password.append('admin123')
        for i in range(len(self.email_id)):
            if email==self.email_id[i] and password==self.password[i]:
                print('login successfull')
                enter=input('do you want to add product (1) or logout (2) : ')
                if enter=='1':
                    return self.set_data()
                elif enter=='2':
                    return self.logout()
                else:
                    print('invalid input')
            
        else:
            print('invalid email or password')
            return self.login()
        
    def logout(self):
        self.email_id.clear()
        self.password.clear()
        print('logout successfull')
        enter=input('do you want to login again:')
        if enter=='yes':
            return self.login()
        
        else:
            print('thank you')
    
class Customer(User,Product):
    email_idd=[]
    passwordd=[]
    def login(self):
        email=input('enter email: ')
        password=input('enter password: ')
        self.email_idd.append('customer@123')
        self.passwordd.append('customer123')
        for i in range(len(self.email_idd)):
            if email==self.email_idd[i] and password==self.passwordd[i]:
                print('login successfull')
                enter=input('do you want to but product(1) or logout(2): ')
                if enter=='1':
                    return self.buy_product()
                elif enter=='2':
                    return self.logout()
                else:
                    print('invalid input')
            else:
                print('invalid email or password')
                return self.login()
    def logout(self):
        self.email_id.clear()
        self.password.clear()
        print('logout successfull')
        enter=input('do you want to login again:')
        if enter=='yes':
            return self.login()
        
        else:
            print('thank you')
            
    def buy_product(self):
        if self.product_container==[]:
            print('no product added')
        else:
            print(self.product_container)
            enter=input('enter product to buy: ')
            for i in range(len(self.product_container)):
                if enter==self.product_container[i]:
                    print(f'{self.product_container[i]} bought')
                    return start()
                else:
                    print('no product found')
    
def start():
    ad=Admin('laptop')   
    cu=Customer('')
    pr=Product('laptop')
    
    try:
        enter=int(input('enter 1 for admin and 2 for customer: '))
        if enter==1:
            return ad.login()
        elif enter==2:
            return cu.login()
        else:
            print('invalid input')
            return start()
    except ValueError as e:
        print(e)
    else:
        print('invalid input')
        return start()
    finally:
        print('invalid input')
        return start()
    
start()

