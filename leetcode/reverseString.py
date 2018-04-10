class Solution:
    def reverseStringPythonic(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

    def reverseStringRecursive(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<2:
            return s
        return self.reverseString(s[len(s)//2:]) + self.reverseString(s[:len(s)//2])

    def reverseStringImperative(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        i=0
        while(i<len(s)//2):
            s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
            i += 1
        return "".join(s)
        