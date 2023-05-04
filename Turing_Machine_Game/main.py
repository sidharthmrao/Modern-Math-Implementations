from verifiers import *
from itertools import combinations, product
from tree import Tree


def get_valid(check, code_list):
    remaining = []
    for i in code_list:
        if check(i):
            remaining.append(i)

    return remaining


# Check ambiguity: Credit to Jewon
def check_ambiguity():
    blacklist = []
    checks_to_possibilities = {}
    for i in verifiers:
        for j in i.checks:
            checks_to_possibilities[j] = set(get_valid(j, possibilities))

    for i in checks_to_possibilities:
        for j in checks_to_possibilities:
            if i != j and checks_to_possibilities[i].issubset(checks_to_possibilities[j]):
                blacklist += list(checks_to_possibilities[i])

    return blacklist


# verifiers = [verifier_8, verifier_11, verifier_16, verifier_18, verifier_19, verifier_20]
# verifiers = [verifier_4, verifier_9, verifier_12, verifier_15, verifier_18]
# verifiers = [verifier_4, verifier_9, verifier_11, verifier_15, verifier_18]
# verifiers = [verifier_4, verifier_15, verifier_17, verifier_19, verifier_20]
# verifiers = [verifier_13, verifier_25, verifier_31, verifier_33, verifier_40, verifier_42]
# verifiers = [verifier_7, verifier_10, verifier_14, verifier_17, verifier_22]
# verifiers = [verifier_2, verifier_12, verifier_17, verifier_21, verifier_22]
verifiers = [verifier_7, verifier_9, verifier_15, verifier_17, verifier_21]

possibilities = [
    Code([x, y, z]) for x in range(1, 6) for y in range(1, 6) for z in range(1, 6)
]
remaining_possibilities = possibilities.copy()

n = len(verifiers)

while n > 0:
    verifier_sets = combinations(
        [i.checks for i in verifiers], n
    )

    possible_collections = []

    for i in verifier_sets:
        possible_collections.append(list(product(*i)))

    verifier_possibilities = []

    for i in possible_collections:
        for j in i:
            verifier_possibilities.append(Validity_Collection(0, j))

    if n == len(verifiers):
        remaining_verifiers = []

        current_valid_possibilities = []
        for i in verifier_possibilities:
            current_valid_possibilities = []
            for j in possibilities:
                if i.verify_all(j):
                    current_valid_possibilities.append(j)

            if len(current_valid_possibilities) == 1:
                remaining_verifiers.append((i, current_valid_possibilities))

        remaining_possibilities = [x[1][0] for x in remaining_verifiers]
    else:
        current_valid_possibilities = []
        for i in verifier_possibilities:
            current_valid_possibilities = []
            for j in possibilities:
                if i.verify_all(j):
                    current_valid_possibilities.append(j)

            if len(current_valid_possibilities) == 1 and current_valid_possibilities[0] in remaining_possibilities:
                remaining_possibilities.remove(current_valid_possibilities[0])

    n -= 1

ambiguous = check_ambiguity()
for i in ambiguous:
    if i in remaining_possibilities:
        remaining_possibilities.remove(i)

for i in remaining_possibilities:
    print(i)


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


if len(remaining_possibilities) == 0:
    print("NO SOLUTION")
elif len(remaining_possibilities) == 1:
    print("SOLUTION: ", remaining_possibilities[0])
else:
    print("DECISION TREE:")
    tree = Tree(get_subtree(verifiers, remaining_possibilities))
    print(tree)
