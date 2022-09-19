import sys

N = int(input())
data =[]
for i in range(N):
    data.append(sys.stdin.readline().rstrip().split())

data.sort(key =lambda x:(int(x[3]),int(x[2]),int(x[1])))

print(data[-1][0])
print(data[0][0])


