class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st = list(s)
        tt = list(t)
        st.sort()
        tt.sort()
      
        return st == tt