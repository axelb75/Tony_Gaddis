def calc_sum(nums, start, end):
    sum = 0
    if start <= end:
        sum = nums[start] + calc_sum(nums, start + 1, end)
    return sum


num_list = [1, 2, 7, 5, 23, 9, 4, 10]
sum = calc_sum(num_list, 0, len(num_list) - 1)
print(sum)