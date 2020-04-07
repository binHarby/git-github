from collections import deque
ans=deque()
for i in range(int(input())):   
    a=input().split()+['']
    eval(f'ans.{a[0]}({a[1]})')
print(*ans)
