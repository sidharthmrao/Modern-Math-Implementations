from roll_sim import generate_rolls, rolls_set

ITERS = 100
SIDES = 10
TESTS = 100000

successful = 0

for i in range(TESTS):
    """
    Assume that every dice roll adds up to a number divisible by 6 (SUM % 6 = 0).
    Everyone selects a guess that would satisfy that condition.
    1/6 correct solve rate because there is a 1/6 chance of everything adding to mod 6.
    1/6 is the maximum probability because that is the probability of one dice roll working.
    """

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
        successful += 1

print(f"Success rate over {TESTS} tests: {successful/TESTS} ({successful} rounds successful).")
