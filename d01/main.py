sources = ["inputs/input.txt", "inputs/sample_input.txt"]




def parseInput(text: str):
	return [(e[0], int(e[1:])) for e in text.split("\n")]



def part1(data):
	total = 50
	count = 0 
	for dir, amount in data:
		if dir == "R":	
			total = (total + amount) % 100
		else:
			total = (total - amount + 100) % 100
		if total == 0:
			count += 1
	print(count)

def part2(data):
	curr = 50
	count = 0
	for dir, rotation in data:
		count += rotation // 100
		rotation = rotation % 100
		if rotation == 0:
			continue	
		if dir == "L":
			rotation *= -1
			if (rotation + curr <= 0) and (curr != 0):
				count += 1
		else:
			if rotation + curr >= 100:
				count += 1

		curr = (curr + rotation + 100) % 100

	print(count)

def main():
	for source in sources:
		with open(source) as f:
			print(source)
			res = parseInput(f.read())
			print("part 1")
			part1(res)
			print("part 2")
			part2(res)

if __name__ == "__main__":
	main()	