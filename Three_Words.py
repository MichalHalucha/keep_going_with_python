dgits = {"1","2","3","4","5","6","7","8","9"}
def checkio(words: str) -> bool:
    list_words = words.split(" ")
    status = index_of_digit(list_words)
    return status

def index_of_digit(list_words):
    counter_list = 0
    for x in list_words:
        #pojedynczy_item
        for key in x:
            #pojedyczny_znak
            for item in dgits:
                #czy_znak_zawiera_cyfre
                if item == key:
                    print(key, "jest")
                    counter_list = 0
                    print("Lecimy dalej")
                    continue
                else:
                    print(key, "nie ma")
        counter_list += 1
        print("______________________________________________"+str(counter_list))
        if counter_list == 3:
            return True
    return False



assert checkio("Hello World hello") == True
assert checkio("He is 123 man") == False
assert checkio("1 2 3 4") == False
assert checkio("bla bla bla bla") == True
assert checkio("Hi") == False
assert checkio('one two 3 four five six 7 eight 9 ten eleven 12') == True
