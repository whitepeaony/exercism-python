import re


def _headers(line: str) -> str: 
    m =re.match('(?P<level>#+) +(?P<header>.*)', line)
    if m:
        n = len(m.group('level'))
        return "<h{}>{}</h{}>".format(n, m.group('header'), n)
    else: 
        return line

def _boldness(line: str) -> str:
    return re.sub('__(.+?)__', '<strong>\1</strong>', line)

def _italicisation(line: str) -> str:
    '''
    Run after _boldness, to avoid confusiuon with double underline
    '''
    return re.sub('_(.+?)_', '<em>\1</em>', line)
   
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
    result = ''
    for l in lines:
        result += _headers(l)
    return result
    
