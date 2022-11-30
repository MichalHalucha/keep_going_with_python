def to_camel_case(name: str) -> str:
    name = name.split("_")
    output = ""
    for i in name:
        output = output+i.capitalize()
    return output


assert to_camel_case("my_function_name") == "MyFunctionName"
assert to_camel_case("i_phone") == "IPhone"

print("The mission is done! Click 'Check Solution' to earn rewards!")
