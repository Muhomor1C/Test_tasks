def get_most_character_example1(string: str) -> tuple:
    if (type(string) is not str) or not string.isalpha():
        print('invalid characters in the string')
        return ()
    lower_string = string.lower()
    character = max(lower_string, key=lower_string.count)
    count_character = lower_string.count(character)
    return character, count_character


def get_most_character_example2(string: str) -> tuple:
    if (type(string) is not str) or not string.isalpha():
        print('invalid characters in the string')
        return ()
    sorted_lower_string = sorted(string.lower())
    set_of_symbols_from_string = set(sorted_lower_string)
    count_character = 0
    character = ''
    for i in set_of_symbols_from_string:
        current_count = sorted_lower_string.count(i)
        if current_count > count_character:
            character = i
            count_character = current_count
    return character, count_character


def extract_sqrt(num: int) -> int or None:
    if not type(num) is int:
        print('invalid number')
        return None
    sqrt = pow(abs(num), 0.5)  # or abs(num) ** 0.5
    if sqrt % 1 == 0:
        return int(sqrt)
    return None


def checking_brackets(string: str) -> bool:
    # lazy checking in case of a very long string
    if (type(string) is not str) or string.count('(') != string.count(')'):
        return False

    counter = 0
    for i in string:
        if i == '(':
            counter += 1
        elif i == ')':
            counter -= 1
        if counter < 0:
            return False
    return True
