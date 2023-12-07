# There is two way for solution

# First of all brute force technique

class Solution(object):
    def addTwoNumbers(self, l1, l2):
       # ListNode(l1)
       # ListNode(l2)
       l1_str=''
       l2_str=''
       for i in l1:
           l1_str = l1_str+str(i)
       for i in l2:
           l2_str = l2_str+str(i)
       l1_str = l1_str[::-1] # reverse l1_str
       l2_str = l2_str[::-1] # reverse l2_str
       result = str(int(l1_str)+int(l2_str))[::-1] # Type Casting --> Int, Sum l1_str+l2_str, Reverse result
       res = [int(x) for x in str(result)] # Add To list
       return res

# Second one, Clean way.

# We don't use reverse function at this solution. Because, we'r gonna add theese two listnode with simple way. 

# l1 [2,4,3] l2 = [5,6,4]
#  2 4 3
#  5 6 4
# +
#--------
# 7 0 8

# 2+5=7, 4+6=10 but we can't write 10, we need to write 0, 3+4=7 but we are given +1 because previous operation = 10.
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1=l1.val
                l1=l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next= ListNode(val)
            n=n.next
        return root.next
