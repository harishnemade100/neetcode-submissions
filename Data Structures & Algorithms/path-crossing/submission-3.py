class Solution:
    def isPathCrossing(self, path: str) -> bool:

        x = y = 0
        visited = [(0, 0)]

        for move in path:

            if move == 'N':
                y += 1
            elif move == 'S':
                y -= 1
            elif move == 'E':
                x += 1
            else:
                x -= 1

            # Brute-force search
            for position in visited:
                if position[0] == x and position[1] == y:
                    return True

            visited.append((x, y))

        return False