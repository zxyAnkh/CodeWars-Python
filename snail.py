def snail(array):
    n = len(array)
    if n == 0:
        return []
    m = len(array[0])
    result = []
    i = j = count = 0
    flag = 1
    while 0 <= i < n and 0 <= j < m:
        if array[i][j] != '0x00':
            count += 1
            result.append(array[i][j])
            array[i][j] = '0x00'
        if count == n * n:
            break
        if flag == 1:
            if j + 1 == m or array[i][j + 1] == '0x00':
                flag = 2
                i += 1
            else:
                j += 1
        elif flag == 2:
            if i + 1 == n or array[i + 1][j] == '0x00':
                flag = 3
                j -= 1
            else:
                i += 1
        elif flag == 3:
            if j == 0 or array[i][j - 1] == '0x00':
                flag = 4
                i -= 1
            else:
                j -= 1
        elif flag == 4:
            if i == 0 or array[i - 1][j] == '0x00':
                flag = 1
                j += 1
            else:
                i -= 1
    return result