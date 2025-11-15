a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
add=a+b+c
d=add
if d==180:
    print("Triangle is valid")
    if a==90 or b==90 or c==90:
        print("Right angled triangle")
    elif a<90 or b<90 or c<90:
        print("Acute angled triangle")
    else:
        print("Obtuse-angled Triangle")
else:
    ("Not a valid Triangle")  





x=int(input("enter x value:"))
y=int(input("enter y value:"))
if x>0 and y>0:
    print("1")
elif x<0 and y>0:
    print("2")
elif x<0 and y<0:
    print("3")
elif x>0 and y<0:
    print("4")
elif x==0 and y==0:
    print("point")
elif x==0 and y<0:
    print("Y")
elif x==0 and y>0:
    print("Y")
elif x>0 and y==0:
    print("X")
elif x<0 and y==0:
    print("X")





z=input("Residential/commercial:")
unit=int(input("enter a unit:"))
if z=="Residential":
    if unit>0 and unit<100:
        print("cast:",unit*3)
    elif unit>100 and unit<200:
        print("cast:",unit*5)
    elif unit>200:
        print("cast:",unit*7)
    else:
        print("out of unit")
elif z=="commercial":
    if unit>0 and unit<100:
        print("cast:",unit*5)
    elif unit>100 and unit<200:
        print("cast:",unit*7)
    elif unit>200:
        print("cast:",unit*10)
    else:
        print("out of unit")





amount = int(input("Enter amount: "))

if amount >= 500:
    n500 = amount // 500
    amount = amount % 500
else:
    n500 = 0

if amount >= 200:
    n200 = amount // 200
    amount = amount % 200
else:
    n200 = 0

if amount >= 100:
    n100 = amount // 100
    amount = amount % 100
else:
    n100 = 0

if amount >= 50:
    n50 = amount // 50
    amount = amount % 50
else:
    n50 = 0

if amount >= 10:
    n10 = amount // 10
    amount = amount % 10
else:
    n10 = 0

if amount >= 5:
    n5 = amount // 5
    amount = amount % 5
else:
    n5 = 0

if amount >= 1:
    n1 = amount // 1
    amount = amount % 1
else:
    n1 = 0

print("500:", n500)
print("200:", n200)
print("100:", n100)
print("50 :", n50)
print("10 :", n10)
print("5  :", n5)
print("1  :", n1)





f=input("pizza/burger/sandwich:")
n=int(input("enter a number:"))
if f=="pizza":
    cast=200
    tax=(5/100)*cast
    print("amount:",cast*n+tax*n)
elif f=="burger":
    cast=100
    tax=(5/100)*cast
    print("amount:",cast*n+tax*n)
elif f=="sandwich":
    cast=50
    tax=(5/100)*cast
    print("amount:",cast*n+tax*n)

    

