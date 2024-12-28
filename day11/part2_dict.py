# dictionary method 
# help from SubNet32 on github

data = "70949 6183 4 3825336 613971 0 15 182"
data = [int(x) for x in data.split()]
from functools import lru_cache

# map stones: count e.g
# 1 2024 1 0 1 becomes
# 1: 3, 2024: 1, 0: 1

dictionary = {}

def add_to_dict(dictionary, stone, count):
    if stone in list(dictionary):
        dictionary[stone] += count 
    else:
        dictionary[stone] = count 


# initialise dictionary
for value in data:
    add_to_dict(dictionary, value, 1)

print("initial")
print(dictionary)


desired_blinks = 75 
for i in range(1, desired_blinks+1):
    print("step", i)
    newStones = {}
    for stone in list(dictionary):
        if stone == 0:
            add_to_dict(newStones, 1, dictionary[stone])
        elif len(str(stone)) % 2 == 0:
            first_half = str(stone)[:len(str(stone))//2] # floor division to remain as int e.g 4/2=2.0 
            second_half = str(stone)[len(str(stone))//2:]
            add_to_dict(newStones, int(first_half), dictionary[stone])
            add_to_dict(newStones, int(second_half), dictionary[stone])
        else:
            add_to_dict(newStones, stone * 2024, dictionary[stone])

    dictionary = newStones 
    





print("# stones after", desired_blinks, "blinks")
total = 0
for key in dictionary.keys():
    total += dictionary[key]

print(total)