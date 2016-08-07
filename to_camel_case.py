def to_camel_case(text):
    #your code here
    if len(text) == 0:
        return text
    else:
        text = text.replace('-',' ')
        text = text.replace('_',' ')
        str_list = text.split(' ')
        for index in range(1, len(str_list)):
            if str_list[index] != '':
                str_list[index] = str_list[index][0].upper() + str_list[index][1:]
            else:
                continue
        return ''.join(str_list)