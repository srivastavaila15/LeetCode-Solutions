class Solution(object):
    def smallestSubsequence(self, s):
        stack = []
        seen = set()
        last_occur = {char: i for i, char in enumerate(s)}

        for i, char in enumerate(s):
            if char not in seen:
                while stack and char < stack[-1] and i < last_occur[stack[-1]]:
                    seen.remove(stack.pop())
                
                stack.append(char)
                seen.add(char)
        return "".join(stack)

        