import random


def generate_rolls(ITERS, DICE_SIDES):
    rolls = []

    for i in range(ITERS):
        rolls.append(random.randint(0, DICE_SIDES-1))

    return rolls


def rolls_set(VALS, DICE_SIDES):
    number_of_rolls_per_num = {}
    for i in range(DICE_SIDES):
        number_of_rolls_per_num[i] = 0

    for i in VALS:
        number_of_rolls_per_num[i] += 1

    return number_of_rolls_per_num
