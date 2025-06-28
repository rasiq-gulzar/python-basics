# class PrimeNumers:
#     def __init__(self,n):
#         self.n=n
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while True:
#             if self.isPrime(self.n):
#                 result=self.n
#                 self.n+=1
#                 return result
#             self.n+=1
# def is_prime(n):
#         if n<2:
#             return False
#         else:
#             for i in range(2,int(n**0.5)+1):
#                 if n%i==0:
#                     return False
#             return True

    
# p=PrimeNumers(1)
# for i in range(20):
#     print(next(p))


# def my_range(n):
#     n2=1
#     n1=0
#     while n1<n:
#         yield n2
#         n2+=2
#         n1+=1
    

# # result=my_range(10)
# for i in result:
#     print(i)
# def fibnoccie(n):
#     num1=0
#     num2=1
#     i=0
#     nextnum=1
#     while i<n:
#         yield num1
#         num1, num2=num2,num1+num2
#         i+=1
     
# for i in fibnoccie(10):
#     print(i)