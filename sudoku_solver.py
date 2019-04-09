# This programme solves sudoku using backtracking algorithm
# Implemented --python-version 3.7

# Sudoku
sudoku = [
[3, 0, 6, 5, 0, 8, 4, 0, 0],
[5, 2, 0, 0, 0, 0, 0, 0, 0],
[0, 8, 7, 0, 0, 0, 0, 3, 1],
[0, 0, 3, 0, 1, 0, 0, 8, 0],
[9, 0, 0, 8, 6, 3, 0, 0, 5],
[0, 5, 0, 0, 9, 0, 6, 0, 0],
[1, 3, 0, 0, 0, 0, 2, 5, 0],
[0, 0, 0, 0, 0, 0, 0, 7, 4],
[0, 0, 5, 2, 0, 6, 3, 0, 0],
]

fixed_idx, track_queue = [], []
block_range = [(0, 3), (3, 6), (6, 9)]

for r in range(9):
	for c in range(9):
		if sudoku[r][c]:
			fixed_idx.append((r,c))
		else:
			track_queue.append((r,c))

def checker(r,c,n):
	# Check in rows and columns
	for idx in range(9):
		if sudoku[r][idx] == n or sudoku[idx][c] == n:
			return False

	# Check in block
	for i in range(*block_range[r//3]):
		for j in range(*block_range[c//3]):
			if sudoku[i][j] == n:
				return False
	return True

def display():
	for elt in sudoku:
		print(elt)
	print('')

# Backtracking...
rc = 0
while rc < len(track_queue):
	r, c = track_queue[rc]
	for n in range(sudoku[r][c]+1, 10):
		if checker(r,c,n):
			sudoku[r][c] = n
			rc += 1
			break
	else:
		for j in range(c, 9):
			if (r, j) not in fixed_idx:
				sudoku[r][j] = 0
		rc -= 1
		
# Solution display
display()