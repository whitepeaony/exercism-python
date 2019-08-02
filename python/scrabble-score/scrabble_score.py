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

    total = 0
    for l in word.lower():
        for pts, group in scores.items():
            if l in group:
                total += pts
                break
    return total
