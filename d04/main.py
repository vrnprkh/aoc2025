def parseInput(data : str):
	return [list(line) for line in data.split("\n")] 

offsets = [
	(0, 1),
	(0, -1),
	(1, 0),
	(-1, 0),
	(1, 1),
	(-1, 1),
	(-1, -1),
	(1, -1)
]

def part1(data: str):
	parsed = parseInput(data)
	total = 0
	for y, row in enumerate(parsed):
		for x, col in enumerate(row):
			if col != "@":
				continue
			count = 0
			for dx, dy in offsets:	
				if (y + dy >= 0 and y + dy < len(parsed) and x + dx >= 0 and x + dx < len(parsed[0]))  and parsed[y + dy][x + dx] == "@":
					count += 1
			if count < 4:
				total += 1
	return total

def part2(data : str):
	parsed = parseInput(data)
	
	total = 0
	lastTotal = 0
	while True:
		lastTotal = 0
		for y, row in enumerate(parsed):
			for x, col in enumerate(row):
				if col != "@":
					continue
				count = 0
				for dx, dy in offsets:	
					if (y + dy >= 0 and y + dy < len(parsed) and x + dx >= 0 and x + dx < len(parsed[0]))  and parsed[y + dy][x + dx] == "@":
						count += 1
				if count < 4:
					lastTotal += 1	
					parsed[y][x] = '.'
					total += 1
		if lastTotal == 0:
			break
	return total
	

	return

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