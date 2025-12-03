from functools import cache
def parseInput(data : str):
	banks = data.split("\n")
	return banks	


def part1(data: str):
	banks = parseInput(data)
	total = 0
	for line in banks:
		best = 0
		for i in range(len(line)):
			for j in range(i + 1, len(line)):
				if int(line[i] + line[j]) > best:
					best = int(line[i] + line[j])
			
		total += best

	return total



def joltage(line: str, targetSize: int) -> int:
	
	dp = [
		[0 for _ in range(len(line) + 1)] for j in range(targetSize + 1)
	]
	for i in range(len(dp[0])):
		dp[0][i] = ""	

	for selecting in range(1, targetSize + 1):	

		for size in range(selecting, len(line) + 1):
			if size == selecting:
				dp[selecting][size] = int(line[len(line) - size:])
			else:
				dp[selecting][size] = max(
						int(line[len(line) - size] + str(dp[selecting - 1][size - 1])),
						dp[selecting][size - 1]
					)	
			
	return dp[targetSize][len(line)]	




	

def part2(data : str):
	banks = parseInput(data)
	return sum([joltage(line, 12) for line in banks])	


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