from numpy import floor
from perlin_noise import PerlinNoise
import time


class RandomMap:
    def __init__(self):
        self.noise = PerlinNoise(octaves=4)

        self.amp = 2
        self.period = 8

        self.length = 15
        self.wight = 7

        self.map = [[0 for _ in range(self.length)] for _ in range(self.wight)]
        self.map_fill()

        self.pprint()

    def map_fill(self):
        for x in range(self.wight):
            for z in range(self.length):
                y = floor(self.noise([x / self.period, z / self.period]) * self.amp)
                # print(f"x-{x}, z-{z}, y-{y}")
                self.map[int(x)][int(z)] = abs(int(y))

    def pprint(self):
        for y in range(self.wight):
            for x in range(self.length):
                item = self.map[y][x]
                if item == 1:
                    print(f"\033[31m{item}\033[0m", end="")
                else:
                    print(f"\033[32m{item}\033[0m", end="")
                print(" ", end="")
            print()


RandomMap()
