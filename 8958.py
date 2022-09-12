import sys
T = int(sys.stdin.readline())
for _ in range(T):
    str = sys.stdin.readline()
    anw = 0
    a = 1
    for i in str:
        if i is 'O':
            anw += a
            a += 1
        else:
            a = 1
    print(anw)





