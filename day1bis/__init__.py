import re
from re import Match

firstletters = re.compile("^[^0-9]*?(one|two|three|four|five|six|seven|eight|nine)")
lastletters = re.compile("(one|two|three|four|five|six|seven|eight|nine)[^0-9]*?$")

def translate(m:Match[str]) -> str:
    match m.group(1):
        case 'one':
            return "1"
        case 'two':
            return "2"
        case 'three':
            return "3"
        case 'four':
            return "4"
        case 'five':
            return "5"
        case 'six':
            return "6"
        case 'seven':
            return "7"
        case 'eight':
            return "8"
        case 'nine':
            return "9"

def line_value(l: str) -> int:
    l = firstletters.sub(translate, l)
    l = lastletters.sub(translate, l)
    first = None
    last = None
    for c in l:
        if c.isdigit():
            if first is None:
                first = c
            last = c
    return int(first + last)


def today(data:list[str]) -> int:
    return sum(line_value(l) for l in data)
