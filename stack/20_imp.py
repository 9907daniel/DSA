class Solution:
    def isValid(self, s: str) -> bool:

        test_stack = []
        test_hash = {")":"(","]":"[","}":"{"}
        
        for c in s:
            if c in test_hash:
                if test_stack and test_stack[-1] == test_hash[c]:
                    stack.pop()
                else:
                    return False
            else:
                test_stack.append(c)
        
        return True if not test_stack else False




        # stack = []
        # # HashMap of all syntaxes
        # closeToOpen = {")":"(","]":"[","}":"{"}

        # # all characters in the string
        # for c in s:
        #     # check it is a closing tag (because keys are all closing tags)
        #     if c in closeToOpen:
        #         # if they match eachother
        #         if stack and stack[-1] == closeToOpen[c]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(c)
        # return True if not stack else False