class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        for elm in s:
            if elm != "]":
                stack.append(elm)
            else:
                subS = ""
                while stack[-1] != "[":
                    subS = stack.pop() + subS
                stack.pop() # get ride of the [
                
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
               
                stack.append(int(k) * subS)
        
       
        return "".join(stack)


    




        