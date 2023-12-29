# import preinstalled packages


# import not preinstalled packages
from numpy import floor
from perlin_noise import PerlinNoise

# import project files


class RandomMap:
    """
    Link with article about Perlin noise in python
    https://habr.com/ru/companies/selectel/articles/731506/
    """
    def __init__(self, length: int = 15, wight: int = 7, octaves: int = 4, amp: int = 1, period: int = 8) -> None:
        """
            :parameter int length: Length of map
            :parameter in wight: Wight of map
            :parameter int octaves: Это количество кривых Перлина, которые отвечают за неоднородность шума. Чем больше этот параметр, тем «необычней» ландшафт по своей форме
            :parameter int amp: Это коэффициент, который отвечает за итоговую высоту координаты y
            :parameter int period: Это периодичность пиков кривой Перлина. При ее увеличении поверхность становится более гладкой
            :return: None
        """

        self.noise = PerlinNoise(octaves=octaves)

        self.length = length
        self.wight = wight

        self.amp = amp
        self.period = period

        self.map = [[0 for _ in range(self.length)] for _ in range(self.wight)]  # fill self.map with 0
        self.map_fill()

        self.pprint()

    def map_fill(self):
        """Filling with numbers using Perlin noise"""

        for x in range(self.wight):
            for z in range(self.length):
                y = floor(self.noise([x / self.period, z / self.period]) * self.amp)
                # print(f"x-{x}, z-{z}, y-{y}")
                self.map[int(x)][int(z)] = abs(int(y))

    def pprint(self):
        """Colored printing self.map for easy analyzing"""
        for y in range(self.wight):
            for x in range(self.length):
                item = self.map[y][x]
                color = "31" if item == 1 else "32"
                print(f"\033[{color}m{item}\033[0m", end="")  # colored print
                print(" ", end="")
            print()


RandomMap()
