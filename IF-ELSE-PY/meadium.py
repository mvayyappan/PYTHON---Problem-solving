a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
if a<b and a<c:
    print(a)
elif b<a and b<c:
    print(b)
else:
    print(c)

tamil=int(input("enter tamil mark:"))
eng=int(input("enter eng mark:"))
max=int(input("enter max mark:"))
science=int(input("enter science marK:"))
s_s=int(input("enter s_s mark:"))
if tamil>=35:
    print("Pass")
else:
    print("Fail")
if eng>=35:
    print("Pass")
else:
    print("Fail")
if max>=35:
    print("Pass")
else:
    print("Fail")
if science>=35:
    print("Pass")
else:
    print("Fail")
if s_s>=35:
    print("Pass")
else:
    print("Fail")


a=int(input("enter tamil subject mark:"))
b=int(input("enter English subject mark:"))
c=int(input("enter Maths subject mark:"))
average=(a+b+c)/3
print(average)
if average>=90:
    print("A")
elif average>=75 and average<90:
    print("B")
elif average>=50 and average<75:
    print("C")
else:
    print("fail")


a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
d=int(input("enter d value:"))
if a>b and a>c and a>d:
    print(a)
elif b>a and b>c and b>d:
    print(b)
elif c>a and c>b and c>d:
    print(c)
else:
    print(d)

a=int(input("enter a KG:"))
if a<=5:
    cost=10
    tax=(5/100)*cost
    print("total:",cost+tax)
elif a>5 and a<=20:
    cost=20
    tax=(5/100)*cost
    print("total:",cost+tax)
else:
    print("cost:",50*0.05+50)

a=int(input("Enter the a value:"))
if ((a%4==0 and a%100!=0) or a%400==0):
    print("Y")
else:
    print("N")


a=int(input("Enter the number x:"))
b=int(input("Enter the number y:"))
c=int(input("Enter the number z:"))
if a+b+c==180:
  print("valid triangle")
  if a==b==c:
    print("Equilateral")
  elif a==b!=c or a==c!=b or b==c!=a:
    print("iso")
  else:
    print("scalene")
else:
  print("invalid triangle")

a=int(input("enter a number:"))
total=a
if a>=0:
    total=a//5
    print("No of Buckets:",total)
    a=a%10
    print("left:",a)



a=int(input("enter a value:"))
if a<=12:
    cast=50
    print("cast:",cast)
    if a%2==0:
        print("Total_amount:",cast-5)
elif a>12 and a<=59:
    cast=100
    print("cast:",cast)
    if a%2==0:
        print("Total_amount:",cast-5)
elif a>=60:
    cast=150
    print("cast:",cast)
    if a%2==0:
        print("Total_amount:",cast-5)
else:
    print("invalid age")

a=int(input("enter a number:"))
if a<=9 and a>=-9:
    print("one digit")
elif a<=99 and a>=-99:
    print("two digit")
elif a<=999 and a>=-999:
    print("three digit")
elif a<=9999 and a>=-9999:
    print("four digit")
elif a<=99999 and a>=-99999:
    print("five digit")


height=float(input("Enter your height:"))
weight=float(input("enter your weight:"))
BMI=weight/(height**2)
print(BMI)
if BMI<=18:
    print("under_weight")
elif BMI>18 and BMI<=25:
    print("normal")
elif BMI>25 and BMI<=29:
    print("overweight")
elif BMI>=30:
    print("Obese")

num = int(input("Enter a number: "))
n = abs(num)  
while n >= 10:
    n = n // 10  
if n == 1:
    print("First digit is 1")
else:
    print("First digit is not 1")

a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
d=b**2-4*a*c
print(d)
if d>0:
    print("two real roots")
elif d==0:
    print("one real root")
elif d<0:
    print("Imaginary roots")

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