test_input = "D2FE28" # literal 2021
test_input2 = "38006F45291200"

def parse(input):
    result = ''
    for i in range(0, len(input), 2):
        result += "{0:08b}".format(int(input[i:i+2], base=16))
    return result

parsed = parse(test_input2)

i = 0

def parse_version_typeid():
    global i
    version = int(parsed[i:i+3], base=2)
    typeid = int(parsed[i+3:i+6], base=2)
    i += 6
    return (version, typeid)

def read_literal():
    """
    when typeid==4
    """
    global i
    stacked = ''
    last_group = False
    while not last_group:
        last_group = (parsed[i] == '0')
        stacked += parsed[i+1:i+5]
        i += 5
    return int(stacked, base=2)

while i < (len(parsed)-6):
    (version, typeid) = parse_version_typeid()
    print(f"pos {i}: version {version}, typeid: {typeid}")
    if typeid == 4:
        l = read_literal()
        print(f"literal {l}")
    else:
        length_type_id = parsed[i]
        i += 1
        if length_type_id == '0':
            total_sub_length = int(parsed[i:i+15], base=2)
            i += 15
        else:
            nb_sub_packets = int(parsed[i:i+11], base=2)
            i += 11
