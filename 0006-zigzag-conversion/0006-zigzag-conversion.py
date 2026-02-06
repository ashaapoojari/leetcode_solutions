class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or len(s) <= numRows:
            return s

        rows = [""] * numRows
        currRow = 0
        goingDown = False

        for c in s:
            rows[currRow] += c

            if currRow == 0 or currRow == numRows - 1:
                goingDown = not goingDown

            currRow += 1 if goingDown else -1

        return "".join(rows)
