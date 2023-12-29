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
    def __init__(self, length: int = 15, wight: int = 7, octaves: float = 2, amp: int = 4, period: int = 3) -> None:
        """
            :parameter int length: Length of map
            :parameter int wight: Wight of map
            :parameter float octaves: Это количество кривых Перлина, которые отвечают за неоднородность шума. Чем больше этот параметр, тем «необычней» ландшафт по своей форме
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
                y = abs(int(floor(self.noise([x / self.period, z / self.period]) * self.amp)))
                # print(f"x-{x}, z-{z}, y-{y}")
                self.map[int(x)][int(z)] = int(y > self.amp // 4)
        """
        self.amp // 2: because of abs. i dont want to use negative numbers
        self.amp // 4: because we taking the middle value
        y > self.amp // 4: if noise value more than middle value than 1 else 0
        1 is rock
        0 is floor
        """

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
