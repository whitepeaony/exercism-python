def is_isogram(string):

    white_string = string.replace(' ', '').replace('-', '').lower()
    b = [white_string.count(char) for char in white_string]

    return len(b) < 2 or max(b) <= 1
