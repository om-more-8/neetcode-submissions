class Solution {
public:
    int reverse(int x) {
        string str = to_string(x);

        int left =0;
        int right = str.length()-1;

        if(str[0] == '-') left ++;

        while(left<right){
            swap(str[left], str[right]);
            left++;
            right --;
        }
        
        long long ans = (long long)stoll(str);
        
        if(ans >= INT_MIN && ans <= INT_MAX){
            return ans;
        }
    return 0;

    }
};
