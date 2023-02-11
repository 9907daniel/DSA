class Solution:
    def isValid(self, s: str) -> bool:

        l = []

        for a in s:
            if a=='(' or a=='{' or a=='[':
                l.append(a)
                print(a)
            elif len(l) >= 1:
                if (a==')' and l[-1]=='(' or 
                   a==']' and l[-1]=='[' or
                   a=='}' and l[-1]=='{'):
                    l.pop(-1)
                else:
                    return False
            else:
                return False
        if l == []:
            return True
        else:
            return False
                

        