def parseInput(data : str):
	rows = data.split("\n")

	

	numRows = rows[:len(rows) - 1]
	intRows = []
	for row in numRows:
		intRows.append([])
		for e in row.split(" "):
			if len(e) > 0:
				intRows[-1].append(int(e))
	ops = rows[len(rows) - 1]
	filterOps = []
	for e in ops.split(" "):
		if len(e) > 0:
			filterOps.append(e)


	return intRows, filterOps



def part1(data: str):
	nums, opdata = parseInput(data)
	total = 0
	for col in range(len(nums[0])):
		op = opdata[col]

		if op == "+":
			for i in range(len(nums)):
					total += nums[i][col]
		else:
			mult = 1
			for i in range(len(nums)):
				mult *= nums[i][col]
			total += mult
	
	return total 




def parse2(data : str):
	problems = []
	rows = data.split("\n")
	for col in range(len(rows[0])):
		if all(rows[i][col] == ' ' for i in range(len(rows))):
			continue	
		if len(rows[-1]) > col and rows[-1][col] != ' ':
			problems.append([rows[-1][col]])

			
		num = int("".join([rows[j][col] for j in range(len(rows) - 1)]))
		problems[-1].append(num)	

	return problems



def part2(data : str):
	problems = parse2(data)

	total = 0
	for problem in problems:
		op = problem[0]
		nums = problem[1:]
		if op == "+":
			total += sum(nums)
		else:
			mult = 1
			for e in nums:
				mult *= e
			total += mult

	return total 
		



def main():
	sources = [
						"inputs/sample.txt", 
						"inputs/input.txt"
						]
	for source in sources:
		print(source)
		with open(source) as f:
			s = f.read()
			print("part1")
			print(part1(s))
			print("part2")
			print(part2(s))

if __name__ == "__main__":
	main()