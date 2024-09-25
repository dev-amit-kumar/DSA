class StockSpanner:

    def __init__(self):
        self.stock = []

    def next(self, price: int) -> int:
        self.stock.append(price)
        for i in range(len(self.stock) - 2, -1, -1):
            if self.stock[i] > price:
                return len(self.stock) - 1 - i
        return len(self.stock)