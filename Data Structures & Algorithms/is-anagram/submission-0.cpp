class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()) return false;
        for(int i =0; i<t.size(); i++){
            
            int pos = s.find(t[i]);
            if(pos != string::npos) s.erase(pos, 1);
            else return false;
        
        }
        return s.empty();
    }
};
