class Solution {
    public int countOdds(int low, int high) {
        int count;
        if(low%2 != 0 && high%2 == 0)
        {
            count = high/2 - (low+1)/2 + 1;
        }
        else if(low%2 != 0 && high%2!=0)
        {
            count = (high+1)/2 - (low+1)/2 + 1;
        }
        else if(low%2 == 0 && high%2!=0)
        {
            count = (high+1)/2 - (low)/2;
        }
        else
        {
            count = (high-low)/2;
        }
    return count;
    }
}
