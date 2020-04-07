from collections import OrderedDict
ans=OrderedDict()
for i in range(int(input())):   
    a=input().split(" ")
    num=int(a.pop())
    a=" ".join(a)
    if a not in ans:
        exec(f'ans[a] = {num}')
    else:
        ans[a]+=num
for it in ans: print(it,ans[it])
