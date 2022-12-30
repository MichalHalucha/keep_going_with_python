from typing import Iterable

def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    zeros_to_add = []
    for pozycja, list_object in enumerate(donuts):
        if list_object == 0:
            print('Znalazłem zero na pozycji', pozycja)
            zeros_to_add.append(pozycja)

    zeros_to_add.reverse()
    for i in zeros_to_add:
        print(i)
        donuts.insert(i+1, 0)
    return donuts



assert list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])) == [
    1,
    0,
    0,
    2,
    3,
    0,
    0,
    4,
    5,
    0,
    0,
]
assert list(duplicate_zeros([0, 0, 0, 0])) == [0, 0, 0, 0, 0, 0, 0, 0]
assert list(duplicate_zeros([100, 10, 0, 101, 1000])) == [100, 10, 0, 0, 101, 1000]

print("The mission is done! Click 'Check Solution' to earn rewards!")
