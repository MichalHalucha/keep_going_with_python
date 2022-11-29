list_of_characters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","w","x","y","z"]
counted = {}

def checkio(text: str) -> str:
    text = text.lower()
    text = text.replace(" ","")
    text = list(text)
    for x in list_of_characters:
        try:
            counted[x]=text.count(x)
        except:
            continue
    print(counted)
    max_key = max(counted, key=lambda k: counted[k])
    print(max_key)
    return max_key

assert checkio("Hello World!") == "l"
assert checkio("How do you do?") == "o"
assert checkio("One") == "e"
assert checkio("Oops!") == "o"
assert checkio("AAaooo!!!!") == "a"
assert checkio("abe") == "a"

print("The mission is done! Click 'Check Solution' to earn rewards!")
