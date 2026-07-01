class StockSpanner(object):

    def __init__(self):
        self.stack = []   # (price, index)
        self.idx = -1

    def next(self, price):
        self.idx += 1

        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()

        if not self.stack:
            span = self.idx + 1
        else:
            span = self.idx - self.stack[-1][1]

        self.stack.append((price, self.idx))

        return span