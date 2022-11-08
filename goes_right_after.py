def goes_after(word: str, first: str, second: str) -> bool:
    dictrionary = set(word.strip())
    print(dictrionary)
    return False
#If more than one symbol is in the list you should always count the first one
#One of the symbols are not in the given word - your function should return False;
#Any symbol appears in a word more than once - use only the first one;
#Two symbols are the same - your function should return False;
#The condition is case sensitive, which means 'a' and 'A' are two different symbols.


assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("panorama", "a", "n") == True
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False