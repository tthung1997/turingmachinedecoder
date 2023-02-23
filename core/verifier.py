from core.utils import NUM_MAX, NUM_MIN, isAscending, isAscendingSequence, isAscendingSequence2, isDescending, isDescendingSequence, isDescendingSequence2, isDoubleNumber, isMultiple, isTripleNumber, sumDigits
from core.utils import circle, square, triangle
from core.utils import containsExactly, isEven, isValidProposal
from core.utils import countEvenDigits, countOddDigits

class Verifier:
    def __init__(self, criteria: list[list[int]]) -> None:
        self.criteria = criteria

    # verify if the number is in the list of satisfied numbers of the provided criterion
    def verify(self, criterionId: int, number: int) -> bool:
        return number in self.criteria[criterionId]

VERIFIERS = [
    # 0
    None,
    # 1
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) == 1],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) > 1]
    ]),
    # 2
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) < 3],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) == 3],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) > 3]
    ]),
    # 3
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) < 3],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) == 3],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) > 3]
    ]),
    # 4
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) < 4],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) == 4],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) > 4]
    ]),
    # 5
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and isEven(triangle(num))],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and not isEven(triangle(num))]
    ]),
    # 6
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and isEven(square(num))],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and not isEven(square(num))]
    ]),
    # 7
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and isEven(circle(num))],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and not isEven(circle(num))]
    ]),
    # 8
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 1, 0)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 1, 1)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 1, 2)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 1, 3)]
    ]),
    # 9
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 3, 0)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 3, 1)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 3, 2)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 3, 3)]
    ]),
    # 10
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 4, 0)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 4, 1)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 4, 2)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 4, 3)]
    ]),
    # 11
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) < square(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) == square(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) > square(num)]
    ]),
    # 12
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) < circle(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) == circle(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) > circle(num)]
    ]),
    # 13
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) < circle(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) == circle(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) > circle(num)]
    ]),
    # 14
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) < square(num) and triangle(num) < circle(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) < triangle(num) and square(num) < circle(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and circle(num) < triangle(num) and circle(num) < square(num)]
    ]),
    # 15
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) > square(num) and triangle(num) > circle(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) > triangle(num) and square(num) > circle(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and circle(num) > triangle(num) and circle(num) > square(num)]
    ]),
    # 16
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and countEvenDigits(num) > countOddDigits(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and countEvenDigits(num) < countOddDigits(num)]
    ]),
    # 17
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and countEvenDigits(num) == 0],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and countEvenDigits(num) == 1],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and countEvenDigits(num) == 2],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and countEvenDigits(num) == 3]
    ]),
    # 18
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and isEven(sumDigits(num))],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and not isEven(sumDigits(num))]
    ]),
    # 19
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) + square(num) < 6],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) + square(num) == 6],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) + square(num) > 6]
    ]),
    # 20
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and isTripleNumber(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and isDoubleNumber(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and not isTripleNumber(num) and not isDoubleNumber(num)]
    ]),
    # 21
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and isDoubleNumber(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and not isDoubleNumber(num)]
    ]),
    # 22
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and isAscending(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and isDescending(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and not isAscending(num) and not isDescending(num)]
    ]),
    # 23
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and sumDigits(num) < 6],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and sumDigits(num) == 6],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and sumDigits(num) > 6]
    ]),
    # 24
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and isAscendingSequence(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and isAscendingSequence2(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and not isAscendingSequence(num) and not isAscendingSequence2(num)]
    ]),
    # 25
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and not (isAscendingSequence(num) or isDescendingSequence(num)) and not (isAscendingSequence2(num) or isDescendingSequence2(num))],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and (isAscendingSequence2(num) or isDescendingSequence2(num))],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and (isAscendingSequence(num) or isDescendingSequence(num))]
    ]),
    # 26
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) < 3],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) < 3],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and circle(num) < 3]
    ]),
    # 27
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) < 4],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) < 4],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and circle(num) < 4]
    ]),
    # 28
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) == 1],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) == 1],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and circle(num) == 1]
    ]),
    # 29
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) == 3],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) == 3],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and circle(num) == 3]
    ]),
    # 30
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) == 4],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) == 4],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and circle(num) == 4]
    ]),
    # 31
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) > 1],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) > 1],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and circle(num) > 1]
    ]),
    # 32
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) > 3],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) > 3],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and circle(num) > 3]
    ]),
    # 33
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and isEven(triangle(num))],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and isEven(square(num))],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and isEven(circle(num))],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and not isEven(triangle(num))],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and not isEven(square(num))],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and not isEven(circle(num))]
    ]),
    # 34
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) <= square(num) and triangle(num) <= circle(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) <= triangle(num) and square(num) <= circle(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and circle(num) <= triangle(num) and circle(num) <= square(num)]
    ]),
    # 35
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) >= square(num) and triangle(num) >= circle(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) >= triangle(num) and square(num) >= circle(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and circle(num) >= triangle(num) and circle(num) >= square(num)]
    ]),
    # 36
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and isMultiple(sumDigits(num), 3)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and isMultiple(sumDigits(num), 4)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and isMultiple(sumDigits(num), 5)]
    ]),
    # 37
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) + square(num) == 4],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) + circle(num) == 4],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) + circle(num) == 4]
    ]),
    # 38
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) + square(num) == 6],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) + circle(num) == 6],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) + circle(num) == 6]
    ]),
    # 39
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) == 1],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) == 1],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and circle(num) == 1],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) > 1],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) > 1],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and circle(num) > 1]
    ]),
    # 40
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) < 3],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) < 3],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and circle(num) < 3],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) == 3],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) == 3],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and circle(num) == 3],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) > 3],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) > 3],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and circle(num) > 3]
    ]),
    # 41
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) < 4],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) < 4],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and circle(num) < 4],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) == 4],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) == 4],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and circle(num) == 4],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) > 4],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) > 4],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and circle(num) > 4]
    ]),
    # 42
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) < square(num) and triangle(num) < circle(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) < triangle(num) and square(num) < circle(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and circle(num) < triangle(num) and circle(num) < square(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) > square(num) and triangle(num) > circle(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) > triangle(num) and square(num) > circle(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and circle(num) > triangle(num) and circle(num) > square(num)]
    ]),
    # 43
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) < square(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) == square(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) > square(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) < circle(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) == circle(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) > circle(num)]
    ]),
    # 44
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) < triangle(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) == triangle(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) > triangle(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) < circle(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) == circle(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) > circle(num)]
    ]),
    # 45
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 1, 0)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 1, 1)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 1, 2)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 3, 0)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 3, 1)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 3, 2)]
    ]),
    # 46
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 3, 0)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 3, 1)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 3, 2)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 4, 0)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 4, 1)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 4, 2)]
    ]),
    # 47
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 1, 0)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 1, 1)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 1, 2)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 4, 0)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 4, 1)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and containsExactly(num, 4, 2)]
    ]),
    # 48
    Verifier([
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) < square(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) < circle(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) < circle(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) == square(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) == circle(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) == circle(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) > square(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and triangle(num) > circle(num)],
        [num for num in range(NUM_MIN, NUM_MAX + 1) if isValidProposal(num) and square(num) > circle(num)]
    ])
]