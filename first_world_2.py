import re
def first_word(text: str) -> str:
    if len(text.split()) == 1:
        try:
            if ',' in text:
                return text[:text.index(",")]
            elif '.' in text:
                return text[:text.index(".")]
        except:
            return text
    desired_list = [word.replace('.', '').replace(',', '') for word in text]
    return ''.join(desired_list).lstrip().split()[0]


assert first_word("Hello world") == "Hello"
assert first_word(" a word ") == "a"
assert first_word("don't touch it") == "don't"
assert first_word("greetings, friends") == "greetings"
assert first_word("... and so on ...") == "and"
assert first_word("hi") == "hi"
assert first_word('Hello.World') == 'Hello'

print("The mission is done! Click 'Check Solution' to earn rewards!")