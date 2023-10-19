def jump1(nums):
    run = True
    i = 0
    finish = len(nums)
    while (run):
        if (nums[i] == 0):
            print(
                f"False: Jump failed to advance at index {i} with jump length {nums[i]}")
            return False
        elif (nums[i] + i >= finish - 1):
            print(
                f"True: Jump reached finish {finish} at index {i} with jump length {nums[i]}")
            return True
        i += 1


nums = [2, 3, 1, 1, 4]
jump1(nums)
