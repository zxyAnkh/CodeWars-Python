def tickets(people):
    change = [0, 0, 0]
    for money in people:
        if money == 25:
            change[0] += 1
        elif money == 50:
            change[1] += 1
            change[0] -= 1
        elif money == 100:
            change[2] += 1
            if change[1] >= 1:
                change[1] -= 1
                change[0] -= 1
            else:
                change[0] -= 3
        if change[0] * 25 + change[1] * 50 + change[2] * 100 < 0 or change[0] < 0:
            return "NO"

    return "YES"