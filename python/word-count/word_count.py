def count_words(sentence):
    
    sentence = sentence.lower()
    words = {}
    shit = ',\n:!&@$%^&._'

    for s in shit:
        sentence = sentence.replace(s, ' ')

    for w in sentence.split():
        if w.endswith('\''):
            w = w[:-1]
        if w.startswith('\''):
            w = w[1:]
        words[w] = words.get(w, 0) + 1
    return words

