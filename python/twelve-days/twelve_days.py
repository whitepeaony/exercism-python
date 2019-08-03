base = "On the {} day of Christmas my true love gave to me: "
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
    "and a Partridge in a Pear Tree.",
]

days = ['second',
        'third',
        'fourth',
        'fifth',
        'sixth',
        'seventh',
        'eighth',
        'ninth',
        'tenth',
        'eleventh',
        'twelfth',
        ]


def recite(start_verse, end_verse):
    return [verse(i) for i in range(start_verse, end_verse + 1)]


def verse(number):
    if number == 1:
        return base.format('first') + last
    var = ''.join(items[-number:])
    return base.format(days[number - 2]) + var
