def solution_1017(nums):
    return True if nums == nums[::-1] else False
nums = 'abbad'
print(solution_1017(nums))
