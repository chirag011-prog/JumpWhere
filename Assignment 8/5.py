class ThreeSum:
    def __init__(self, numbers):
        self.numbers = numbers
    def find_triplets(self):
        triplets = []
        for i in range(len(self.numbers)):
            for j in range(i + 1, len(self.numbers)):
                for k in range(j + 1, len(self.numbers)):
                    if self.numbers[i] + self.numbers[j] + self.numbers[k] == 0:
                        triplets.append([self.numbers[i], self.numbers[j], self.numbers[k]])
        return triplets