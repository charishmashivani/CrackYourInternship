#Day 17

def missingNumber(self,arr, n):
        for i in range(n):
            while 1 <= arr[i] <= n and arr[i] != arr[arr[i] - 1]:
                correct_pos = arr[i] - 1
                arr[i], arr[correct_pos] = arr[correct_pos], arr[i]
    
        for i in range(n):
            if arr[i] != i + 1:
                return i + 1
    
        return n + 1
