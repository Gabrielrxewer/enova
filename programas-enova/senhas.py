import itertools

char_set = list("0123456789")

with open("combinations.txt", "w") as f:
    combinations = itertools.product(char_set, repeat=12)
    for combination in combinations:
        f.write(''.join(combination) + '\n')
