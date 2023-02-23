import random
from core.problem import Problem
from core.utils import isValidProposal

class Decoder:
    def __init__(self) -> None:
        pass

    def reset(self, problem: Problem) -> None:
        self.problem = problem
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
                if self.problem.isSolution(self.pool[0]):
                    return self.pool[0]
                else:
                    return -1
            elif len(self.pool) == 0:
                return -1

    def newRound(self) -> None:
        proposal, verifierKeys = self.getProposal()
        for key in verifierKeys:
            result = self.problem.check(proposal, key)
            print(f"Question {self.questionCount}: {proposal} is {result} for {key}")
            
            self.questionCount += 1
            self.history.append((proposal, key, result))
            self.updatePool(proposal, key, result)

    def getProposal(self):
        # get random number from self.pool using random.choice
        proposal = random.choice(self.pool)
        # select at most 3 verifiers from self.verifiers that has more than one criterion left to check
        verifierKeys = [key for key in self.verifiers.keys() if len(self.verifiers[key][1]) > 1]
        verifierKeys = random.sample(verifierKeys, min(3, len(verifierKeys)))
        return proposal, verifierKeys

    def updatePool(self, proposal: int, verifierKey: str, result: bool) -> None:
        verifier = self.verifiers[verifierKey]
        for i in range(len(verifier[0].criteria)):
            criterion = verifier[0].criteria[i]
            if proposal in criterion:
                if result:
                    self.pool = [num for num in self.pool if num in criterion]
                else:
                    self.pool = [num for num in self.pool if num not in criterion]
                    self.verifiers[verifierKey][1].remove(i)
            else:
                if result:
                    self.pool = [num for num in self.pool if num not in criterion]
                    self.verifiers[verifierKey][1].remove(i)
