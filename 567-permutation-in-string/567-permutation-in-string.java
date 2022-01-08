class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int[] hash1 = new int[26];
        for (int i=0; i < s1.length(); i++)
            hash1[s1.charAt(i) - 'a']++;
        
        int[] hash2 = new int[26];
        int start = 0, end = 0;
        while (end < s2.length()) {
            if (end < s1.length()-1) {
                hash2[s2.charAt(end++) - 'a']++;
            } else if (end == s1.length()-1) {
                hash2[s2.charAt(end++) - 'a']++;
                if (Arrays.equals(hash1, hash2))
                    return true;
            } else {
                hash2[s2.charAt(end++) - 'a']++;
                hash2[s2.charAt(start++) - 'a']--;
                if (Arrays.equals(hash1, hash2))
                    return true;
            }
        }
        return false;
    }
}