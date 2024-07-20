class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        curr_turn = "Alice"
        last_turn = "Bob"
        total = 0
        while(True):
            if (total == 115):
                total = 0
                if (curr_turn == "Bob"):
                    last_turn = "Bob"
                    curr_turn = "Alice"
                else:
                    last_turn = "Alice"
                    curr_turn = "Bob"
            else:
                if (total == 0 and x > 0):
                    total += 75
                    x -= 1
                    continue
                elif (total >= 75 and y > 0):
                    total += 10
                    y -= 1
                else:
                    return last_turn
                    