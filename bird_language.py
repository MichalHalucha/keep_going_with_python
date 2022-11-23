VOWELS = "aeiouy"

def translate(phrase):
    human_phrase = []
    i = 0

    while i < len(phrase):
        human_phrase.append(phrase[i])
        print(human_phrase)
        if phrase[i] in VOWELS:
            i += 3
        elif phrase[i] == ' ':
            i += 1
        else:
            i += 2
    return ''.join(human_phrase)


print("Example:")
print(translate("hieeelalaooo"))

assert translate("hieeelalaooo") == "hello"
assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translate("aaa bo cy da eee fe") == "a b c d e f"
assert translate("sooooso aaaaaaaaa") == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")
