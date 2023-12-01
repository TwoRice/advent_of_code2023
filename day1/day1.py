import re

if __name__ == "__main__":
    with open("day1.txt", "r") as f:
        document = f.readlines()

    calibration_sum = 0
    for line in document:
        nums = [char for char in line if char.isdigit()]
        calibration_sum += int(nums[0] + nums[-1])
    print(f" Part 1: {calibration_sum}")

    calibration_sum = 0
    numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    search = "one|two|three|four|five|six|seven|eight|nine"
    number_search = re.compile(r"\d|" + search)
    reverse_number_search = re.compile(r"\d|" + search[::-1])
    for line in document:
        first = re.findall(number_search, line)[0]
        last = re.findall(reverse_number_search, line[::-1])[0][::-1]
        calibration_sum += int(numbers.get(first, first) + numbers.get(last, last))
    print(f"Part 2: {calibration_sum}")