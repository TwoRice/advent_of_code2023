import numpy as np

def extrapolate_trend(trend):
    diffs = np.diff(trend)
    if all(diffs == 0):
        return trend[-1]
    return trend[-1] + extrapolate_trend(diffs)

if __name__ == "__main__":
    with open("day9.txt", "r") as f:
        stability_values = [[int(x) for x in values.split()] for values in f.read().split("\n")]

    sum_extrapolated_values = 0
    for value_trend in stability_values:
        sum_extrapolated_values += extrapolate_trend(value_trend)
    print(f"Part 1: {sum_extrapolated_values}")

    sum_extrapolated_values = 0
    for value_trend in stability_values:
        sum_extrapolated_values += extrapolate_trend(value_trend[::-1])
    print(f"Part 2: {sum_extrapolated_values}")