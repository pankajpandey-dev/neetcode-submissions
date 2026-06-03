class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort_s ="".join(sorted(s))
        sort_t = "".join(sorted(t))

        if sort_t == sort_s:
            return True

        return False