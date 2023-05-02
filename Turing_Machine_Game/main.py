from verifiers import Validity_Collection, verifier_4, verifier_9, verifier_12, verifier_15, verifier_18, Code, Verifier
from itertools import combinations, product

verifiers = [verifier_4, verifier_9, verifier_12, verifier_15, verifier_18]
possibilities = [
    Code([x, y, z]) for x in range(1, 6) for y in range(1, 6) for z in range(1, 6)
]
remaining_possibilities = possibilities.copy()

n = len(verifiers)

while n > 0:
    verifier_sets = combinations(
        [i.verifiers for i in verifiers], n
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

            if len(current_valid_possibilities) == 1:
                try:
                    remaining_possibilities.remove(current_valid_possibilities[0])
                except:
                    pass

    n -= 1

for i in remaining_possibilities:
    print(i)
