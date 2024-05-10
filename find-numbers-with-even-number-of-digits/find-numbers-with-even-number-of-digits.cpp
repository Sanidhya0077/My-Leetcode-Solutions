class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int digit_count = 0;
        int even_number_count = 0;
        int digit = 0;
        
        for (int i = 0; i < nums.size(); i++)
        {
            while (nums[i] != 0)
            {
              nums[i] = nums[i]/10;
              digit_count++;
            }
            if (digit_count % 2 == 0)
            {
                cout << digit_count;
                even_number_count++;
            }
            digit_count = 0;
        }
        
        return even_number_count;
    }
};