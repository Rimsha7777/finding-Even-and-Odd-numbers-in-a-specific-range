x1=input("enter your range in format xtoy= ")
x=(x1.split("to"))
if x[0]>x[1]:
    print("your 1st must be less than 2nd number")
elif x[0]<x[1]:
    c=range(int(x[0]),int(x[1])+1)
    for i in c:
        if i%2==0:
            print(i,"is even number")
        else:
            print(i,"is odd number")
