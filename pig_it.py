def pig_it(text):
    #your code here
    strlist = text.split(' ')
    letter = 'QAZWSXEDCRFVTGBYHNUJMIKOLPqazwsxedcrfvtgbyhnujmikop'
    result = []
    for s in strlist:
        if len(s) > 1:
            s = s[1:] + s[0] + 'ay'
        elif len(s) == 1 and s in letter:
            s += 'ay'
        result.append(s)
    return ' '.join(result)