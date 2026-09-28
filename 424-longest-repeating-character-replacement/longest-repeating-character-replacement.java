class Solution {
    public int characterReplacement(String s, int k) {
        int[] count = new int[26];
        int start = 0;
        int maxFreq = 0;
        int maxLength = 0;
        for(int end = 0; end < s.length(); end++){
            int charIdx = s.charAt(end) - 'A';
            count[charIdx]++;
            maxFreq = Math.max(maxFreq, count[charIdx]);
            if((end - start + 1) - maxFreq > k) {
                int startCharIdx = s.charAt(start) - 'A';
                count[startCharIdx]--;    
                start++;     
            }
            maxLength = Math.max(maxLength, end - start + 1);
        }
        return maxLength;
    }
}