from functools import total_ordering


test_input = "D2FE28" # literal 2021
test_input1 = "C200B40A82" # example operator "finds the sum of 1 and 2, resulting in the value 3."
test_input2 = "04005AC33890" # "finds the product of 6 and 9, resulting in the value 54"
test_input3 = "880086C3E88112" # "finds the minimum of 7, 8, and 9, resulting in the value 7."
test_input4 = "CE00C43D881120" # finds the maximum of 7, 8, and 9, resulting in the value 9
test_input5 = "F600BC2D8F" # produces 0, because 5 is not greater than 15
test_input6 = "D8005AC2A8F0" # produces 1, because 5 is less than 15
test_input7 = "9C0141080250320F1802104A08" # produces 1, because 1 + 3 = 2 * 2
puzzle_input = "E20D72805F354AE298E2FCC5339218F90FE5F3A388BA60095005C3352CF7FBF27CD4B3DFEFC95354723006C401C8FD1A23280021D1763CC791006E25C198A6C01254BAECDED7A5A99CCD30C01499CFB948F857002BB9FCD68B3296AF23DD6BE4C600A4D3ED006AA200C4128E10FC0010C8A90462442A5006A7EB2429F8C502675D13700BE37CF623EB3449CAE732249279EFDED801E898A47BE8D23FBAC0805527F99849C57A5270C064C3ECF577F4940016A269007D3299D34E004DF298EC71ACE8DA7B77371003A76531F20020E5C4CC01192B3FE80293B7CD23ED55AA76F9A47DAAB6900503367D240522313ACB26B8801B64CDB1FB683A6E50E0049BE4F6588804459984E98F28D80253798DFDAF4FE712D679816401594EAA580232B19F20D92E7F3740D1003880C1B002DA1400B6028BD400F0023A9C00F50035C00C5002CC0096015B0C00B30025400D000C398025E2006BD800FC9197767C4026D78022000874298850C4401884F0E21EC9D256592007A2C013967C967B8C32BCBD558C013E005F27F53EB1CE25447700967EBB2D95BFAE8135A229AE4FFBB7F6BC6009D006A2200FC3387D128001088E91121F4DED58C025952E92549C3792730013ACC0198D709E349002171060DC613006E14C7789E4006C4139B7194609DE63FEEB78004DF299AD086777ECF2F311200FB7802919FACB38BAFCFD659C5D6E5766C40244E8024200EC618E11780010B83B09E1BCFC488C017E0036A184D0A4BB5CDD0127351F56F12530046C01784B3FF9C6DFB964EE793F5A703360055A4F71F12C70000EC67E74ED65DE44AA7338FC275649D7D40041E4DDA794C80265D00525D2E5D3E6F3F26300426B89D40094CCB448C8F0C017C00CC0401E82D1023E0803719E2342D9FB4E5A01300665C6A5502457C8037A93C63F6B4C8B40129DF7AC353EF2401CC6003932919B1CEE3F1089AB763D4B986E1008A7354936413916B9B080"

def parse(input):
    result = ''
    for i in range(0, len(input), 2):
        result += "{0:08b}".format(int(input[i:i+2], base=16))
    return result

parsed = parse(puzzle_input)
i = 0

def parse_version_typeid():
    global i
    version = int(parsed[i:i+3], base=2)
    typeid = int(parsed[i+3:i+6], base=2)
    i += 6
    return (version, typeid)

def read_literal():
    global i
    stacked = ''
    last_group = False
    while not last_group:
        last_group = (parsed[i] == '0')
        stacked += parsed[i+1:i+5]
        i += 5
    l = int(stacked, base=2)
    print(f"literal {l}")
    return l

def sum_packets():
    total = 0
    for v in generate_sub_packets():
        total += v
    print(f"sum is {total}")
    return total

def product_packets():
    total = 1
    for v in generate_sub_packets():
        total *= v
    print(f"product is {total}")
    return total

def minimum_packets():
    minimum = None
    for v in generate_sub_packets():
        if minimum is None or v < minimum:
            minimum = v
    print(f"minimum is {minimum}")
    return minimum

def maximum_packets():
    maximum = None
    for v in generate_sub_packets():
        if maximum is None or v > maximum:
            maximum = v
    print(f"maximum is {maximum}")
    return maximum

def greater_than():
    reader = iter(generate_sub_packets())
    left = next(reader)
    right = next(reader)
    if left > right:
        return 1
    return 0

def less_than():
    reader = iter(generate_sub_packets())
    left = next(reader)
    right = next(reader)
    if left < right:
        return 1
    return 0

def equal_to():
    reader = iter(generate_sub_packets())
    left = next(reader)
    right = next(reader)
    if left == right:
        return 1
    return 0

readers_map = {
    0: sum_packets,
    1: product_packets,
    2: minimum_packets,
    3: maximum_packets,
    4: read_literal,
    5: greater_than,
    6: less_than,
    7: equal_to,
}

total_version = 0

def read_packet():
    global total_version, i
    (version, typeid) = parse_version_typeid()
    print(f"pos {i}: version {version}, typeid: {typeid}")
    total_version += version
    return readers_map[typeid]()

def generate_sub_packets():
    global i
    length_type_id = parsed[i]
    i += 1
    if length_type_id == '0':
        total_sub_length = int(parsed[i:i+15], base=2)
        # print(f"operator: total_sub_length={total_sub_length}")
        i += 15
        limit = i + total_sub_length
        while i < limit:
            yield read_packet()
    else:
        nb_sub_packets = int(parsed[i:i+11], base=2)
        # print(f"operator: nb_sub_packets={nb_sub_packets}")
        i += 11
        for sub in range(nb_sub_packets):
            yield read_packet()

packet_evaluation = read_packet()
print(f"packet evaluates to {packet_evaluation}")
print(f"versions sum: {total_version}")

# phase 1: versions sum is 920
# phase 2: puzzle evaluates to 
