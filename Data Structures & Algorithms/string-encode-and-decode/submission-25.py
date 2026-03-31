class Solution:

    def encode(self, strs: List[str]) -> str:
        #["we","say",":","yes","!@#$%^&*()"]
        encoded = ""
        for s in strs:
            encoded = encoded + str(len(s)) + "#" + s
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
    
        decoded = []
        i = 0
        while i < len(s):
            num = ""
            while s[i].isdigit():
                num += s[i]
                i += 1
            if s[i] == "#":
                decoded.append(s[i+1: i+1+int(num)])
            i = i+1+int(num)
        return decoded
