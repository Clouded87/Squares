import random
from typing import List, Tuple


def gen_square_questions(
	start: int = 1,
	end: int = 25,
	include_square: bool = True,
	include_root: bool = True,
) -> List[Tuple[str, int, str]]:
	"""
	Generate questions for squares (n^2) and square roots (sqrt(n^2)).
	Returns list of (prompt, correct_answer, tag)
	"""
	questions: List[Tuple[str, int, str]] = []
	for n in range(start, end + 1):
		if include_square:
			questions.append((f"What is {n} squared?", n * n, f"{n}^2"))
		if include_root:
			sq = n * n
			questions.append((f"What is the square root of {sq}?", n, f"√{sq}"))
	return questions


def gen_cube_questions(
	start: int = 1,
	end: int = 10,
	include_cube: bool = True,
	include_root: bool = True,
) -> List[Tuple[str, int, str]]:
	"""
	Generate questions for cubes (n^3) and cube roots (cuberoot(n^3)).
	Returns list of (prompt, correct_answer, tag)
	"""
	questions: List[Tuple[str, int, str]] = []
	for n in range(start, end + 1):
		if include_cube:
			questions.append((f"What is {n} cubed?", n * n * n, f"{n}^3"))
		if include_root:
			cu = n * n * n
			questions.append((f"What is the cube root of {cu}?", n, f"∛{cu}"))
	return questions


def choose_mode() -> Tuple[bool, bool, bool, bool]:
	"""Prompt the user to choose which topics to practice.
	Returns a tuple: (squares, square_roots, cubes, cube_roots)
	"""
	print("\nSelect a practice mode:")
	print("  1) Squares only")
	print("  2) Square roots only")
	print("  3) Cubes only")
	print("  4) Cube roots only")
	print("  5) Squares + Square roots")
	print("  6) Cubes + Cube roots")
	print("  7) All four")

	while True:
		choice = input("Enter 1-7 (or 'q' to quit): ").strip().lower()
		if choice in {"q", "quit", "exit"}:
			print("Exiting quiz…")
			raise SystemExit(0)
		if choice not in {"1", "2", "3", "4", "5", "6", "7"}:
			print("Please enter a number between 1 and 7.")
			continue

		c = int(choice)
		if c == 1:
			return True, False, False, False
		if c == 2:
			return False, True, False, False
		if c == 3:
			return False, False, True, False
		if c == 4:
			return False, False, False, True
		if c == 5:
			return True, True, False, False
		if c == 6:
			return False, False, True, True
		# 7
		return True, True, True, True


def ask_questions(questions: List[Tuple[str, int, str]]) -> Tuple[List[str], List[str]]:
	"""
	Ask each question once in random order.
	Returns (correct_tags, incorrect_tags)
	"""
	random.shuffle(questions)
	correct: List[str] = []
	incorrect: List[str] = []

	for prompt, answer, tag in questions:
		while True:
			raw = input(f"{prompt} ")
			if raw.strip().lower() in {"q", "quit", "exit"}:
				print("Exiting quiz…")
				return correct, incorrect
			try:
				guess = int(raw)
				break
			except ValueError:
				print("Please enter a whole number (or type 'q' to quit).")

		if guess == answer:
			print("Correct!")
			correct.append(tag)
		else:
			print(f"Incorrect. The answer is {answer}.")
			incorrect.append(tag)

	return correct, incorrect


def main() -> None:
	print("Math Quiz: Squares, Square Roots (to 25) and Cubes, Cube Roots (to 10)")
	print("- Enter numbers only. Type 'q' to quit at any time.")

	# Choose mode
	use_squares, use_sq_roots, use_cubes, use_cu_roots = choose_mode()

	# Choose optional lower bounds (defaults to 1 if blank)
	def ask_lower_bound(label: str = "", default_val: int = 1) -> int:
		while True:
			raw = input(f"Bottom number to study for {label} (press Enter for {default_val}): ").strip()
			if raw == "":
				return default_val
			if raw.lower() in {"q", "quit", "exit"}:
				print("Exiting quiz…")
				raise SystemExit(0)
			try:
				n = int(raw)
				if n < 0:
					print("Please enter a non-negative integer.")
					continue
				return n
			except ValueError:
				print("Please enter a whole number, or press Enter to accept the default.")

	# Gather ranges only for selected topics
	sq_start = None
	cu_start = None
	if use_squares or use_sq_roots:
		sq_start = ask_lower_bound("squares/square roots (upper limit 25)", 1)
	if use_cubes or use_cu_roots:
		cu_start = ask_lower_bound("cubes/cube roots (upper limit 10)", 1)

	# Build questions
	questions: List[Tuple[str, int, str]] = []
	if use_squares or use_sq_roots:
		questions.extend(
			gen_square_questions(
				start=max(0, sq_start or 1),
				end=25,
				include_square=use_squares,
				include_root=use_sq_roots,
			)
		)
	if use_cubes or use_cu_roots:
		questions.extend(
			gen_cube_questions(
				start=max(0, cu_start or 1),
				end=10,
				include_cube=use_cubes,
				include_root=use_cu_roots,
			)
		)

	if not questions:
		print("No topics selected; exiting.")
		return

	round_num = 1
	remaining_questions = questions
	total_correct = 0
	total_attempted = 0

	while remaining_questions:
		print(f"\nRound {round_num}: {len(remaining_questions)} question(s)")
		correct_tags, incorrect_tags = ask_questions(remaining_questions)
		attempted = len(correct_tags) + len(incorrect_tags)
		total_attempted += attempted
		total_correct += len(correct_tags)

		print(f"Round {round_num} score: {len(correct_tags)}/{attempted}")

		if not incorrect_tags:
			break

		choice = input("Do you want to retry only the incorrect ones? (y/n) ").strip().lower()
		if choice != "y":
			break

		# Rebuild only the missed questions from their tags
		tag_to_question = {q[2]: q for q in questions}
		remaining_questions = [tag_to_question[tag] for tag in incorrect_tags]
		round_num += 1

	if total_attempted:
		print(f"\nFinal score: {total_correct}/{total_attempted} correct")


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\nInterrupted. Goodbye!")

