class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        if len(string) == 0:
            return 0
        longest_string = string[0]
        len_longest_string = 1
        longest = 1

        for i in string[1:]:
            if i not in longest_string:
                longest_string += i
                len_longest_string += 1
                if len_longest_string > longest:
                    longest = len_longest_string
            else:
                while i in longest_string:
                    longest_string = longest_string[1:]
                    len_longest_string -= 1
                longest_string += i  
                len_longest_string += 1
        return longest
