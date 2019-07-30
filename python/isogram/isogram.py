def is_isogram(string):

    white_string = string.replace(' ', '').replace('-', '').lower()

    letters = list(white_string)

    b = [letters.count(char) for char in letters]

    if len(b) == 0:
        return True
    else:
        return not max(b) > 1

