def parseInput(data : str):
	lines = data.split("\n")	
	ranges = []
	at = 0
	for i, l in enumerate(lines):
		if len(l) == 0:
			at = i + 1
			break
		ranges.append(tuple([int(e) for e in l.split("-")]))
	return ranges, [int(lines[j]) for j in range(at, len(lines))] 

def inRange(range, e):
	return e >= range[0] and e <= range[1]

def part1(data: str):
	ranges, ings = parseInput(data)
	count = 0 
	for e in ings:
		for r in ranges:
			if inRange(r, e):
				count += 1
				break
	return count

def overlap(r1, r2):
	return r1[0] <= r2[1] and r2[0] <= r1[1]

def combine(r1, r2):
	return (min(r1[0], r2[0]), max(r1[1], r2[1]))

def part2(data : str):
	ranges, _ = parseInput(data)
	while True:
		merged = []		
		for r in ranges:
			found = False	
			for j, r2 in enumerate(merged):
				if overlap(r, r2):
					merged[j] = combine(r, r2)
					found = True
					break
			if not found:
				merged.append(r)
		
		if len(merged) == len(ranges):
			break
		ranges = merged[:]

	total =0 
	for e in merged:
		size = e[1] - e[0] + 1
		total += size
	return 	total



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