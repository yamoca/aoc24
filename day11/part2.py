data = "70949 6183 4 3825336 613971 0 15 182"
data = [int(x) for x in data.split()]
from functools import lru_cache

# just adduing lru_cache on my part1 code didnt work (cause func was called with the complete list, so changed every time, therefore cache didnt help
# solution instead of calling func on whole list, call func on individual stone
# help from u/StaticMoose to get recursion properly
# key words for further reading "memoization"

@lru_cache(maxsize=None)
def blink_one_stone(stone):
    if stone == 0:
        return(1, None)
    elif len(str(stone)) % 2 == 0:
        first_half = str(stone)[:len(str(stone))//2] # floor division to remain as int e.g 4/2=2.0 
        second_half = str(stone)[len(str(stone))//2:]
        return (int(first_half), int(second_half))
    else:
        return (stone * 2024, None)

@lru_cache(maxsize=None)
def collect_num_of_stones_from_stone(stone, num_of_blinks):
    print(num_of_blinks) 
    first_stone, second_stone = blink_one_stone(stone)

    if num_of_blinks == 1:
        if second_stone == None:
            return 1
        else:
            return 2
    else:
        output = collect_num_of_stones_from_stone(first_stone, num_of_blinks - 1) 
        if second_stone != None:
            output += collect_num_of_stones_from_stone(second_stone, num_of_blinks - 1)
        
        return output

    
result = 0  
for stone in data:
    result += collect_num_of_stones_from_stone(stone, 75)

print(result)

# def blink(data):
#     nextline = []
#     for i in range(len(data)):
#         if data[i] == 0:
#             nextline.append(1)
#         elif len(str(data[i])) % 2 == 0:
#             first_half = str(data[i])[:len(str(data[i]))//2] # floor division to remain as int e.g 4/2=2.0 
#             second_half = str(data[i])[len(str(data[i]))//2:]
#             nextline.append(int(first_half))
#             nextline.append(int(second_half))
#         else:
#             nextline.append(data[i]*2024)
    
#     return nextline
    

# print("initial")
# print(data)
# desired_blinks = 25 

# for i in range(1, desired_blinks+1):# +1 because range is exclusive
#     print(i, "blinks")
#     data = blink(data) 
#     # print(data)


# print("# stones after", desired_blinks, "blinks")
# print(len(data))