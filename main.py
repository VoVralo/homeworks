def passcode_checker(string: str) -> bool:
    if len(string) < 8:
        return False
    contains_lower_letter = False
    contains_upper_letter = False
    contains_specials = False
    for letter in string:
        if letter.islower():
            contains_lower_letter = True

        if letter.isupper():
            contains_upper_letter = True

        if letter in '+-/*!"№;%:?*()=':
            contains_specials = True

        if letter.isspace():
            return False

        if not letter.isascii():
            return False

    return all([contains_lower_letter, contains_upper_letter, contains_specials])


passcode = ('dDrrrrrrrrrggfhgfh+')
