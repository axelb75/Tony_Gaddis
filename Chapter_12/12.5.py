def calc_sum(nums, start, end):
    sum = 0
    if start <= end:
        sum = nums[start] + calc_sum(nums, start + 1, end)
        return sum
    else:
        return 0


num_list = [1, 2, 11, 5, 22, 9, 4, 10, 6]
sum = calc_sum(num_list, 0, len(num_list) - 1)
print('Сумма чисел:', sum)