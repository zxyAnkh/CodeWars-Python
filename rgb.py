def rgb(r, g, b):
    #your code here :)
    hexr = hex(r)[2:]
    hexg = hex(g)[2:]
    hexb = hex(b)[2:]
    if r < 0:
        hexr = '00'
    if g < 0:
        hexg = '00'
    if b < 0:
        hexb = '00'
    if r > 255:
        hexr = 'FF'
    if g > 255:
        hexg = 'FF'
    if b > 255:
        hexb = 'FF'
    if len(hexr) == 1:
        hexr = '0' + hexr
    if len(hexg) == 1:
        hexg = '0' + hexg
    if len(hexb) == 1:
        hexb = '0' + hexb
    return ''.join(hexr+hexg+hexb).upper()