class Power:
    def __init__(self, x, n):
        self.x = x
        self.n = n
    def pow(self):
        if self.n == 0:
            return 1
        elif self.n < 0:
            return 1 / self.pow(self.x, -self.n)
        else:
            result = 1
            while self.n > 0:
                if self.n % 2 == 1:
                    result *= self.x
                self.x *= self.x
                self.n //= 2
            return result