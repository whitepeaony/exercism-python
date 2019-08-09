import re


def _headers(line: str) -> str: 
    m =re.match('(?P<level>#+) +(?P<header>.*)', line)
    if m:
        n = len(m.group('level'))
        return "<h{}> {} </h{}>".format(n, m.group('header'), n)
    else: 
        return line

def _boldness(line: str) -> str:
    bold = re.compile('__')
    a = bold.sub('<strong>', _headers(line), count=1 )
    return bold.sub('</strong>', a, count=1)

def _italicisation(line: str) -> str:
    italics = re.compile('_')
    a = italics.sub('<em>', _boldness(line), count=1 )
    return italics.sub('</em>', a, count=1)

def _bullet(line: str, inlist: bool ) -> (str, bool):
    m = re.compile(r'*')
    n = re.compile(r'\n*')
    if m.match(_italicisation(line)):
        bull = m.sub('<ul><li>', _italicisation(line), count=1) + '</li></ul>'
        if n.match(bull):
            return print(n.split(bull))

    else:
        bull = m.sub('<p>', _italicisation(line), count=1)
        return bull + '</p>' 

def parse(markdown: str) -> str:
    lines = markdown.split('\n')
    
    pass
    
