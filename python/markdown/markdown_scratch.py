import re

def _parse(markdown):
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

def _boldness(markdown):
    bold = re.compile('__')
    a = bold.sub('<strong>', _parse(markdown), count=1 )
    return bold.sub('</strong>', a, count=1)

def _italicisation(markdown):
    italics = re.compile('_')
    a = italics.sub('<em>', _boldness(markdown), count=1 )
    return italics.sub('</em>', a, count=1)

def _bullet(markdown):
    m = re.compile(r'\* (.*)')
    n = re.compile(r'\n*')
    if m.match(_italicisation(markdown)):
        bull = m.sub('<ul><li>', _italicisation(markdown), count=1) + '</li></ul>'
        if n.match(bull):
            return print(n.split(bull))

    else:
        bull = m.sub('<p>', _italicisation(markdown), count=1)
        return bull + '<p>' 



print(_bullet("* Item 1\n* Item 2"))
    


m = re.match(r'\* (.*)', i)
if m:
    curr = m.group(1)
    i = '<ul><li>' + curr + '</li>'
else:
    i = '<li>' + curr + '</li>'

