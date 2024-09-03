m=int(input())
n=int(input())
res=""
for i in range(m,n+1):
    if i %2 !=0:
        res= str(i) +" "+res
print(res)