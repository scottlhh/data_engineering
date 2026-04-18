# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        i, j = 0, 0
        while i < len(list1) or j < len(list2):
            if i == len(list1):
                res.append(list2[j])
                j += 1
            elif j== len(list2):
                res.append(list1[i])
                i+=1
            elif list1[i] < list2[j]:
                res.append(list1[i])
                i+=1
            else:
                res.append(list2[j])
                j += 1
        return res

if __name__ == '__main__':
    sol = Solution()

    list1 = [1,2,4]
    list2 = [1,3,4]
    res = sol.mergeTwoLists(list1, list2)
    print(res)
    assert res == [1,1,2,3,4,4]

    list1 = []
    list2 = []
    res = sol.mergeTwoLists(list1, list2)
    print(res)
    assert res == []

    list1 = []
    list2 = [0]
    res = sol.mergeTwoLists(list1, list2)
    print(res)
    assert res == [0]

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
# Example 2:
#
# Input: list1 = [], list2 = []
# Output: []
#
# Example 3:
#
# Input: list1 = [], list2 = [0]
# Output: [0]
#
