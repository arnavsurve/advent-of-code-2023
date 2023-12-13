import re

file = open('input.txt', 'r')
lines = file.readlines()


def get_digit(d):
    if d.isnumeric():
        return d
    else:
        return digits.index(d)

digits = ('', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
regex = r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))'

count = 0
for line in lines:
    nums = re.findall(regex, line)
    count += int(str(get_digit(nums[0])) + str(get_digit(nums[-1])))

print(count)
