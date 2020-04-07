n=int(input("enter a positive integer"))
f=range(1,n+1)
fact=1

if (n==0)|(n==1):
    print("factorial of "+str(n)+" is "+str(1))
else:
    for m in f:
        fact *= m

    print("factorial of " + str(n) + " is " + str(fact))

