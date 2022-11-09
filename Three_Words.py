dgits = {"1","2","3","4","5","6","7","8","9"}

def checkio(words: str) -> bool:
    word = set(words)
    if len(dgits & word) != 0:
        return False
    elif len(words.strip(" "))<3:
        return False
    return True


assert checkio("Hello World hello") == True
assert checkio("He is 123 man") == False
assert checkio("1 2 3 4") == False
assert checkio("bla bla bla bla") == True
assert checkio("Hi") == False
