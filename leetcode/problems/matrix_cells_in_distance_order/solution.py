class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        distances_to_center = {}
        for i in range(rows):
            for j in range(cols):
                distances_to_center[(i,j)] = abs(i-rCenter) + abs(j-cCenter)
        sorted_distances_to_center_list = [list(entry) for entry in dict(sorted(distances_to_center.items(), key=lambda item: item[1]))]
        
        return sorted_distances_to_center_list