def is_isogram(string):

    white_string = string.replace(' ', '').replace('-', '').lower()
    b = [white_string.count(char) for char in white_string]

    if len(b) < 2:
        return True
    else:
        return max(b) <= 1
