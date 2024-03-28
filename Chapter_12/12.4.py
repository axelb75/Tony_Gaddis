def calc_max(nums, start, end):
    if end > start:
        if nums[start] > nums[start +1]:
            del nums[start + 1]
        else:
            del nums[start]
        calc_max(nums, start, end - 1)


num_list = [1, 2, 7, 4, 5, 3, 2, 4, 1]
calc_max(num_list, 0, len(num_list) - 1)
print(num_list[0])