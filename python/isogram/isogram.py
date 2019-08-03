def is_isogram(string):

    white_string = string.replace(' ', '').replace('-', '').lower()

    counts = {}
    for char in white_string:
        if char in counts:
            return False 
        else:
            counts[char] = True
    return True
