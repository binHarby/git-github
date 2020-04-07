from collections import Counter
n,lst,k=int(input()),list(map(int,input().split())),int(input())
tot,dic=int(0),dict(Counter(lst))
for _ in range(k):
    sho,mon=list(map(int,input().split()))
    if (sho in dic)and(dic[sho]>0):
        dic[sho]-=1
        tot+=mon
print(tot)


