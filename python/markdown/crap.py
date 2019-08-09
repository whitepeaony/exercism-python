import re

def _headers(line: str) -> (str, bool): 
    m =re.match('(?P<level>#+) +(?P<header>.*)', line)
    if m:
        n = len(m.group('level'))
        return "<h{}>{}</h{}>".format(n, m.group('header'), n), True
    else: 
        return line, False

def _bold(line: str) -> str:
    return re.sub('__(.+?)__', '<strong>\1</strong>', line)

def _italic(line: str) -> str:
    '''
    Run after _boldness, to avoid confusiuon with double underline
    '''
    return re.sub('_(.+?)_', '<em>\1</em>', line)
   
def _bullet(line: str) -> (str, bool):
    m = re.match(r' *\* +(.*)', line)
    if m:
        return "<li>{}</li>".format(m.group(1)), True
    else:
        return line, False

def _paragraph(line):
    return '<p>{}</p>'.format(line)


def parse(markdown: str) -> str:
    lines = markdown.split('\n')
    result = ''
    inlist = False

    for l in lines:
        a, b = _headers(l)
        if b:
            result += a
            continue
        c, d = _bullet(l)

        
        
        
        
        _bullet(_italic(_bold(l)), inlist)
            result += c
        
    return result
    
