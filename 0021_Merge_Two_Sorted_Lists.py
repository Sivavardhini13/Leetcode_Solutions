# LeetCode 21: Merge Two Sorted Lists
# Difficulty: Easy
# Approach: Recursion
# Time Complexity: O(m + n)
# Space Complexity: O(m + n)  # Recursion stack

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2