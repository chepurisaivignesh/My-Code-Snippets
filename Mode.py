a=input()
k=list(map(str,a.split(" ")))
print(k)

listy=[]
for i in k:
    listy.append([i,k.count(i)])        
        
print(listy)

maxi=listy[0][1]

for j in range(len(listy)):
    if listy[j][1]>maxi:
            maxi=listy[j][1]
ans=[]
for l in range(len(listy)):
    if listy[l][1]==maxi:
        ans.append(int(listy[l][0]))
print(ans)        
answer=set(ans) 

for i in answer:
           
    print(i,end=" ")