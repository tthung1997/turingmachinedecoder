NUM_MIN = 111
NUM_MAX = 555

# check if a number is a valid proposal
# a proposal is valid if it has exactly 3 digits and its digits are from [1, 2, 3, 4, 5]
def isValidProposal(number: int) -> bool:
    return len(str(number)) == 3 and all(1 <= int(digit) <= 5 for digit in str(number))

# get the digit in the 100s place of a number
def triangle(number: int) -> int:
    return (number // 100) % 10

# get the digit in the 10s place of a number
def square(number: int) -> int:
    return (number // 10) % 10

# get the digit in the 1s place of a number
def circle(number: int) -> int:
    return number % 10

# check if a digit is even
def isEven(number: int) -> bool:
    return number % 2 == 0

# check if a number contains a digit exactly times
def containsExactly(number: int, digit: int, times: int) -> bool:
    return str(number).count(str(digit)) == times

# count number of even digits in a number
def countEvenDigits(number: int) -> int:
    return sum(1 for digit in str(number) if isEven(int(digit)))

# count number of odd digits in a number
def countOddDigits(number: int) -> int:
    return sum(1 for digit in str(number) if not isEven(int(digit)))

# get sum of all digits in a number
def sumDigits(number: int) -> int:
    return sum(int(digit) for digit in str(number))

# check if a number is a triple number
# a triple number is a number that has exactly 3 digits and all digits are the same
def isTripleNumber(number: int) -> bool:
    return len(str(number)) == 3 and all(digit == str(number)[0] for digit in str(number))

# check if a number is a double number
# a double number is a number that has exactly 2 same digits and 1 different digit
def isDoubleNumber(number: int) -> bool:
    return len(str(number)) == 3 and any(str(number).count(digit) == 2 for digit in str(number))

# check if a number's digits are in ascending order
def isAscending(number: int) -> bool:
    return all(int(str(number)[i]) < int(str(number)[i + 1]) for i in range(len(str(number)) - 1))

# check if a number's digits are in descending order
def isDescending(number: int) -> bool:
    return all(int(str(number)[i]) > int(str(number)[i + 1]) for i in range(len(str(number)) - 1))

# check if a number's digits are in ascending sequence
def isAscendingSequence(number: int) -> bool:
    return all(int(str(number)[i]) + 1 == int(str(number)[i + 1]) for i in range(len(str(number)) - 1))

# check if 2 digits of a number are in ascending sequence
def isAscendingSequence2(number: int) -> bool:
    return not isAscendingSequence(number) and any(int(str(number)[i]) + 1 == int(str(number)[i + 1]) for i in range(len(str(number)) - 1))

# check if a number's digits are in descending sequence
def isDescendingSequence(number: int) -> bool:
    return all(int(str(number)[i]) - 1 == int(str(number)[i + 1]) for i in range(len(str(number)) - 1))

# check if 2 digits of a number are in descending sequence
def isDescendingSequence2(number: int) -> bool:
    return not isDescendingSequence(number) and any(int(str(number)[i]) - 1 == int(str(number)[i + 1]) for i in range(len(str(number)) - 1))

# check if a number is a multiple of another number
def isMultiple(number: int, multiple: int) -> bool:
    return number % multiple == 0