class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Step 1: Initialize tracking structures
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    box_index = (r // 3) * 3 + (c // 3)
                    boxes[box_index].add(val)

        # Step 2: Backtracking function
        def backtrack(index):
            if index == len(empty):
                return True  # solved

            r, c = empty[index]
            box_index = (r // 3) * 3 + (c // 3)

            for num in map(str, range(1, 10)):
                if (num not in rows[r] and
                    num not in cols[c] and
                    num not in boxes[box_index]):

                    # Place number
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_index].add(num)

                    # Recurse
                    if backtrack(index + 1):
                        return True

                    # Undo (backtrack)
                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_index].remove(num)

            return False

        backtrack(0)