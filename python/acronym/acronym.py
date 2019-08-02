def abbreviate(words):
    words = words.upper()
    
    crap = ',_-'

    for c in crap:
        words = words.replace(c, ' ')

    acronym = ''

    for w in words.split():
        acronym += w[0]
    return acronym
