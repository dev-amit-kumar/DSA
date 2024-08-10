class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        player_counts = [{} for _ in range(n)]
        for xi, yi in pick:
            if yi not in player_counts[xi]:
                player_counts[xi][yi] = 0
            player_counts[xi][yi] += 1
        win_count = 0
        for i in range(n):
            if any(count >= i + 1 for count in player_counts[i].values()):
                win_count += 1
        return win_count