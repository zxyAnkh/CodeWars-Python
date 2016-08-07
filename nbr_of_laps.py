def nbr_of_laps(x, y):
    z = 0
    bigger = 0
    if x > y:
        bigger = x
    else:
        bigger = y
    while bigger > 0:
        if y % bigger == 0 and x % bigger == 0:
            z = bigger
            break
        bigger -= 1
    return [int(y/z), int(x/z)]