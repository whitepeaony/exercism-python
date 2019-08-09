import re

def parse(markdown):
    lines = markdown.split('\n')
    text = ''
    for l in lines:
        newline = ''
        for n in range(0, 7):
            if re.match('#' * n, l):
                newline = l.replace('#' * n + ' ',  "<h{}>".format(n)) + "</h{}>".format(n)
            else: 
                newline = l
        text += newline
    return text

def boldness(markdown):
    bold = re.compile('__')
    a = bold.sub('<strong>', parse(markdown), count=1 )
    return bold.sub('</strong>', a, count=1)

print(boldness("__This will be bold__"))
    