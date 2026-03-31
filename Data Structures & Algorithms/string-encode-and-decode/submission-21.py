class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

        # ["neet","code","love","you"]
        # "4#neet4#code4#love3#you"]


    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        while i < len(s):
            j = i
            # find the index of '#'
            while s[j] != "#":
                j += 1
            length = int(s[i:j])   # convert the number between i and j into an integer
            word = s[j+1 : j+1+length]
            res.append(word)
            i = j + 1 + length     # move i to start of next encoded string

        return res
            