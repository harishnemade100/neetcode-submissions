class Solution:
    def isPathCrossing(self, path: str) -> bool:

        x = y = 0

        visited_point = {(0,0)}

        for move in path:
            if move == 'N':
                y+=1
            elif move == 'S':
                y-=1
            elif move == 'E':
                x+=1
            else:
                x-=1
            
            if (x,y) in visited_point:
                return True
                
            visited_point.add((x,y))

        return False
