from verifiers import *
from itertools import combinations, product
from tree import Tree


def get_valid(check, code_list):
    remaining = []
    for i in code_list:
        if check(i):
            remaining.append(i)

    return remaining


def find_intersection(set_list: list[set]):
    intersect = set_list[0]
    for s in set_list[1:]:
        intersect = intersect.intersection(s)

    return intersect


# verifiers = [verifier_8, verifier_11, verifier_16, verifier_18, verifier_19, verifier_20]
# verifiers = [verifier_4, verifier_9, verifier_12, verifier_15, verifier_18]
# verifiers = [verifier_4, verifier_9, verifier_11, verifier_15, verifier_18]
# verifiers = [verifier_4, verifier_15, verifier_17, verifier_19, verifier_20]
# verifiers = [verifier_13, verifier_25, verifier_31, verifier_33, verifier_40, verifier_42]
# verifiers = [verifier_7, verifier_10, verifier_14, verifier_17, verifier_22]
# verifiers = [verifier_2, verifier_12, verifier_17, verifier_21, verifier_22]
# verifiers = [verifier_7, verifier_9, verifier_15, verifier_17, verifier_21]
# verifiers = [verifier_5, verifier_21, verifier_23, verifier_25, verifier_32, verifier_48]
# verifiers = [verifier_16, verifier_26, verifier_38, verifier_39]
# verifiers = [verifier_9, verifier_11, verifier_13, verifier_26, verifier_31]
verifiers = [verifier_10, verifier_22, verifier_26, verifier_39, verifier_48]

possibilities: set[str] = {
    f"{x}{y}{z}" for x in range(1, 6) for y in range(1, 6) for z in range(1, 6)
}

whitelist: set[str] = set()

for verifier in verifiers:
    verifier.set_up(possibilities)

code_set_combos = list(product(*[verifier.sets for verifier in verifiers]))

# Whitelist numbers that appear alone in a combination of 5 checks
for combo in code_set_combos:
    intersection = find_intersection(combo)
    if len(intersection) == 1:
        intersect = intersection.pop()
        whitelist.add(intersect)

print(whitelist)

# Eliminate numbers that appear in intersections with only one possibility
non_specific_verifiers = [verifier for verifier in verifiers if verifier.specific is False]

verifier_combos = list(combinations(non_specific_verifiers, len(non_specific_verifiers) - 1))
# verifier_combos = list(combinations(verifiers, len(verifiers)))
verifier_based_code_set_combos = []
for i in verifier_combos:
    verifier_based_code_set_combos.append(list(product(*[verifier.sets for verifier in i])))

for verifier in verifiers:
    verifier.set_up(whitelist)

for verifier_combo in verifier_based_code_set_combos:
    for combo in verifier_combo:
        intersection = find_intersection(combo)
        if len(intersection) == 1:
            intersect = intersection.pop()
            if intersect in whitelist:
                whitelist.remove(intersect)

print(whitelist)


# Analyze checklist
def get_next_verifier(possible):
    check_list = []

    check_possibilities = []
    for x in verifiers:
        for y in x.checks:
            check_possibilities.append([x, y])

    for check in check_possibilities:
        current_remaining_possibilities = get_valid(check[1], possible)
        if len(current_remaining_possibilities) > 0:
            check_list.append([check, current_remaining_possibilities, len(current_remaining_possibilities)])

    check_list = sorted(check_list, key=lambda x: x[2])

    next_verifier: Verifier = check_list[0][0][0]

    return next_verifier


def get_subtree(left_verifiers, possible):
    current_tree = {}
    next_verifier = get_next_verifier(possible)

    for i in next_verifier.checks:
        temp_remaining_possibilities = get_valid(i, possible)
        if len(temp_remaining_possibilities) == 1:
            verifier_string = "Verifier " + str(next_verifier.number) + " " + str(i)
            current_tree[verifier_string] = temp_remaining_possibilities[0]
        elif len(temp_remaining_possibilities) > 1:
            verifier_string = "Verifier " + str(next_verifier.number) + " " + str(i)
            new_verifiers = left_verifiers.copy()
            new_verifiers.remove(next_verifier)
            current_tree[verifier_string] = get_subtree(new_verifiers, temp_remaining_possibilities)

    return current_tree


whitelist = list(whitelist)
print(whitelist)

if len(whitelist) == 0:
    print("NO SOLUTION")
elif len(whitelist) == 1:
    print("SOLUTION: ", whitelist[0])
else:
    print("DECISION TREE:")
    tree = Tree(get_subtree(verifiers, whitelist))
    print(tree)
