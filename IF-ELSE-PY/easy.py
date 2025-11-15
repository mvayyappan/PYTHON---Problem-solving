a=int(input("enter a number:"))
if a%10==2 or a%5==-2:
    print("2")
else:
    print("not 2")




n=int(input("enter a number:"))
if n>=500:
    print("your delivery cast is free")
else:
    print(n+50)



colors=(input("red/yellow/green:"))
if colors=="red":
    print("Stop")
elif colors=="yellow":
    print("Get ready")
elif colors=="green":
    print("Go")



a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
if a>=40 and b>=40 and c>=40:
    print("promoted")
else:
    print("not promoted")




weather_condition=input("weather/sunny:")
if weather_condition=="sunny":
    print("umbrella")
else:
    print("no umbrella")




x=int(input("enter a value:"))
if x<=100:
    print("bill:" "free")
elif x>=100 and x<=200:
    print("bill",x*5)
elif x>=200:
    print("bill",x*10)




a=int(input("enter a value:"))
if a%2==0 and a<0:
    print("negative even")
elif a%2==0 and a>0:
    print("positive even")
elif a%2==1 and a>0:
    print("positive odd")
elif a%2==1 and a<0:
    print("negative odd")




num = int(input("Enter a number: "))
if num < 0:
    print(-num)  
else:
    print(num)
    

n=int(input("enter n value:"))
m=int(input("enter m value:"))
add=n+m
if add%2==0:
    print("even")
else:
    print("odd")



file=input(".csv/.jpg/.doc/.pdf/.py:")
if file==".csv":
    print("This is an Excel File")
elif file==".jpg":
    print("This is an JPEG File")
elif file==".doc":
    print("This is an Word File")
elif file==".pdf":
    print("This is an PDF File")
elif file==".py":
    print("This is an Python File")
else:
    print("Unknown File Type")




a=input("username:")
b=input("password:")
username=("Ayyappan_M_V")
password=("An@2007") 
if username==a and b==password:
    print("Login Successful")
else:
    print("Access Denied")
    



a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
print(a," ",b," ",c)


                            
what_is_today=input("sunday/Monday/Tuesday/Wednesday/thursday/Friday/saturday:")
if what_is_today=="Monday" or what_is_today=="Tuesday" or what_is_today=="Wednesday" or what_is_today=="Thursday" or what_is_today=="friday":
    print("Working day")
elif what_is_today=="Saturday"  or what_is_today=="Sunday":
    print("Holiday")
else:
    print("Invalid day")



n=int(input("enter a time:"))
if n>9 and n<12:
    print("Morning Show")
elif n>12 and n<16:
    print("Matinee Show")
elif n>16 and n<20:
    print("Evening Show ")
elif n>20:
    print("night Show ")





n=int(input("enter value:"))
if  n%3==0 and n%5==0:
    print("FizzBuzz if the number is divisible by both 3 and 5")
elif n%3==0:
    print("Fizz if the number is divisible by 3")
elif n%5==0:
    print("Buzz if the number is divisible by 5")
else:
    print("The number itself if it is divisible by neither 3 nor 5")




ola=50
n=int(input("enter a km:"))
if n<=5:
    print("cast:",ola+n*10)
elif n>=6 and n<=15:
    print("cast:",ola+n*8)
elif n>15:
    print("cast:",ola+n*6)



 


    































