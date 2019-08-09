import re

def parse(markdown):
    lines = markdown.split('\n')
    text = ''
    for l in lines:
        newline = ''
        for n in range(0, 7):
            if re.match('#' * n, l) is not None:
                newline = l.replace('#' * n + ' ',  "<h{}>".format(n)) + "</h{}>".format(n)
        text += newline
    return text


#re.search


print(parse("###### This will be an h6"))


