while True:
    num = int(input())
    if num == -1:
        break;
    lst = []
    for i in range(1,int(num/2)+1):
        if num%i == 0:
            lst.append(i)
    if sum(lst) == num:
        print(num,"=",end=" ")
        print(*lst,sep=" + ")
    else:
        print(num,"is NOT perfect.")