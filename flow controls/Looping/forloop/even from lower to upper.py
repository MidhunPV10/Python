low=int(input("Enter lower limit:"))
upper=int(input("Enter upper limit:"))
for i in range(low,upper+1):
    if(i%2!=0):
        print(i)
