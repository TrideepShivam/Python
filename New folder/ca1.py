#create a list for first 30 prime numbers in reverse order
prime = []
n=1
while True:
    if len(prime)==30:
        break
    else:
        n+=1
        i=2
        while i<=n:
            if n%i==0:
                break
            else:
                i+=1
                continue
        if n==i:
            prime.append(n)
i=0
# while i<30:
#     temp=prime[i]
#     prime[i]=prime[29-i]
#     prime[29-i]=temp
#     i+=1
prime.reverse()
print(prime)