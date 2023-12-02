def BruteForce_TwoSum(nums,target):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return([i,j])
my_list = [2,3,5,6,7]
target  = 9
print(BruteForce_TwoSum(my_list, target))


def Dictionary_TwoSum(nums,target):
    seen={}

    for i, num in enumerate(nums):
        if target - num in seen:
            return(seen[target-num],i)
        elif num not in seen:
            seen[num] =i

my_list = [2,3,5,6,7]
target  = 9
print(Dictionary_TwoSum(my_list, target))
