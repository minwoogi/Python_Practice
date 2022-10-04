import sys
N = int(input())
lst =[]
for i in range(N):
    lst.append(list(map(int,sys.stdin.readline().split())))

lst.sort(key = lambda x:(x[0],x[1]))

for i in range(N):
    print(lst[i][0],lst[i][1])