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

        self.map_draft = [[0 for _ in range(self.length)] for _ in range(self.wight)]  # fill self.map with 0
        self.map = [[0 for _ in range(self.length + 2)] for _ in range(self.wight + 2)]

        self.map_fill()
        self.pprint(self.map_draft)
        print(self.map_draft)
        print("====self.map_draft printed====")

        self.map_formatting()
        # print(self.map)
        self.pprint(self.map)

    def map_fill(self):
        """Filling with numbers using Perlin noise"""

        for x in range(self.wight):
            for z in range(self.length):
                y = abs(int(floor(self.noise([x / self.period, z / self.period]) * self.amp)))
                # print(f"x-{x}, z-{z}, y-{y}")
                self.map_draft[int(x)][int(z)] = int(y > self.amp // 4)
        """
        self.amp // 2: because of abs. i dont want to use negative numbers
        self.amp // 4: because we taking the middle value
        y > self.amp // 4: if noise value more than middle value than 1 else 0
        1 is rock
        0 is floor
        """

    def map_formatting(self):
        for y in range(self.wight + 2):
            for x in range(self.length + 2):
                print(x, self.length, self.length + 2)
                if x == 0 or y == 0 or x == self.length + 2 - 1 or y == self.wight - 1:
                    self.map[y][x] = "w"
                    # print(1)
                elif x == 1 or y == 1 or x == self.length - 2 or y == self.wight - 2:
                    self.map[y][x] = "g"
                    # print(2)
                else:
                    self.map[y][x] = "r" if self.map_draft[y - 2][x - 2] else "g"
                    # print(3)

    def pprint(self, map):
        """Colored printing self.map for easy analyzing"""
        for y in range(len(map) - 2):
            for x in range(len(map[y]) - 2):
                item = map[y][x]
                # print(item)
                if item in ("r", 1):  # rock
                    color = "31"
                elif item in ("w",):  # wall
                    color = "32"
                elif item in ("g", 0):  # ground
                    color = "33"
                else:
                    color = "34"
                print(f"\033[{color}m{item}\033[0m", end="")  # colored print
                print(" ", end="")
            print()


RandomMap()
