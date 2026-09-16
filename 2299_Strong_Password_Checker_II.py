# Leetcode 2299 : Strong Password Checker II
# Difficulty : Easy

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        if not any(c.isupper() for c in password):
            return False
        if not any(c.islower() for c in password):
            return False
        if not any(c.isdigit() for c in password):
            return False
        if not any(c in "!@#$%^&*()-+" for c in password):
            return False
        for i in range(len(password)-1):
            if password[i]==password[i+1]:
                return False
        return True