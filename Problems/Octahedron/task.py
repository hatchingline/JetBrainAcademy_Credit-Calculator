import math


edge_a = int(input())
area = round(2 * math.sqrt(3) * edge_a ** 2, 2)
volume = round(1 / 3 * math.sqrt(2) * edge_a ** 3, 2)
print('{} {}'.format(area, volume))
