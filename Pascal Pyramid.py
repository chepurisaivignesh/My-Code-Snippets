def factorial(number):
    ans=1
    if number==1 or number==0:
        return ans
    for i in range(2,number+1):
        ans=ans*i
    return ans

def combination(n,r):
    return factorial(n)//(factorial(r)*factorial(n-r))

n=int(input())
for i in range(n+1):
    line=""
    for j in range(i+1):
        line=line+str(combination(i,j))+" "
    print(line)