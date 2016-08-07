def vowel_indices(word):
  # your code here
    vowels = ['a','e','i','o','u','y','A','E','I','O','U','Y']
    list = []
    index = 0
    for i in word:
        index += 1
        if i in vowels:
            list.append(index)
    return list