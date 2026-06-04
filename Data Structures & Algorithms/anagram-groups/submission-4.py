from collections import defaultdict
from typing import List  # Ensure List is imported if needed

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Bug fix: pass 'list' as the default factory
        anagram_map = defaultdict(list)

        for i in strs:
            sorted_key = "".join(sorted(i))
            anagram_map[sorted_key].append(i)

        return list(anagram_map.values())
