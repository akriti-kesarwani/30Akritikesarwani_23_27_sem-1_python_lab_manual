a=int(input("Enter range: "))
b={}
for i in range(1,a):
 if i%2!=0:
    b[i]=i**3
print(b)