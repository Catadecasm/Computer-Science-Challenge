"""The time complexity of the code is O(n^2), where n is the length of the string s.
 This is because the code iterates through the string s, and each iteration takes linear time.
"""

"""The space complexity of the code is O(n), where n is the length of the string s.
 This is because the code only uses a linear amount of space to store the array and the lengthLongest variable.
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        array = list(s)
        lenghtLongest = -1

        for i in range(len(array)):
            count = 0
            for j in range(i, len(array)):
                element = 1
                if array[j] == '(':
                else:
                    -1
                count += element
                if count == 0:
                    if lenghtLongest < j - i:
                        lenghtLongest = j - i
                elif count < 0:
                    break

        return lenghtLongest + 1
        
       
