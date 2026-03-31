class Solution:

    def encode(self, strs: List[str]) -> str:
        #["we","say",":","yes","!@#$%^&*()"]
        encoded = ""
        for s in strs:
            encoded = encoded + str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
    
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = s[i:j]
            j += 1
            decoded.append(s[j:j+int(length)])
            i = j + int(length)
        return decoded
