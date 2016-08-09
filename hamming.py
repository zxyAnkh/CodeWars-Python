from functools import lru_cache

hammings = []

@lru_cache(None)
def hammingNum():
    for i in range(0,40):
        for j in range(0, 40):
            for k in range(0, 40):
                hammings.append(2**i * 3**j * 5**k)
    hammings.sort()
    
    
hammingNum()

def hamming(n):
    return hammings[n-1]