from z3 import *
def parseLine(line):
	e = line.split()
	targetLights = tuple(e[0][1:-1])
	targetLights = tuple([True if a == "#" else False for a in targetLights])
	buttons = [[int(f) for f in button[1:-1].split(",")] for button in e[1: -1]]	
	joltage = tuple([int(f) for f in e[-1][1:-1].split(",")])
	return targetLights, buttons, joltage

def parseInput(data : str):
	return [parseLine(e) for e in data.split("\n")]

def solveOne(target, buttons, joltage):
	start = tuple([False for e in range(len(target))])	
	states = set()
	states.add(start)
	def step():
		nonlocal states
		newStates = set()
		for state in states:
			for button in buttons:
				newState = tuple([not e if i in button else e for i, e in enumerate(state)])
				newStates.add(newState)
		states = newStates
	i = 0
	while True:
		i += 1
		step()
		if target in states:
			break
	return i

def part1(data : str):
	lines = parseInput(data)
	res = sum([solveOne(*line) for line in lines])
	return res

def solveTwo(target, buttons, joltage):
	solver = Optimize()
	presses = [Int("b" + str(i)) for i in range(len(buttons))]

	for press in presses:
		solver.add(press >= 0)	
	for i, j in enumerate(joltage):
		relevant = [presses[b] for b in range(len(buttons)) if i in buttons[b]]
		solver.add(Sum(relevant) == j)
	
	solver.minimize(Sum(presses))
	if solver.check() == sat:	
		model = solver.model()
		return sum([model[p].py_value() for p in presses])
			
	return 0

def part2(data : str):
	lines = parseInput(data)
	res = sum([solveTwo(*line) for line in lines])
	return res

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
