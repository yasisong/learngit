import numpy
class Solution():
    def containsDuplicate(self, nums: List[int]) -> bool:
        L = []
        for i in range(len(L)):
            val = L[i]
            if val not in L:
                  L.append(val)

        if len(L) != len(L):
            return True
        else:
            return False

if __name__ == '__main__':
    Solution s
    L = [1,2,3,4,1]
    s.cotainsDuplicate(L)