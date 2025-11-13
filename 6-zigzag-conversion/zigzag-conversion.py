class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if only one row, the zigzag is just the same string
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False

        # Iterate over each character
        for c in s:
            rows[current_row] += c  # Add char to current row

            # Flip direction if at top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            # Move up or down
            current_row += 1 if going_down else -1

        # Combine all rows
        return ''.join(rows)
