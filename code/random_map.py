from numpy import floor
from perlin_noise import PerlinNoise
import matplotlib.pyplot as plt


class RandomMap:
    def __init__(self):
        self.noise = PerlinNoise(octaves=4)

        self.amp = 2
        self.period = 8

        self.length = 15
        self.wight = 7

        self.landscale = [[0 for _ in range(self.length)] for _ in range(self.wight)]

        for x in range(self.wight):
            for z in range(self.length):

                y = floor(self.noise([x / self.period, z / self.period]) * self.amp)
                # print(f"x-{x}, z-{z}, y-{y}")
                self.landscale[int(x)][int(z)] = abs(int(y))

        self.pprint()

    def pprint(self):
        for y in range(self.wight):
            for x in range(self.length):
                item = self.landscale[y][x]
                if item == 1:
                    print(f"\033[31m{item}\033[0m", end="")
                else:
                    print(f"\033[32m{item}\033[0m", end="")
                print(" ", end="")
            print()


RandomMap()
