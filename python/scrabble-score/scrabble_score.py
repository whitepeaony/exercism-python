def score(word):

    scores = {
        1: 'aeioulnrst',
        2: 'dg',
        3: 'bcmp',
        4: 'fhvwy',
        5: 'k',
        8: 'jx',
        10: 'qz'
    }

    letters = {}
    for score, group in scores.items():
        for l in group:
            letters[l] = score 
                  
    return sum([letters[l] for l in word.lower()])

    

