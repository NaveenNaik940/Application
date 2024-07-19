list1=[]
list2=[]
l1=int(input("Enetr the length of list1: "))
l2=int(input("ENter the length of list2: "))

print(f"Enter the names for list1 to be added: ")
for i in range(l1+1):
    list1.append(input("Enter the friend name: "))

print(f"Enter the names for list2 to be added: ")
for i in range(l2+1):
    list2.append(input("Enter the friend name: "))

print(f"common friends name will be  from list1 and list 2 is: ")
l3=[]
for i in list1:
    if i in list2:
        l3.append(i)
print(f"{l3}")