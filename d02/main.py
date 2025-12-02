




def parseInput(data : str):
	data = data.split(",")
	data =[e.split("-") for e in data]	
	return [[int(e[0]), int(e[1])] for e in data]



def valid(id):
	id = str(id)

	if len(id) % 2 == 1:
		return True

	return not id[:len(id) // 2] == id[len(id) // 2:]


def valid2(id):
	id = str(id)

	for size in range(1,len(id)):
		if len(id) % size != 0:
			continue
		strs = [id[i * size : (i + 1) * size] for i in range(len(id) // size)]
		if len(strs) <= 0:
			continue	
		if len(set(strs)) == 1:

			return False

	return True
			

def part1(data):
	parsed = parseInput(data)
	total = 0
	for endpoints in parsed:
		for id in range(endpoints[0], endpoints[1] + 1):
			if not valid(id):
				total += id
	print(total)


def part2(data):
	parsed = parseInput(data)
	total = 0
	for endpoints in parsed:
		for id in range(endpoints[0], endpoints[1] + 1):
			if not valid2(id):
				total += id
	print(total)



def main():
	sources = ["inputs/sample.txt", 
						"inputs/input.txt"
						]
	for source in sources:
		print(source)
		with open(source) as f:
			s = f.read()
			print("part1")
			part1(s)
			print("part2")
			part2(s)


if __name__ == "__main__":
	main()