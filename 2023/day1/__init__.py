def line_value(l: str) -> int:
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
