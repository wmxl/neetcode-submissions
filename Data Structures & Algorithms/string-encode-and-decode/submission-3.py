from typing import List, Optional, Dict, Tuple
from collections import defaultdict, Counter, deque
import heapq
import math
from functools import lru_cache, cmp_to_key
import bisect
from itertools import permutations, combinations, product, accumulate

class Solution:

    def encode(self, strs: List[str]) -> str:
        sep = chr(0)
        parts = []
        for s in strs:
            parts.append(s)
            parts.append(sep)
        return "".join(parts)


    def decode(self, s: str) -> List[str]:
        sep = chr(0)
        res = []
        word = ""
        for c in s:
            if c == sep:
                res.append(word)
                word = ""
                continue
            word += c
        return res
