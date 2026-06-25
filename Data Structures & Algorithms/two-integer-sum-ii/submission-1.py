class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1, p2 = 0, len(numbers)-1
        while p1<p2:
            two_sum = numbers[p1]+numbers[p2]
            if two_sum == target:
                return [p1+1,p2+1]
            elif two_sum<target:
                p1+=1
            else:
                p2-=1
        