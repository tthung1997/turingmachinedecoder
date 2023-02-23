from core.problem import Problem
from core.utils import isValidProposal

class Decoder:
    def __init__(self) -> None:
        pass

    def reset(self, problem: Problem) -> None:
        self.questionCount = 0
        self.history = []
        self.pool = [num for num in range(111, 556) if isValidProposal(num)]
        self.verifiers = problem.getVerifiers()
        for key in self.verifiers.keys():
            self.verifiers[key] = (self.verifiers[key], [i for i in range(len(self.verifiers[key].criterions))])

    def decode(self, problem: Problem) -> int:
        self.reset(problem)
        while True:
            self.newRound()
            if len(self.pool) == 1:
                return self.pool[0]
            elif len(self.pool) == 0:
                return -1

    def newRound(self) -> None:
        pass