class Solution:

    def encode(self, strs: List[str]) -> str:

        if not strs:
            return ""
        
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + ":" + word  # Prefix each word with its length and a colon
            
        return encoded


    def decode(self, s: str) -> List[str]:

        if not s:
            return []
        
        res = []
        i = 0
        while i < len(s):
            j = s.find(":", i)  # Find the separator
            length = int(s[i:j])  # Extract length
            i = j + 1  # Move past the colon
            res.append(s[i:i+length])  # Extract the word
            i += length  # Move to the next word
        
        return res
        
