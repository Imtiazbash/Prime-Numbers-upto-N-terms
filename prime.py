import sys
n=int(input(sys.argv)) 
for n in range(2, n):
    k=1
        # all prime numbers are greater than 1
    if n > 1:
        for i in range(2,int(n/2)):
            if (n % i) == 0:
                k=2
    if(k==1):
        print(n)
            
