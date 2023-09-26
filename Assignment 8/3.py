import itertools


class Subsets:
    def __init__(self, set):
        self.set = set
    def get_subsets(self):
        subsets = [[]]
        for i in range(1, len(self.set) + 1):
            combinations = itertools.combinations(self.set, i)
            subsets.extend(list(combinations))
        return subsets