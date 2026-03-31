class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["neet","code","love","you"]
        # "4#neet4#code4#love4#you"

        s = ""
        for string in strs:
            s += str(len(string)) + "#" + string
        return s

    def decode(self, s: str) -> List[str]:
        # "4#neet4#code4#love4#you"
        # ["neet","code","love","you"]

        #2#we3#say1#:3#yes10#!@#$%^&*()

        l = []
        i=0
        while i < len(s):
            n = ""
            while s[i] != "#":
                n += s[i] 
                i+=1
                
            wordlen = int(n)
            print(wordlen)
            l.append(s[i+1 : i+1+wordlen])
            i = i+1+wordlen
        return l

        
