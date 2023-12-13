file = open('input.txt', 'r')
lines = file.readlines()

count = 0

for line in lines:
    nums = []
    for char in line:
        if char.isdigit():
            nums.append(int(char))
    if len(nums) != 0:
        value = int(str(nums[0]) + str(nums[-1]))
        count += value

print(count)