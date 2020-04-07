from collections import namedtuple
n,student,summ = int(input()),namedtuple("student",",".join(input().split())),0
for _ in range (n):
    summ+=int(student(*input().split()).MARKS)
print(f'{(summ/n):.2f}')
