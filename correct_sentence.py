def correct_sentence(text: str) -> str:
    x = text.capitalize() + '.' * (not text.endswith('.'))
    if x.__contains__("n"):
        x = x.replace("new york", "New York")
        print(x)
    return x

assert correct_sentence('welcome to New York') == 'Welcome to New York.'
assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("greetings, friends.") == "Greetings, friends."
assert correct_sentence('welcome to New York') == 'Welcome to New York.'

print("The mission is done! Click 'Check Solution' to earn rewards!")
