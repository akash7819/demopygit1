#print first n odd natural numbers in reverse order
n=int(input("Enter a number"))
i=n
while i>=1:
    print(i*2-1,end=" ")
    i-=1
print()    
