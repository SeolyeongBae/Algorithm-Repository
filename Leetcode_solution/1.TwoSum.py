def twoSum(nums, target):
    for i in range(len(nums)):
        temp = nums[::]
        temp[i] = 10000000000
        try:
            a = temp.index(target - nums[i])
        except ValueError:
            continue

        if a > 0:
            return [i, a]

#runtime : 1238ms, 상위 65%다. 여기서 더 개선할 수 있는 점 -> 답이 하나밖에 없으므로
'''
  checked = {}
        i = 0
        while target - nums[i] not in checked:
            checked[nums[i]] = i
            i += 1

        return [checked[target - nums[i]], i]
checked를 활용해서 한번 체크한 경우는 다시 확인하지 않는다 -> index 보다 더 낫다
'''


print(twoSum([0,4,3,0], 0))