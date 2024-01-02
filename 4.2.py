def kbfunction(*args, **kwargs):
 for i in args:
     print("Name:",i)
 for i in kwargs:
     print(i,":",kwargs[i])
b=input("Enter your name: ")
c=int(input("Enter your age: "))
a=input("Enter your email: ")
kbfunction(b,age=c,email=a)