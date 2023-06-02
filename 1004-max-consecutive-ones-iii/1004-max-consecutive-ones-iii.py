from collections import deque
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        window = deque()
        counter = 0
        maxWindow = 0
        for num in nums:
            # print(window, num, maxWindow)
            if num == 1:
                window.append(num)
                maxWindow = max(maxWindow,len(window))
            elif num == 0 and counter < k:
                window.append(num)
                counter +=1
                maxWindow = max(maxWindow,len(window))
            elif num == 0 and counter == k:
                window.append(num)
                counter += 1
                while counter > k:
                    if window[0] == 1:
                        window.popleft()
                    else:
                        window.popleft()
                        counter -=1
        return maxWindow
                    