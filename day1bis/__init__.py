from dataclasses import dataclass

letters = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

@dataclass
class Match():
    pos: int
    number: str

def lreplace(l: str) -> str:
    smallest = None
    for k in letters:
        i = l.find(k)
        if i >= 0:
            if smallest is None or smallest.pos > i:
                smallest = Match(pos=i, number=k)
    if smallest is None:
        return l
    for i in range(smallest.pos):
        if l[i].isdigit():
            return l
    end = smallest.pos + len(smallest.number)
    return l[0:smallest.pos] + letters[smallest.number] + l[end:]

def rreplace(l: str) -> str:
    greatest = None
    for k in letters:
        i = l.rfind(k)
        if i >= 0:
            if greatest is None or greatest.pos < i:
                greatest = Match(pos=i, number=k)
    if greatest is None:
        return l
    end = greatest.pos + len(greatest.number)
    for i in range(end, len(l)):
        if l[i].isdigit():
            return l
    return l[0:greatest.pos] + letters[greatest.number] + l[end:]
    

def line_value(l: str) -> int:
    l = rreplace(lreplace(l))
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
