nums = [1, 3, 5, 3, 1, 7, 5]
write_index = 0 # это для индексов он будет указывать на индексы вот не спутай 

for i in range(len(nums)):
    is_duplicate = False
    for j in range(i):
        if nums[j] == nums[i]:
            is_duplicate = True
            break
    if not is_duplicate:
        nums[write_index] = nums[i]
        write_index = write_index + 1

print(nums[:write_index])