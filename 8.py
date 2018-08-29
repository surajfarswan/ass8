#Q1.-Get Keys Corresponding to a Value in User Defined Dictionary
dicti={}
n=int(input("Enter number of items: "))
for x in range(n):
    key=input("Enter key ")
    value=input("Enter value ")
    dicti[key]=value
print(dicti)
val=input("Enter value to find")
for y,z in dicti.items():
    if(z==val):
        print("Key of value",val,"is",y)

#Q2.- Nested Dictionary
a={}
n=int(input("Enter number of items: "))
for x in range(n):
    name=input("Enter name ")
    b={}
    marks1=int(input("Enter marks in C++ "))
    marks2=int(input("Enter marks in CST "))
    marks3=int(input("Enter marks in CN "))
    b['C++']=marks1
    b['CN']=marks2
    b['CST']=marks3
    a[name]=b
print(a)
s=input("Enter name of student :")
print(a[s])
