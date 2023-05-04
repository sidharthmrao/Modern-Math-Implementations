class Code:
    def __init__(self, numbers: list[int, int, int]):
        self.numbers = numbers

    def __str__(self):
        return f'Code({self.numbers})'


class Check:
    def __init__(self, check, description=""):
        self.check = check
        self.description = description

    def __call__(self, x):
        return self.check(x)

    def __str__(self):
        return "Check: " + self.description


class Verifier:
    def __init__(self, number: int, verifiers: list[Check], correct: int = 0):
        self.number = number
        self.checks = verifiers
        self.correct = correct

    def verify_any(self, code: Code) -> bool:
        return any(v(code) for v in self.checks)

    def __str__(self):
        resp = ""
        resp += f"Verifier {self.number} {'{'} \n"
        for x in self.checks:
            resp += "\t" + x.__str__() + "\n"
        resp += "}"

        return resp


class Validity_Collection:
    def __init__(self, number: int, verifiers: list, correct: int = 0):
        self.number = number
        self.verifiers = verifiers

    def verify_all(self, code: Code) -> bool:
        return all(v(code) for v in self.verifiers)

    def __str__(self):
        resp = ""
        resp += f"Verifier {self.number} {'{'} \n"
        for x in self.verifiers:
            resp += "\t" + x.__str__() + "\n"
        resp += "}"

        return resp


# Compares the first number to 3
verifier_2 = Verifier(2, [
    Check(lambda c: c.numbers[0] < 3, "if num[0] < 3"),
    Check(lambda c: c.numbers[0] == 3, "if num[0] == 3"),
    Check(lambda c: c.numbers[0] > 3, "if num[0] > 3"),
])

# Compares the second number to 4
verifier_4 = Verifier(4, [
    Check(lambda c: c.numbers[1] < 4, "if num[1] < 4"),
    Check(lambda c: c.numbers[1] == 4, "if num[1] == 4"),
    Check(lambda c: c.numbers[1] > 4, "if num[1] > 4"),
])

# Check if the first number is even or odd
verifier_5 = Verifier(5, [
    Check(lambda c: c.numbers[0] % 2 == 0, "if num[0] is even"),
    Check(lambda c: c.numbers[0] % 2 == 1, "if num[0] is odd"),
])

# Checks if the third number is even or odd
verifier_7 = Verifier(7, [
    Check(lambda c: c.numbers[2] % 2 == 0, "if num[2] is even"),
    Check(lambda c: c.numbers[2] % 2 == 1, "if num[2] is odd"),
])

# Checks how many numbers equal 1
verifier_8 = Verifier(8, [
    Check(lambda c: sum([c.numbers[0] == 1, c.numbers[1] == 1, c.numbers[2] == 1]) == 0, "if no num == 1"),
    Check(lambda c: sum([c.numbers[0] == 1, c.numbers[1] == 1, c.numbers[2] == 1]) == 1, "if one num == 1"),
    Check(lambda c: sum([c.numbers[0] == 1, c.numbers[1] == 1, c.numbers[2] == 1]) == 2, "if two nums == 1"),
    Check(lambda c: sum([c.numbers[0] == 1, c.numbers[1] == 1, c.numbers[2] == 1]) == 3, "if three nums == 1"),
])

# Checks how many numbers equal 3
verifier_9 = Verifier(9, [
    Check(lambda c: sum([c.numbers[0] == 3, c.numbers[1] == 3, c.numbers[2] == 3]) == 0, "if no num == 3"),
    Check(lambda c: sum([c.numbers[0] == 3, c.numbers[1] == 3, c.numbers[2] == 3]) == 1, "if one num == 3"),
    Check(lambda c: sum([c.numbers[0] == 3, c.numbers[1] == 3, c.numbers[2] == 3]) == 2, "if two nums == 3"),
    Check(lambda c: sum([c.numbers[0] == 3, c.numbers[1] == 3, c.numbers[2] == 3]) == 3, "if three nums == 3"),
])

# Checks the number of 4s in the code
verifier_10 = Verifier(10, [
    Check(lambda c: sum([c.numbers[0] == 4, c.numbers[1] == 4, c.numbers[2] == 4]) == 0, "if no num == 4"),
    Check(lambda c: sum([c.numbers[0] == 4, c.numbers[1] == 4, c.numbers[2] == 4]) == 1, "if one num == 4"),
    Check(lambda c: sum([c.numbers[0] == 4, c.numbers[1] == 4, c.numbers[2] == 4]) == 2, "if two nums == 4"),
    Check(lambda c: sum([c.numbers[0] == 4, c.numbers[1] == 4, c.numbers[2] == 4]) == 3, "if three nums == 4"),
])

# Compare num[0] to num[1]
verifier_11 = Verifier(11, [
    Check(lambda c: c.numbers[0] < c.numbers[1], "if num[0] < num[1]"),
    Check(lambda c: c.numbers[0] == c.numbers[1], "if num[0] == num[1]"),
    Check(lambda c: c.numbers[0] > c.numbers[1], "if num[0] > num[1]"),
])

# Compares the first number to the third number
verifier_12 = Verifier(12, [
    Check(lambda c: c.numbers[0] < c.numbers[2], "if num[0] < num[2]"),
    Check(lambda c: c.numbers[0] == c.numbers[2], "if num[0] == num[2]"),
    Check(lambda c: c.numbers[0] > c.numbers[2], "if num[0] > num[2]"),
])

# Compares the second number to the third number
verifier_13 = Verifier(13, [
    Check(lambda c: c.numbers[1] < c.numbers[2], "if num[1] < num[2]"),
    Check(lambda c: c.numbers[1] == c.numbers[2], "if num[1] == num[2]"),
    Check(lambda c: c.numbers[1] > c.numbers[2], "if num[1] > num[2]"),
])

# Checks which number is the smallest
verifier_14 = Verifier(14, [
    Check(lambda c: c.numbers[0] < c.numbers[1] and c.numbers[0] < c.numbers[2], "if num[0] smallest"),
    Check(lambda c: c.numbers[1] < c.numbers[0] and c.numbers[1] < c.numbers[2], "if num[1] smallest"),
    Check(lambda c: c.numbers[2] < c.numbers[0] and c.numbers[2] < c.numbers[1], "if num[2] smallest"),
])

# Checks which number is greater than both of the others
verifier_15 = Verifier(15, [
    Check(lambda c: c.numbers[0] > c.numbers[1] and c.numbers[0] > c.numbers[2], "if num[0] smallest"),
    Check(lambda c: c.numbers[1] > c.numbers[0] and c.numbers[1] > c.numbers[2], "if num[1] smallest"),
    Check(lambda c: c.numbers[2] > c.numbers[0] and c.numbers[2] > c.numbers[1], "if num[2] smallest"),
])

# Compares number of even numbers to number of odd numbers
verifier_16 = Verifier(16, [
    Check(lambda c: sum([i % 2 == 0 for i in c.numbers]) > sum([i % 2 != 0 for i in c.numbers]), "if more even"),
    Check(lambda c: sum([i % 2 == 0 for i in c.numbers]) < sum([i % 2 != 0 for i in c.numbers]), "if more odd"),
])

# Checks how many even numbers there are
verifier_17 = Verifier(17, [
    Check(lambda c: sum([i % 2 == 0 for i in c.numbers]) == 0, "if no even"),
    Check(lambda c: sum([i % 2 == 0 for i in c.numbers]) == 1, "if one even"),
    Check(lambda c: sum([i % 2 == 0 for i in c.numbers]) == 2, "if two even"),
    Check(lambda c: sum([i % 2 == 0 for i in c.numbers]) == 3, "if three even"),
])

# Checks if the sum of numbers is odd or even
verifier_18 = Verifier(18, [
    Check(lambda c: sum(c.numbers) % 2 == 0, "if sum of nums even"),
    Check(lambda c: sum(c.numbers) % 2 != 0, "if sum of nums odd"),
])

# Compares the sum of num[0] and num[1] to 6
verifier_19 = Verifier(19, [
    Check(lambda c: sum(c.numbers[:2]) < 6, "if sum of num[0] and num[1] < 6"),
    Check(lambda c: sum(c.numbers[:2]) == 6, "if sum of num[0] and num[1] == 6"),
    Check(lambda c: sum(c.numbers[:2]) > 6, "if sum of num[0] and num[1] > 6"),
])

# Checks if a num repeats itself
verifier_20 = Verifier(20, [
    Check(lambda c: len(set(c.numbers)) == 3, "if no num repeats"),
    Check(lambda c: len(set(c.numbers)) == 2, "if one num repeats"),
    Check(lambda c: len(set(c.numbers)) == 1, "if two nums repeat"),
])

# Checks if a number is present twice
verifier_21 = Verifier(21, [
    Check(lambda c: (c.numbers[0] == c.numbers[1] != c.numbers[2]) or (c.numbers[0] == c.numbers[2] != c.numbers[1]) or (c.numbers[1] == c.numbers[2] != c.numbers[0]), "if there is a pair"),
    Check(lambda c: not ((c.numbers[0] == c.numbers[1] != c.numbers[2]) or (c.numbers[0] == c.numbers[2] != c.numbers[1]) or (c.numbers[1] == c.numbers[2] != c.numbers[0])), "if there is no pair"),
])

# Checks if the numbers are ascending, descending, or neither
verifier_22 = Verifier(22, [
    Check(lambda c: c.numbers[0] < c.numbers[1] < c.numbers[2], "if ascending"),
    Check(lambda c: c.numbers[0] > c.numbers[1] > c.numbers[2], "if descending"),
    Check(lambda c: not (c.numbers[0] < c.numbers[1] < c.numbers[2]) and not (c.numbers[0] > c.numbers[1] > c.numbers[2]), "if neither")
])

# Compares the sum of all numbers to 6
verifier_23 = Verifier(23, [
    Check(lambda c: sum(c.numbers) < 6, "if sum of nums < 6"),
    Check(lambda c: sum(c.numbers) == 6, "if sum of nums == 6"),
    Check(lambda c: sum(c.numbers) > 6, "if sum of nums > 6"),
])

# Checks if a specific number is greater than 3
verifier_32 = Verifier(32, [
    Check(lambda c: c.numbers[0] > 3, "if num[0] > 3"),
    Check(lambda c: c.numbers[1] > 3, "if num[1] > 3"),
    Check(lambda c: c.numbers[2] > 3, "if num[2] > 3"),
])

# Checks if no sequence of numbers ascending or descending, two numbers ascending or descending, or all numbers
# ascending or descending
verifier_25 = Verifier(25, [
    Check(lambda c:
          c.numbers[0] == c.numbers[1] - 1 and c.numbers[1] == c.numbers[2] - 1 or
          c.numbers[0] == c.numbers[1] + 1 and c.numbers[1] == c.numbers[2] + 1,
          "if three nums ascending or descending"),
    Check(lambda c:
          c.numbers[0] == c.numbers[1] - 1 and c.numbers[1] != c.numbers[2] - 1 or
          c.numbers[0] == c.numbers[1] + 1 and c.numbers[1] != c.numbers[2] + 1 or
          c.numbers[0] != c.numbers[1] - 1 and c.numbers[1] == c.numbers[2] - 1 or
          c.numbers[0] != c.numbers[1] + 1 and c.numbers[1] == c.numbers[2] + 1,
          "if two num ascending or descending"),
    Check(lambda c:
          c.numbers[0] != c.numbers[1] - 1 and c.numbers[1] != c.numbers[2] - 1 and
          c.numbers[0] != c.numbers[1] + 1 and c.numbers[1] != c.numbers[2] + 1,
          "if no num ascending or descending"),
    ]
)

# Checks if a specific number is greater than 1
verifier_31 = Verifier(31, [
    Check(lambda c: c.numbers[0] > 1, "if num[0] > 1"),
    Check(lambda c: c.numbers[1] > 1, "if num[1] > 1"),
    Check(lambda c: c.numbers[2] > 1, "if num[2] > 1"),
])

# Checks if a specific number is even or odd
verifier_33 = Verifier(33, [
    Check(lambda c: c.numbers[0] % 2 == 0, "if num[0] even"),
    Check(lambda c: c.numbers[0] % 2 != 0, "if num[0] odd"),
    Check(lambda c: c.numbers[1] % 2 == 0, "if num[1] even"),
    Check(lambda c: c.numbers[1] % 2 != 0, "if num[1] odd"),
    Check(lambda c: c.numbers[2] % 2 == 0, "if num[2] even"),
    Check(lambda c: c.numbers[2] % 2 != 0, "if num[2] odd"),
])

# Compares a specific number to 3
verifier_40 = Verifier(40, [
    Check(lambda c: c.numbers[0] < 3, "if num[0] < 3"),
    Check(lambda c: c.numbers[0] == 3, "if num[0] == 3"),
    Check(lambda c: c.numbers[0] > 3, "if num[0] > 3"),
    Check(lambda c: c.numbers[1] < 3, "if num[1] < 3"),
    Check(lambda c: c.numbers[1] == 3, "if num[1] == 3"),
    Check(lambda c: c.numbers[1] > 3, "if num[1] > 3"),
    Check(lambda c: c.numbers[2] < 3, "if num[2] < 3"),
    Check(lambda c: c.numbers[2] == 3, "if num[2] == 3"),
    Check(lambda c: c.numbers[2] > 3, "if num[2] > 3"),
])

# Checks which number is the smallest or largest
verifier_42 = Verifier(42, [
    Check(lambda c: c.numbers[0] < c.numbers[1] and c.numbers[0] < c.numbers[2], "if num[0] smallest"),
    Check(lambda c: c.numbers[1] < c.numbers[0] and c.numbers[1] < c.numbers[2], "if num[1] smallest"),
    Check(lambda c: c.numbers[2] < c.numbers[0] and c.numbers[2] < c.numbers[1], "if num[2] smallest"),
    Check(lambda c: c.numbers[0] > c.numbers[1] and c.numbers[0] > c.numbers[2], "if num[0] largest"),
    Check(lambda c: c.numbers[1] > c.numbers[0] and c.numbers[1] > c.numbers[2], "if num[1] largest"),
    Check(lambda c: c.numbers[2] > c.numbers[0] and c.numbers[2] > c.numbers[1], "if num[2] largest"),
])

# Compares one specific number to another
verifier_48 = Verifier(48, [
    Check(lambda c: c.numbers[0] < c.numbers[1], "if num[0] < num[1]"),
    Check(lambda c: c.numbers[0] == c.numbers[1], "if num[0] == num[1]"),
    Check(lambda c: c.numbers[0] > c.numbers[1], "if num[0] > num[1]"),
    Check(lambda c: c.numbers[0] < c.numbers[2], "if num[0] < num[2]"),
    Check(lambda c: c.numbers[0] == c.numbers[2], "if num[0] == num[2]"),
    Check(lambda c: c.numbers[0] > c.numbers[2], "if num[0] > num[2]"),
    Check(lambda c: c.numbers[1] < c.numbers[2], "if num[1] < num[2]"),
    Check(lambda c: c.numbers[1] == c.numbers[2], "if num[1] == num[2]"),
    Check(lambda c: c.numbers[1] > c.numbers[2], "if num[1] > num[2]"),
])

