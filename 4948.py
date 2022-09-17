import math
while True:
    n = int(input())
    if n == 0 :
        break;
    elif n == 1:
        print(1)
    else:
        count = 0
        flag = [True for i in range(2*n+1)]
        for i in range(2,int(math.sqrt(2*n)+1)):
            if flag[i] == True:
                j = 2
                while i * j <= 2*n:
                    flag[i * j] = False
                    j += 1
        for i in range(n+1, 2*n+1):
            if flag[i]:
                count += 1
        print(count)
        






    





