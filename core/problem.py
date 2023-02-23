from core.verifier import Verifier

class Fact:
    def __init__(self, verifier: Verifier, correctCriterionId: int) -> None:
        self.verifier = verifier
        self.correctCriterionId = correctCriterionId

    def verify(self, number: int) -> bool:
        return self.verifier.verify(self.correctCriterionId, number)

class Problem:
    def __init__(self, facts: dict) -> None:
        self.facts = facts
        self.questionCount = 0
        self.history = []

    # check if a number satisfies all facts
    def isSolution(self, number: int) -> bool:
        return all(fact.verify(number) for fact in self.facts.values())

    # check if a number satisfies a specific verifier
    def check(self, number: int, verifierName: str) -> bool:
        self.questionCount += 1
        result =  self.facts[verifierName].verify(number)
        self.history.append((number, verifierName, result))
        return result

    # reset the question count
    def reset(self) -> None:
        self.questionCount = 0
        self.history = []