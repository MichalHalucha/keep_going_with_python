from operator import mul as mult_two
mult_two = int.__mul__

assert mult_two(3, 2) == 6
assert mult_two(0, 1) == 0