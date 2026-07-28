class Solution:
    def isPathCrossing(self, path: str) -> bool:

        x = y = 0

        visited_point = [(0,0)]

        for move in path:
            if move == 'N':
                y+=1
            elif move == 'S':
                y-=1
            elif move == 'E':
                x+=1
            else:
                x-=1
            
            for position in visited_point:
                if position[0] == x and position[1] == y:
                    return True
                
            visited_point.append((x,y))

        return False
