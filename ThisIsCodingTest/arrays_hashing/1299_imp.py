class  Solution:
    def replaceElements(self, arr: List[int])->List[int]:
        
        # initial max = -1
        # reverse iteration to reach time complexity of O(n)
        # new max = max(old_max, arr[i])
        
        # reversly start at -1 which will always be true
        rightMax = -1
        
        for i in range(len(arr)-1, -1, -1):
            # reversly compare
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr