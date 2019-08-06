def abbreviate(words):
    
    crap = ',_-'

    for c in crap:
        words = words.replace(c, ' ')
    
    separator = ''
    return separator.join([w[0] for w in words.split()]).upper()     
