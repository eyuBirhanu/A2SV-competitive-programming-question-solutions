# Problem: Asteroid Collision - https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def sign(x):
            return (x > 0) - (x < 0)

        rest = []
        for a in asteroids:
            if not rest:
                rest.append(a)
                continue
            rest.append(a)
            if (rest[-2] < 0 and rest[-1] < 0) or (rest[-2] and rest[-1] > 0):
                continue
            else:
                while len(rest) >= 2 and (sign(rest[-1]) == -1 and sign(rest[-2]) == 1):
                    if abs(rest[-1]) == abs(rest[-2]):
                            rest.pop()
                            rest.pop()
                    else:
                        val_1, val_2 = [-1,rest[-1]], [-2, rest[-2]]
                        lesser = 0
                        if abs(val_1[1]) < abs(val_2[1]):
                            lesser = val_1
                        else:
                            lesser = val_2
                        rest.pop(lesser[0])
        return rest
                            