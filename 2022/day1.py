test_input = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

max_calories = 0
current_calories = 0
calories_per_elf = []
lines = open("day1_input.txt").readlines()
for raw in lines: #test_input.split('\n'):
    line = raw.strip()
    if line:
        current_calories += int(line)
    else:
        if current_calories > max_calories:
            max_calories = current_calories
        calories_per_elf.append(current_calories)
        current_calories = 0

calories_per_elf.append(current_calories)
if current_calories > max_calories:
    max_calories = current_calories

print(f"max_calories = {max_calories}")

calories_per_elf.sort(reverse=True)
print(f"Top-3 caloried-elved: {calories_per_elf[0:3]}, total = {calories_per_elf[0]+calories_per_elf[1]+calories_per_elf[2]}")
