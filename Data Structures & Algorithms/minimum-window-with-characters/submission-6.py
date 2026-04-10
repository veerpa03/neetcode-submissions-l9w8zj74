class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = {}
        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1

        def all_zero(d):
            for v in d.values():
                if v > 0:
                    return False
            return True

        min_string = ""

        for i in range(len(s)):
            if s[i] not in count_t:
                continue
            count_t1 = count_t.copy()  

            for j in range(i, len(s)):
                if s[j] in count_t1:
                    count_t1[s[j]] -= 1 
                    length =j
                if all_zero(count_t1):
                    curr = s[i:length+1]   
                    if min_string == "" or len(curr) < len(min_string):
                        min_string = curr
                    break  

        return min_string
