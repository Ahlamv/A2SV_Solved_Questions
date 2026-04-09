class Solution:
    def removeComments(self, source):
        res = []
        inBlock = False
        newline = ""

        for line in source:
            i = 0
            if not inBlock:
                newline = ""

            while i < len(line):
             
                if not inBlock and i + 1 < len(line) and line[i:i+2] == "//":
                    break

                
                elif not inBlock and i + 1 < len(line) and line[i:i+2] == "/*":
                    inBlock = True
                    i += 1

             
                elif inBlock and i + 1 < len(line) and line[i:i+2] == "*/":
                    inBlock = False
                    i += 1

             
                elif not inBlock:
                    newline += line[i]

                i += 1

            if newline and not inBlock:
                res.append(newline)

        return res
        