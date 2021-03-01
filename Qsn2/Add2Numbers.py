# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        current = ListNode(0)
        temp = current
        carry = 0
        
        while l1 != None or l2 != None:
            
            x,y = 0,0
            
            if(l1):
                x = l1.val
                l1 = l1.next
                
            if(l2):
                y = l2.val
                l2 = l2.next
                
            sum = carry + x + y
            carry = sum // 10
            
            current.next = ListNode(sum%10)
            current = current.next
    
        if(carry):
            current.next = ListNode(carry)      
        
        return temp.next
