lines = open("day6_input.txt").readlines()

def find_first_marker(msg, nb_distinct):
    i = nb_distinct
    while len(set(msg[i-nb_distinct:i])) != nb_distinct:
        i += 1
    return i

print("First half")
for input in lines:
    if input:
        print(f"first marker at {find_first_marker(input.strip(), 4)}")
print("Second half")
for input in lines:
    if input:
        print(f"first marker at {find_first_marker(input.strip(), 14)}")
