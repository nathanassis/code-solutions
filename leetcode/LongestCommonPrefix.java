package leetcode;

public final class LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
        String res = new String();
        for (int i = 0; i < strs[0].length(); i++) {
            char newChar = strs[0].charAt(i);
            try {
                for (String str : strs) {
                    if (str.charAt(i) != newChar) {
                        return res;
                    }
                }
            } catch (Exception e) {
                return res;
            }
            res += newChar;
        }

        return res;
    }
}
