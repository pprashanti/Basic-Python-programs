n=int(input("enter the integer upto which u want to find the sum of integers"))
i=1
sum=0

while i<=n:
    sum+=i
    i+=1

print("the no. entered is "+str(n))
print("the sum is "+str(sum))