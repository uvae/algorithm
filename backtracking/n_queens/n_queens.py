def solve_n_queens(n=8):
	"""
	8 퀸즈 문제를 해결하는 함수
	Args:
		n: 체스판의 크기와 퀸의 개수 (기본값 8)
	Returns:
		solutions: 가능한 모든 해결책의 리스트
	"""
	def is_safe(board, row, col):
		# 같은 열에 퀸이 있는지 확인
		for i in range(row):
			if board[i] == col:
				return False
			
		# 왼쪽 대각선 확인
		for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
			if board[i] == j:
				return False
			
		# 오른쪽 대각선 확인
		for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
			if board[i] == j:
				return False
			
		return True

	def backtrack(board, row, depth=0):
		indent = "    " * depth
		print(f"\n{indent}현재 상태 (행 {row}):")
		print_solution(board, indent)

		# 모든 행에 퀸을 배치했다면 해결책 추가
		if row == n:
			print(f"{indent}해결책 발견!")
			solutions.append(board[:])
			return
		
		# 현재 행의 각 열에 퀸을 놓아보기
		for col in range(n):
			if is_safe(board, row, col):
				print(f"{indent}행 {row}, 열 {col}에 퀸 배치 시도")
				board[row] = col  # 퀸 배치
				backtrack(board, row + 1, depth + 1)  # 다음 행으로 이동
				board[row] = -1  # 백트래킹
				print(f"{indent}행 {row}, 열 {col}에서 백트래킹")

	solutions = []
	initial_board = [-1] * n  # -1로 초기화된 체스판
	backtrack(initial_board, 0)
	return solutions

def print_solution(board, indent=""):
	"""
	체스판 형태로 해결책을 출력하는 함수
	"""
	n = len(board)
	for row in range(n):
		line = indent
		for col in range(n):
			if board[row] == col:
				line += "Q "
			elif board[row] == -1:
				line += "· "
			else:
				line += ". "
		print(line)
	print()

# 실행 및 결과 출력
print("N-Queens 문제 해결 과정:")
print("=" * 50)
solutions = solve_n_queens(4)  # 4x4로 변경하여 과정을 더 명확하게 보여줌
print("=" * 50)
print(f"\n총 {len(solutions)}개의 해결책을 찾았습니다.")
print("\n최종 해결책들:")
for i, solution in enumerate(solutions, 1):
	print(f"\n해결책 {i}:")
	print_solution(solution)