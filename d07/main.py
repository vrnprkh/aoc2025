from functools import cache 
def parseInput(data : str):
	return [list(line) for line in data.split("\n")] 

def part1(data : str):
	m = parseInput(data)	
	def dfs(x, y, visited):
		if y == len(m) - 1:
			return
		if m[y + 1][x] == "^":
			if (x, y+1) in visited:
				return
			visited.add((x, y + 1))	
			dfs(x + 1, y + 1, visited)
			dfs(x - 1, y + 1, visited)
			return
		dfs(x, y + 1, visited)
	xStart = "".join(m[0]).find("S")
	visited = set()
	dfs(xStart, 0, visited)
	return len(visited)

def part2(data : str):
	m = parseInput(data)
	@cache
	def dfs(x, y):
		if y == len(m) - 1:
			return 1
		if m[y + 1][x] == "^":
			return dfs(x + 1, y + 1) + dfs( x - 1, y + 1)
		return dfs(x, y + 1)
		
	xStart = "".join(m[0]).find("S")
	return dfs(xStart, 0)


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