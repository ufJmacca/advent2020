#%%
import requests
import secrets
import numpy

#%%
header = {'cookie': secrets.cookie}

map_start = requests.get('https://adventofcode.com/2020/day/3/input', headers = header)
# %%
map_list = map_start.text.split('\n')

map_array = [[char for char in i] for i in map_list if len(i) > 0]
print(map_array[0])

mod = len(map_array[0])
print(mod)
# %%
# Part 1
x = -3
y = 0

offset_x = 3
offset_y = 1

trees = 0

for idx, y_level in enumerate(map_array):
    print(y_level[(x + offset_x) % mod])
    if y_level[(x + offset_x) % mod] == '#':
        trees += 1
    x += offset_x

print(trees)
# %%
# Part 2
slopes = [
    [1,1],
    [3,1],
    [5,1],
    [7,1],
    [1,2]
]

trees = []

total_levels = len(map_array)

for slope in slopes:
    x = slope[0] * -1
    y = slope[1] * -1

    offset_x = slope[0]
    offset_y = slope[1]

    trees_on_slope = 0

    while y + offset_y < total_levels:
        if map_array[y + offset_y][(x + offset_x) % mod] == '#':
            trees_on_slope += 1
        y += offset_y
        x += offset_x

    trees.append(trees_on_slope)

print(trees)
print(numpy.prod(trees))
# %%
