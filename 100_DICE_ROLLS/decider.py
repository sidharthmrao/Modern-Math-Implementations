from roll_sim import generate_rolls, rolls_set

ITERS = 100
SIDES = 6
TESTS = 100000

worked = 0

for i in range(TESTS):
    rolls = generate_rolls(ITERS, SIDES)
    counts = rolls_set(rolls, SIDES)

    # print(rolls)
    # print(counts)

    decisions = []
    for val in rolls:
        guess = -(sum(rolls) - val) % SIDES
        decisions.append(guess)

    # print(decisions)

    if rolls == decisions:
        worked += 1

print(worked/TESTS)