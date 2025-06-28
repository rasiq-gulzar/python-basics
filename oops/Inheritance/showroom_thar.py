class Showroom:
    car_list=[]
    car_key_list=[]
    dict1={}
    def con(self):
        press=input('Do you want to continue press y/n--> ')
        if press=='y':
            start()
        else:
            print('Thank you for visiting')
            
    def by_a_car(self):
        print('1. Thar')
        print('2. Safari')
        print('3. Nexon')
        print('4. Harrier')
        print('5. Exit')
        choice=input('Enter--> ')
        if choice=='1':
            for i in self.car_list:
                if i=='Thar':
                    print('car already bought..')
                    return self.con()
            else:
                self.car_list.append('Thar')
                print('Congratulations! You have bought a Thar')
                self.car_key_list.append(1212)
                print('Your car key is: 1212 please keep it safe')
                self.con()
        elif choice=='2':
            for i in self.car_list:
                if i=='Safari':
                    print('car already bought..')
                    return self.con()
            else:
                self.car_list.append('Safari')
                print('Congratulations! You have bought a Safari')
                self.car_key_list.append(2323)
                print('Your car key is: 2323 please keep it safe')
        elif choice=='3':
            for i in self.car_list:
                if i=='Nexon':
                    print('car already bought..')
                    return self.con()
            else:
                self.car_list.append('Nexon')
                print('Congratulations! You have bought a Nexon')
                self.car_key_list.append(3434)
                print('Your car key is: 3434 please keep it safe')
        elif choice=='4':
            for i in self.car_list:
                if i=='Harrier':
                    print('car already bought..')
                    return self.con()
            else:
                self.car_list.append('Harrier')
                print('Congratulations! You have bought a Harrier')
                self.car_key_list.append(4545)
                print('Your car key is: 4545 please keep it safe')
        else:
            print('Thank you for visiting')
            return self.con()
        
    def drive_car(self,n):
        for i in self.dict1:
            if n==i:
                print(f'Car key mathced your car is {self.dict1[i]}')
                print('Press 1. to start the car')
                print('Press 2. accelerate the car')
                print('Press 3. to stop the car')
                press=input('Enter--> ')
                if press=='1':
                    print('Car started')
                    print('Press 2. accelerate the car')
                    print('Press 3. to stop the car')
                    press=input('Enter--> ')
                    if press=='2':
                        print('Car accelerated')
                        print('Press 3. to stop the car')
                        press=input('Enter--> ')
                        if press=='3':
                            print('Car stopped')
                            return self.con()
                        else:
                            print('Thank you for visiting')
                            return self.con()
                    elif press=='3':
                        print('first accelerate the car then stop the car')
                        return self.drive_car()
                        
                    else:
                        print('Thank you for visiting')
                        return self.con()
                elif press=='2':
                    print('first start the car then accelerate the car')
                    return self.drive_car()
                elif press=='3':
                    print('frist start the car and then accelerat the car then stop the car')
                    return self.drive_car()
                else:
                    print('Thank you for visiting')
                    return self.con()
            else:
                print('Car key not matched')
                return self.drive_car()
            
                        
    
    def drive_your_car(self):
        if self.car_list==[]:
            print('No car bought')
            press=input('would you like to buy a car press y/n--> ')
            if press=='y':
                self.by_a_car()
            else:
                self.con()
        else:
            for i in range(len(self.car_key_list)):
                self.dict1[self.car_key_list[i]]=self.car_list[i]
            print(self.dict1)
            press=input('would you like to drive a car press y/n--> ')
            if press=='y':
                print('To drive your car you need a car key which you got while buying the car')
                key=int(input('Enter your car key--> '))
                for i in self.dict1:
                    if key==i:
                        self.drive_car(key)
            else:
                print('car key not matched enter correct car key')
                self.drive_your_car()
                
    def sell_car(self):
        if self.car_list==[]:
            print('No car bought')
            press=input('would you like to buy a car press y/n--> ')
            if press=='y':
                self.by_a_car()
            else:
                self.con()
        else:
            print(f'your available cars are {self.car_list}')
            key=int(input('Enter your car key to sell your car--> '))
            if key==1212:
                self.car_list.remove('Thar')
                self.car_key_list.remove(1212)
                print('Your car has been sold')
                self.con()
            elif key==2323:
                self.car_list.remove('Safari')
                self.car_key_list.remove(2323)
                print('Your car has been sold')
                self.con()
            elif key==3434:
                self.car_list.remove('Nexon')
                self.car_key_list.remove(3434)
                print('Your car has been sold')
                self.con()
            elif key==4545:
                self.car_list.remove('Harrier')
                self.car_key_list.remove(4545)
                print('Your car has been sold')
                self.con()
            else:
                print('Car key not matched')
                self.sell_car()
        
            
                
            
                  
def start():
    print('1. By a car')
    print('2. Drive your car')
    print('3. sell your car')
    print('4. Exit')
    choice=input('Enter--> ')
    sh=Showroom()
    if choice=='1':
        sh.by_a_car()
        return start()
    elif choice=='2':
        sh.drive_your_car()
        return start()
    elif choice=='3':
        sh.sell_car()
        return start()
    else:
        print('Thank you for visiting')
        
start()
          