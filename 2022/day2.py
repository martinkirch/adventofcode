lines = open("day2_input.txt").readlines()

def match(opponent, me):
    choice_points = ord(me) - ord('W')
    match (ord(opponent) - ord('A') - ord(me) + ord('X')) % 3:
        case 0:
            return 3 + choice_points
        case 1:
            return choice_points
        case 2:
            return 6 + choice_points

score = 0
for line in lines:
    splitted = line.strip().split()
    score += match(splitted[0], splitted[1])

print(f"part one: {score}")

score_map = {
    'X': 0,
    'Y': 3,
    'Z': 6 
}

def guess(opponent, outcome):
    opponent_i = ord(opponent) - ord('A')
    match outcome:
        case 'X': # let's loose
            me = (opponent_i + 2) % 3
        case 'Y': # let's draw
            me = opponent_i
        case 'Z': # let's win
            me = (opponent_i + 1) % 3

    return score_map[outcome] + me + 1


score = 0
for line in lines:
    splitted = line.strip().split()
    score += guess(splitted[0], splitted[1])

print(f"part two: {score}")
