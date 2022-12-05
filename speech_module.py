FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
OTHER_TENS = [
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]
HUNDRED = "hundred"


def checkio(number):
    result = []
    assert 0 < number < 1000, 'number is out of supported range (1-999)'
    if 100 <= number < 1000:
        result.append(FIRST_TEN[(number // 100) - 1])
        result.append(HUNDRED)
        number = number % 100
    if 20 <= number <= 99:
        result.append(OTHER_TENS[(number // 10) - 2])
        number = number % 10
    elif 10 <= number <= 19:
        result.append(SECOND_TEN[number - 10])
        number = 0
    if 1 <= number <= 9:
        result.append(FIRST_TEN[number - 1])
    return ' '.join(result)


def first_(num):
    return FIRST_TEN[num-1]
def second_ten(num):
    num = str(num)
    return SECOND_TEN[int(num[1])]
def other_tens(num):
    num = str(num)
    print(num)
    print(int(num[0])-1,int(num[1]),int(num[2]))
    a = FIRST_TEN[int(num[0])-1]
    b = OTHER_TENS[int(num[1])-2]
    c = FIRST_TEN[int(num[2])-1]
    print(a + " " + HUNDRED + " " + b + " " + c)
    return (a + " " + HUNDRED + " " + b + " " + c)


assert checkio(21) == "twenty one"
assert checkio(100) == "one hundred"
assert checkio(50) == "fifty"
assert checkio(30) == "thirty"
assert checkio(20) == "twenty"
assert checkio(1) == "one"
assert checkio(2) == "two"
assert checkio(3) == "three"
assert checkio(4) == "four"
assert checkio(5) == "five"
assert checkio(6) == "six"
assert checkio(9) == "nine"
assert checkio(10) == "ten"
assert checkio(11) == "eleven"
assert checkio(12) == "twelve"
assert checkio(13) == "thirteen"
assert checkio(14) == "fourteen"
assert checkio(15) == "fifteen"
assert checkio(16) == "sixteen"
assert checkio(17) == "seventeen"
assert checkio(18) == "eighteen"
assert checkio(19) == "nineteen"
assert checkio(999) == "nine hundred ninety nine"
assert checkio(784) == "seven hundred eighty four"
assert checkio(777) == "seven hundred seventy seven"
assert checkio(88) == "eighty eight"
assert checkio(44) == "forty four"
assert checkio(40) == "forty"
assert checkio(50) == "fifty"
assert checkio(80) == "eighty"
assert checkio(90) == "ninety"
assert checkio(200) == "two hundred"
assert checkio(300) == "three hundred"
assert checkio(600) == "six hundred"
assert checkio(700) == "seven hundred"
assert checkio(900) == "nine hundred"
assert checkio(21) == "twenty one"
assert checkio(312) == "three hundred twelve"
assert checkio(302) == "three hundred two"
assert checkio(509) == "five hundred nine"
assert checkio(753) == "seven hundred fifty three"
assert checkio(940) == "nine hundred forty"
assert checkio(999) == "nine hundred ninety nine"

print("The mission is done! Click 'Check Solution' to earn rewards!")
