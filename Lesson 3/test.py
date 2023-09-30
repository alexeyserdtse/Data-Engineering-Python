import fnmatch


single_minute = {
    '*0': 'zero',
    '*1': 'one',
    '*2': 'two',
    '*3': 'three',
    '*4': 'four',
    '*5': 'five',
    '*6': 'six',
    '*7': 'seven',
    '*8': 'eight',
    '*9': 'nine'
}


# Your pattern
pattern = {
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '2*': 'twenty',
    '3*': 'thirdy',
    '4*': 'fourty',
    '5*': 'fifty'
}

# Strings to compare
strings = ['12', '25', '41', '50']

minute_str = []

"""
for s in strings:
    for p in pattern:
        if fnmatch.fnmatch(s, p) == True:
            minute_str.append(pattern[p])
            """
for s in strings:
    for p in single_minute:
        if fnmatch.fnmatch(s, p) == True:
            print(pattern[p])

print(minute_str)
