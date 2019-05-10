def get_permutations(string):
    if len(string) <= 1:
        return set([string])
    string_except_last_letter = string[:-1]
    last_letter = string[-1]

    permutations_of_left_over_string = get_permutations(string_except_last_letter)
    permutations = set()

    for x in range(len(string_except_last_letter) + 1):
        for per in permutations_of_left_over_string:
            p = (per[:x] + last_letter + per[x:])
            permutations.add(p)

    return permutations


print(get_permutations('ABC'))