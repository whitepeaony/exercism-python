import re

def _headers(line: str) -> (str, bool): 
    m =re.match('(?P<level>#+) +(?P<header>.*)', line)
    if m:
        n = len(m.group('level'))
        return "<h{}>{}</h{}>".format(n, m.group('header'), n), True
    else: 
        return line, False

def _boldness(line: str) -> str:
    return re.sub('__(.+?)__', '<strong>\1</strong>', line)

def _italicisation(line: str) -> str:
    '''
    Run after _boldness, to avoid confusiuon with double underline
    '''
    return re.sub('_(.+?)_', '<em>\1</em>', line)
   
def _bullet(line: str, inlist: bool ) -> (str, bool):
    m = re.match(r' *\* +(.*)', line)
    if m and inlist:
        return "<li>{}</li>".format(m.group(1)), True

    elif m and not inlist:
        return "<ul><li>{}</li>".format(m.group(1)), True

    elif not m and inlist:
        return "</ul>{}".format(line), False

    elif not m and not inlist:
        return line, False

def _paragraph(line):
    return '<p>{}</p>'.format(line)



def parse(markdown: str) -> str:
    lines = markdown.split('\n')
    result = ''
    for l in lines:
        result += _headers(l)
    return result
    
