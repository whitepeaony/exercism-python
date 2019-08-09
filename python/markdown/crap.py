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


print(_italicisation("# Header!\n* __Bold Item__\n* _Italic Item_"))
    