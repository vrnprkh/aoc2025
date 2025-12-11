from functools import cache 
from collections import defaultdict
import math

def parseLine(line: str):
	l = line.split()
	l[0] = l[0][:-1]
	return l
def parseInput(data : str):
	lines = data.split("\n")
	return [parseLine(line) for line in lines]

def buildMap(p):
	conns = defaultdict(set)

	for e in p:
		f = e[0]
		to = e[1:]
		for t in to:
			conns[f].add(t)
	return conns

def part1(data : str):
	p = parseInput(data)
	conns = buildMap(p)

	@cache
	def dfs(curr):
		if curr == "out":
			return 1
		return  sum([dfs(e) for e in conns[curr]])
	return dfs('you')

def part2(data : str):
	p = parseInput(data)
	conns = buildMap(p)

	@cache
	def dfs(curr, hasDac, hasFft):
		if curr == "out":
			if hasDac and hasFft:
				return 1
			else:
				return 0
		total = 0	
		for e in conns[curr]:
			if e == "dac":
				total += dfs(e, True, hasFft)
			elif e == "fft":
				total += dfs(e, hasDac, True)
			else:
				total += dfs(e, hasDac, hasFft)
		return total


	return dfs('svr', False, False)


def main():
	sources = [
						"inputs/sample.txt", 
						"inputs/input.txt",
						]
	for source in sources:
		with open(source) as f:
			s = f.read()
			print("part1")
			print(part1(s))
			print("part2")
			print(part2(s))

if __name__ == "__main__":
	main()