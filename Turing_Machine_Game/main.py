from verifiers import Validity_Collection, verifier_4, verifier_9, verifier_12, verifier_15, verifier_18, Code, Verifier
from itertools import combinations

verifiers = [verifier_4, verifier_9, verifier_12, verifier_15, verifier_18]

possibilities = [
    Code([x, y, z]) for x in range(1, 6) for y in range(1, 6) for z in range(1, 6)
]

verifier_possibilities = [
    Validity_Collection(0, [a, b, c, d, e]) for a in verifiers[0].verifiers for b in verifiers[1].verifiers for c in
    verifiers[2].verifiers for d in verifiers[3].verifiers for e in verifiers[4].verifiers
]

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

# With 4
verifier_sets = combinations([verifiers[0].verifiers, verifiers[1].verifiers, verifiers[2].verifiers, verifiers[3].verifiers, verifiers[4].verifiers], 4)

verifier_possibilities = []
for i in verifier_sets:
    verifier_possibilities += [
        Validity_Collection(0, [a, b, c, d]) for a in i[0] for b in i[1] for c in
        i[2] for d in i[3]
    ]

remaining_verifiers = []

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

# With 3
verifier_sets = combinations([verifiers[0].verifiers, verifiers[1].verifiers, verifiers[2].verifiers, verifiers[3].verifiers, verifiers[4].verifiers], 3)

verifier_possibilities = []
for i in verifier_sets:
    verifier_possibilities += [
        Validity_Collection(0, [a, b, c]) for a in i[0] for b in i[1] for c in
        i[2]
    ]

remaining_verifiers = []

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

# With 2
verifier_sets = combinations([verifiers[0].verifiers, verifiers[1].verifiers, verifiers[2].verifiers, verifiers[3].verifiers, verifiers[4].verifiers], 2)

verifier_possibilities = []
for i in verifier_sets:
    verifier_possibilities += [
        Validity_Collection(0, [a, b]) for a in i[0] for b in i[1]
    ]

remaining_verifiers = []

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

# With 1
verifier_sets = combinations([verifiers[0].verifiers, verifiers[1].verifiers, verifiers[2].verifiers, verifiers[3].verifiers, verifiers[4].verifiers], 1)

verifier_possibilities = []
for i in verifier_sets:
    verifier_possibilities += [
        Validity_Collection(0, [a]) for a in i[0]
    ]

remaining_verifiers = []

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

for i in remaining_possibilities:
    print(i)
