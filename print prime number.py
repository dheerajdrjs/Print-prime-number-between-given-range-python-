# print prime number 

l=int(input("Enter lower number : "))
u=int(input("Enter upper number : "))
i=1
for num in range(l,u+1):
    if num>1:
        for j in range(2,num):
            if(num%j==0):
                break
        else:
            print(num , end=" ")
