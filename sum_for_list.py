def sum_for_list(lst):
    result = []
    alst = [abs(l) for l in lst]
    max_l = max(alst)
    primes = primeRange(max_l)
    for p in primes:
        sum = 0
        flag = False
        for l in lst:
            if l % p == 0:
                sum += l
                flag = True
        if sum != 0 or flag == True:
            result.append([p,sum])
    return result
    
def primeRange(n):
    myArray=[1 for x in range(n+1)]
    myArray[0]=0
    myArray[1]=0
    startPos=2
    while startPos <= n:
        if myArray[startPos]==1:
            key=2
            resultPos = startPos * key
            while resultPos <= n:
                myArray[resultPos] =0
                key += 1
                resultPos = startPos *key
        startPos += 1
    resultList=[]
    startPos=0
    while startPos <= n:
        if myArray[startPos] == 1:
            resultList.append(startPos)
        startPos += 1
    return resultList  