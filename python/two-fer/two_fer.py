def two_fer(name = None):
    sentence = 'One for {}, one for me.'
    if name is None:
        return sentence.format('you')
    else:
        return  sentence.format(name)

