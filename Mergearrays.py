"""The time complexity of the code is O(n + m), where n is the length of nums1 and m is the length of nums2.
 This is because the code iterates through both nums1 and nums2, and each iteration takes constant time.
"""

"""The space complexity of the code is O(1), where n is the length of nums1 + m is the length of nums2.
 This is because the code only uses a constant amount of space to store the totalArray and result arrays.
"""



class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        totalArray = [0] * 1001
        count = len(nums1)
        
        for index, value in nums1:
            totalArray[index] = value
        
        for index, value in nums2:
            if totalArray[index] == 0:
                count += 1
            totalArray[index] += value
        
        result = [[0, 0] for _ in range(count)]
        count2 = 0
        
        for i in range(1, 1001):
            if totalArray[i] != 0:
                result[count2] = [i, totalArray[i]]
                count2 += 1
        
        return result
        

        
  