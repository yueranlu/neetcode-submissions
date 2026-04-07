class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) -1
        s = s.lower()

        while l < r :
            while not ord("a") <= ord(s[l]) <= ord("z") and not ord("0") <= ord(s[l]) <= ord("9") and l < r:
                l += 1
                print()
            while not ord("a") <= ord(s[r]) <= ord("z") and not ord("0") <= ord(s[r]) <= ord("9")and r > l:
                r -= 1
            if s[l] != s[r]:
                return False
                break
            l += 1
            r -= 1
        return True