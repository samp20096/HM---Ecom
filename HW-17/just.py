class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        return len(words[-1])
solution = Solution()

word: str = input("Words: ")

print(f"The length of the last word is: {solution.lengthOfLastWord(word)}")