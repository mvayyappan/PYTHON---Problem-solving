shape=input("circle/square/rectangle:")
match shape:
    case "square":
        a=int(input("enter meeter:"))
        result=a**2
        print(result)
    case "rectangle":
        l=int(input("enter length meeter:"))
        b=int(input("enter meeter:"))
        result=l*b
        print(result)
    case "circle":
        r=int(input("enter radius meeter:"))
        result=22/7*r*r
        print(result)
    case _:
        print("invalid operator")

    
categories=input("electronics/fashion/groceries/books:")
price=int(input("enter the price:"))
match categories:
    case "electronics":
        discount=price*10/100
        print("discount:",discount)
        print("price:",price-discount)
    case "fashion":
        discount=price*20/100
        print("discount:",discount)
        print("price:",price-discount)
    case "groceries":
        discount=price*5/100
        print("discount:",discount)
        print("price:",price-discount)
    case"books":
        discount=("no discount:",price)
        print(discount)
    case _:
        print("invalid product:")
        
a=int(input("Enter a value:"))
convert=input("Meters/centimeters/millimeters/mile:")
match convert:
    case "Meters":
        result=a*1000
        print(result,"meters")
    case "centimeters":
        result=a*100000
        print(result,"centimeters")
    case "millimeters":
        result=a*1000000
        print(result,"millimeters")
    case "mile":
        result=a/1.609
        print(result,"mile")
    case _:
        print("Invalid Conversion")

