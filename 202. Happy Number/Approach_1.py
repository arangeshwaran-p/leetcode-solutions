class Solution:
    def next(self, n: int) -> int:
        total = 0
        while n > 0:
            d = n % 10
            total += d * d
            n //= 10
        return total

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n

        while True:
            slow = self.next(slow)
            fast = self.next(self.next(fast))

            if slow == 1:
                return True

            if slow == fast:
                return False