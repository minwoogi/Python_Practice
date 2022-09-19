N = input()
lst = []
for i in range(len(N)):
    lst.append(int(N[i]))
lst.sort(reverse=True)
for i in lst:
    print(i,end="")