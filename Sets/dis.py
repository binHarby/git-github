n,st,k = input(),set(map(int, input().split())),int(input())
for i in range(k): 
    com=input().split()
    try:
        comm,num=com[0],com[1]
    except IndexError:
        comm,num=com[0],''
    try:
        eval('st.'+comm+'('+num+')')
    except KeyError: 
        pass
print(sum(st))
