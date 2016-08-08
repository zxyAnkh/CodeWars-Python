def maxSequence(arr):
    if len(arr) == 0:
        return 0
    max = sum = 0   
    for e in arr:   
        sum += e   
        if max < sum:   
            max = sum   
        elif sum < 0:   
            sum = 0   
    return max