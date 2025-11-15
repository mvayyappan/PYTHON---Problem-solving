month_number=int(input("enter a number:"))
match month_number:
    case 1:
        print("january")
    case 2:
        print("february")
    case 3:
        print("march")
    case 4:
        print("april")
    case 5:
        print("may")
    case 6:
        print("june")
    case 7:
        print("july")
    case 8:
        print("August")
    case 9:
        print("september")
    case 10:
        print("october")
    case 11:
        print("november")
    case 12:
       print("december")
    case _:
        print("invalid month number")

color=input("enter a color:")
match color:
    case "red":
        print("stop")
    case "yellow":
        print("wait")
    case "green":
        print("go")
    case _:
        print("invalid color")

marks=int(input("enter yours marks:"))
match marks:
    case n if n>=90:
      print("grade a")
    case n if n>=50:
      print("grade b")
    case n if n>=40:
      print("grade c")
    case n if n>=0 and n<=35:
      print("fail") 
    case _:
      print("invalid mark")

age=int(input("enter your age:"))
match age:
    case n if age<=5:
        print("Your ticket is free")
    case n if age>5 and age<12:
        print("your ticket cost is 10")
    case n if age>13 and age<64:
        print("your ticket cost is 20")
    case n if age>=65:
        print("your ticket cost is 20")


a=int(input("enter a number:"))
match a%2==0:
    case True:
        print("even")
    case False:
        print("odd")
         
payment=input("UPI/Card/Net banking/COD:")
match payment:
    case "UPI":
        print("You selected UPI payment")
    case "Card":
        print("You selected Debit/Credit Card payment")
    case "NetBanking":
        print("You selected Net Banking")
    case "COD":
        print("You selected Cash on Delivery")
    case _:
        print("Invalid Payment Mode")


a=int(input("enter a value:"))
b=int(input("enter a value:"))
operator=input("add/sub/mul/div:")
match operator:
    case "add":
        print(a+b)
    case "sub":
        print(a-b)
    case "mul":
        print(a*b)
    case "div":
        print(a/b)
    case _:
        print("invalid operator")


balance=int(input("enter a balance:"))
bank=input("withdraw/deposit:")
match bank:
    case "withdraw":
        amount=int(input("enter amount"))
        print(balance-amount)
    case "deposit":
        deposit=int(input("enter a deposit"))
        print(balance+deposit)

n=int(input("enter 2 digit positive number:"))
a=n//10
b=n%10
m=a+b
j=a*b
result=m+j
match result:
    case x if result==n:
        print("great")
    case _:
        print("Not")

