base1 = "On the "  
base2 = " day of Christmas my true love gave to me: " 
last = "a Partridge in a Pear Tree."
items = [
    "twelve Drummers Drumming, ",
    "eleven Pipers Piping, ",
    "ten Lords-a-Leaping, ",
    "nine Ladies Dancing, ",
    "eight Maids-a-Milking, ",
    "seven Swans-a-Swimming, ",
    "six Geese-a-Laying, ",
    "five Gold Rings, ",
    "four Calling Birds, ",
    "three French Hens, ",
    "two Turtle Doves, ",
    "and a Partridge in a Pear Tree."
]

days = [ 'second',
'third',
'fourth',
'fifth',
'sixth',
'seventh',
'eigth',
'ninth',
'tenth',
'eleventh',
'twelfth'
]

def recite(start_verse, end_verse):
    verses = [verse(i) for i in range(start_verse, end_verse + 1)]
    return verses
        

def verse(number):
    if number == 1:
        return base1 + 'first' + base2 + last 
    var = ''.join(items[-number:])
    return base1 + days[number - 2] + base2 + var

