# a=[]
# n=int(input("Enter number of elements: "))
# for i in range(n):
#  b=int(input("Enter an element: "))
#  a.append(b)
# print(a)
# a.reverse()
# print("Reversed list:",a)
a=[]
n=int(input("Enter number of elements: "))
for i in range(n):
 b=int(input("Enter an element: "))
 a.append(b)
print(a)
print("Reversed list:",a[::-1])