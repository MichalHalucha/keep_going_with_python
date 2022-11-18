def end_zeros(a: int) -> int:
    x = [x for x in str(a)]
    counter=0
    x = x.__reversed__()
    for i in x:
        if i == '0':
            counter+=1
        else:
            return counter
    return 1
