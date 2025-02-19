package leetcode;

public class PalindromeNumber {
    public boolean isPalindrome(int x) {
        String strNumber = Integer.toString(x);
        int len = strNumber.length();

        for (int i = 0; i < len / 2; i++) {
            if (strNumber.charAt(i) != strNumber.charAt(len - 1 - i)) {
                return false;
            }
        }

        return true;
    }
}
