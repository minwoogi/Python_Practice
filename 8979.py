N, K = map(int,input().split())

rank = []

for _ in range(N):
    rank.append(list(map(int,input().split())))
    
rank.sort(key = lambda x : (-x[1],-x[2],-x[3]))

anw = 1
index = 0
if rank[0][0] != K:
    for i in range(1,N):
        if rank[i][0] == K:
            index = i
            
for i in range(index):
    if rank[i][1:] != rank[index][1:]:
        anw += 1            
        
print(anw)    