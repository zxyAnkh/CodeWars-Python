def last_digit(n1, n2):
    if n1 == 1 or n2 == 0:
        return 1
    if n2 == 1:
        return int(str(n1)[-1])
    arr = []
    for i in range(1, n2 + 1):
        if str(n1**i)[-1] in arr:
            break
        else:
            arr.append(str(n1**i)[-1])
    return int(arr[(n2-1)%len(arr)])