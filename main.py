from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    numToIndex = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in numToIndex:
            return [numToIndex[complement], i]
        numToIndex[num] = i

    return []


if __name__ == "__main__":
    nums, target = [3, 3], 6
    print(twoSum(nums, target))
    