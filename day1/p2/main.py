import re

file = open('example.txt', 'r')
lines = file.readlines()

count = 0

def replace_number_word(match):
    number_words = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    return number_words[match.group(0)]



for line in lines:
    line = re.sub(r'\b(?:zero|one|two|three|four|five|six|seven|eight|nine)\b', replace_number_word, line)
    print(line)
    nums = []
    for char in line:
        if char.isdigit():
            nums.append(int(char))
    if len(nums) != 0:
        value = int(str(nums[0]) + str(nums[-1]))
        count += value

print(count)