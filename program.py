def square(n):
    sum=0
    while(n>0):
        sum+=(n%10)**2
        n//=10

    return sum

number=int(input("Enter the number to check happy number:"))   
x=number
if number==1:
    print(f"Number {number}is happy number")
else:
    list=[]
    while number!=1:
        number=square(number)

        if number ==1:
            print(f"{x} is happy number")
            break
        
        elif number in list:
            print(f"The {x} is Not happy number")
            break

        
        else:
            list.append(number)
