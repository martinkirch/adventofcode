import re

lettersdigit = re.compile("(one|two|three|four|five|six|seven|eight|nine)")

def line_value(l: str) -> int:
    l = lettersdigit.sub(lambda x: "<"+x.group(0)+">", l)
    l = l.replace("<one>", "1")
    l = l.replace("<two>", "2")
    l = l.replace("<three>", "3")
    l = l.replace("<four>", "4")
    l = l.replace("<five>", "5")
    l = l.replace("<six>", "6")
    l = l.replace("<seven>", "7")
    l = l.replace("<eight>", "8")
    l = l.replace("<nine>", "9")
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
