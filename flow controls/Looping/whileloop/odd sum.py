
low = int(input("Enter lower limit:"))
upper = int(input("Enter upper limit:"))
sum=0
while(low<=upper):
    if(low%2!=0):
        sum+=low
    low+=1
print("sum is",sum)
