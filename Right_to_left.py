def left_join(phrases: tuple) -> str:
    result=""
    lst=list(phrases)
    lst = [w.replace('right','left') for w in lst]
    for word in lst:
        result=result+word+','
    print(result[:-1])
    return result[:-1]
        
assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
assert left_join(("brightness wright",)) == "bleftness wleft"
assert left_join(("enough", "jokes")) == "enough,jokes"

print("The mission is done! Click 'Check Solution' to earn rewards!")
