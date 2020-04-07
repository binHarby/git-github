n,t= list(map(int,input().split()))
lst=[]
for _ in range(t):lst.append(list(map(float,input().split())))
print(*[round(sum(L)/t,1) for L in list(zip(*lst))],sep="\n")
