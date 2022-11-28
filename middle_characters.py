def middle(text: str) -> str:
    x = len(text)
    y = x/2
    if x % 2 == 0:
        print(text[int(y):int(y)+1])
        return text[int(y)-1:int(y)+1]
    else:
        print(text[int(y):int(y)+1])
        return text[int(y):int(y)+1]

assert middle('    few whitespaces   ') == 'it'
assert middle("example") == "m"
assert middle("test") == "es"



print("The mission is done! Click 'Check Solution' to earn rewards!")
