from collections import defaultdict
groupA,groupB=defaultdict(list),list()
n,m=map(int,input().split())
temp=[]
for i in range(n+m):   
    groupA:.append(input()) if i<n else groupB.append(input()) 
for string in groupB: 
    if(string not in ans["groupA"]):
        print(-1)
        continue
    else: print(" ".join(map(str,groupA[string])))
    #this didnot work well
