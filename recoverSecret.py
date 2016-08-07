charInfo = {}
def recoverSecret(triplets):
    'triplets is a list of triplets from the secrent string. Return the string.'
    for triplet in triplets:
        registeredOrderedPair(triplet[0], triplet[1])
        registeredOrderedPair(triplet[1], triplet[2])
    
    result = ''
    while len(charInfo) > 0:
        ch = findEarliest()
        result += ch
        removeChar(ch)
    return result

def registeredOrderedPair(ch1, ch2):
    if ch1 not in charInfo:
        ch1Info = {'earlier': [], 'later': []}
    else:
        ch1Info = charInfo[ch1]
    if ch2 not in charInfo:
        ch2Info = {'earlier': [], 'later': []}
    else:
        ch2Info = charInfo[ch2]
    ch1Info['later'].extend(ch2)
    ch2Info['earlier'].extend(ch1)
    charInfo[ch1] = ch1Info
    charInfo[ch2] = ch2Info

def findEarliest():
    for ch in charInfo:
        if (len(charInfo[ch]['earlier']) == 0): 
            print(ch)
            return ch


def removeChar(chToDelete):
    del charInfo[chToDelete]
    isNotCh = lambda ch : ch != chToDelete
    for ch in charInfo:
        charInfo[ch]['earlier'] = filter(isNotCh, charInfo[ch]['earlier'])
        charInfo[ch]['later'] = filter(isNotCh, charInfo[ch]['later'])