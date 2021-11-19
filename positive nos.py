a=[]
n=int(input("Enter the no of elements :"))
for i in range(0,n):
    l=int(input("Enter the {} element : ".format(i+1)))
    a.append(l)
print("List of positive nos. are: ")
for i in range(0,n):
    if (a[i]>0):
        print(a[i], end=" ")


