def easy_unpack(elements: tuple) -> tuple:
    try:
        x, y, z = elements[0], elements[2], elements [-2]
    except:
        return False
    return (x, y, z)


print("Example:")
print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
assert easy_unpack((6, 3, 7)) == (6, 7, 3)

print("The mission is done! Click 'Check Solution' to earn rewards!")
