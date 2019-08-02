def score(word):

    word = word.lower()
    letters = {}

    scrabble = [
        ['a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't'],
        ['d', 'g'],
        ['b', 'c', 'm', 'p'],
        ['f', 'h', 'v', 'w', 'y'],
        ['k'],
        ['j', 'x'],
        ['q', 'z']
    ]
    scores = [1, 2, 3, 4, 5, 8, 10]

    total = 0
    for l in word:
        for i, s in zip(scrabble, scores):
            if l in i:
                letters[l] = s
        total += letters.get(l, 0)

    return total
