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
    def __init__(self, number: int, verifiers: list, correct: int = 0):
        self.number = number
        self.verifiers = verifiers
        self.correct = correct

    def verify_any(self, code: Code) -> bool:
        return any(v(code) for v in self.verifiers)

    def verify_find(self, code: Code) -> bool:
        for i in self.verifiers:
            if i(code):
                return i

        return False

    def verify_real(self, code: Code) -> bool:
        return self.verify_find(code) == self.correct

    def __str__(self):
        resp = ""
        resp += f"Verifier {self.number} {'{'} \n"
        for x in self.verifiers:
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


# Compares the second number to 4
verifier_4 = Verifier(4, [
    Check(lambda c: c.numbers[1] < 4, "Check if num[1] < 4"),
    Check(lambda c: c.numbers[1] == 4, "Check if num[1] == 4"),
    Check(lambda c: c.numbers[1] > 4, "Check if num[1] > 4"),
])

# Checks how many numbers equal 3

verifier_9 = Verifier(9, [
    Check(lambda c: sum([c.numbers[0] == 3, c.numbers[1] == 3, c.numbers[2] == 3]) == 0, "Check if no num == 3"),
    Check(lambda c: sum([c.numbers[0] == 3, c.numbers[1] == 3, c.numbers[2] == 3]) == 1, "Check if one num == 3"),
    Check(lambda c: sum([c.numbers[0] == 3, c.numbers[1] == 3, c.numbers[2] == 3]) == 2, "Check if two nums == 3"),
    Check(lambda c: sum([c.numbers[0] == 3, c.numbers[1] == 3, c.numbers[2] == 3]) == 3, "Check if three nums == 3"),
])

# Compares the first number to the third number
verifier_12 = Verifier(12, [
    Check(lambda c: c.numbers[0] < c.numbers[2], "Check if num[0] < num[2]"),
    Check(lambda c: c.numbers[0] == c.numbers[2], "Check if num[0] == num[2]"),
    Check(lambda c: c.numbers[0] > c.numbers[2], "Check if num[0] > num[2]"),
])

# Checks which number is greater than both of the others
verifier_15 = Verifier(15, [
    Check(lambda c: c.numbers[0] > c.numbers[1] and c.numbers[0] > c.numbers[2], "Check if num[0] smallest"),
    Check(lambda c: c.numbers[1] > c.numbers[0] and c.numbers[1] > c.numbers[2], "Check if num[1] smallest"),
    Check(lambda c: c.numbers[2] > c.numbers[0] and c.numbers[2] > c.numbers[1], "Check if num[2] smallest"),
])

# Checks if the sum of numbers is odd or even
verifier_18 = Verifier(18, [
    Check(lambda c: sum(c.numbers) % 2 == 0, "Check if sum of nums even"),
    Check(lambda c: sum(c.numbers) % 2 != 0, "Check if sum of nums odd"),
])
