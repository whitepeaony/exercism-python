def score(word):

    word = word.lower()
    letters = {}

    scores = {
        1: ['a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't'],
        2: ['d', 'g'],
        3: ['b', 'c', 'm', 'p'],
        4: ['f', 'h', 'v', 'w', 'y'],
        5: ['k'],
        8: ['j', 'x'],
        10: ['q', 'z']
    }

    total = 0
    for l in word:
        for pts, group in scores.items():
            if l in group:
                letters[l] = pts
        total += letters.get(l, 0)

    return total
