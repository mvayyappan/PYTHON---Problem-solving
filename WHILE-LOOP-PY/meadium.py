
a=100
while a>=50:
    print(a)
    a=a-1


z=int(input("enter a number:"))
a=1
while a<=10:
    print(a,"x",z,"=",a*z)
    a=a+1



n=int(input("enter a number:"))
a=0
total=0
while a<=n:
    total=total+a
    a=a+1
print(total)



n=int(input("enter a number:"))
a=0
total=0
while a<=n:
    if a%2==0:
        total=total+a
    a=a+1
print(total)


n=int(input("enter a number:"))
a=0
total=0
while a<=n:
    if a%2==1:
        total=total+a
    a=a+1
print(total)



n=int(input("enter a number:"))
a=0
total=0
while a<=n:
    total=total+a*a
    a=a+1
print(total)



n=int(input("enter a number:"))
a=0
total=0
while a<=n:
    total=total+a*a*a
    a=a+1
print(total)



n=int(input("enter a number:"))
a=1
total=1
while a<=n:
    total=total*a
    a=a+1
print(total)


z=int(input("enter a number:"))
a=1
while a<=10:
    print(a*z,"=",z,"x",a)
    a=a+1
