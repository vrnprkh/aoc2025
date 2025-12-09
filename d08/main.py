from functools import cache 
from collections import defaultdict
import math
def parseInput(data : str):
	lines = data.split("\n")
	return [tuple([int(e) for e in line.split(",")]) for line in lines]



def dist2(p1, p2):
	x1,y1,z1 = p1
	x2,y2,z2 = p2
	return (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2

def part1(data : str, size = 10):
	p = parseInput(data)
	conns = []
	for i in range(len(p)):
		for j in range(i + 1, len(p)):
			conns.append([dist2(p[i], p[j]), p[i], p[j]])

	conns.sort()
	networks = []

	for conn in conns[:size]:
		inNetworks = []
		for network in networks:
			if conn[1] in network or conn[2] in network:
				inNetworks.append(network)
		
		if len(inNetworks) == 0:
			networks.append({conn[1], conn[2]})
		elif len(inNetworks) == 1:
			inNetworks[0].add(conn[1])
			inNetworks[0].add(conn[2])
		else:
			networks.remove(inNetworks[1])
			inNetworks[0].update(inNetworks[1])
	return math.prod(sorted([len(n) for n in networks])[-3:])

def part2(data : str):
	p = parseInput(data)
	conns = []
	for i in range(len(p)):
		for j in range(i + 1, len(p)):
			conns.append([dist2(p[i], p[j]), p[i], p[j]])

	conns.sort()
	networks = []
	remaining = set(p)
	last = None
	for conn in conns:
		inNetworks = []
		for network in networks:
			if conn[1] in network or conn[2] in network:
				inNetworks.append(network)
		
		if len(inNetworks) == 0:
			networks.append({conn[1], conn[2]})
		elif len(inNetworks) == 1:
			inNetworks[0].add(conn[1])
			inNetworks[0].add(conn[2])
		else:
			networks.remove(inNetworks[1])
			inNetworks[0].update(inNetworks[1])

		remaining.discard(conn[1])
		remaining.discard(conn[2])
		if len(remaining) == 0:
			last = conn
			break
	
	return last[1][0] * last[2][0]

def main():
	sources = [
						["inputs/sample.txt", 10], 
						["inputs/input.txt", 1000],
						]
	for source, size in sources:
		print(source)
		with open(source) as f:
			s = f.read()
			print("part1")
			print(part1(s, size))
			print("part2")
			print(part2(s))

if __name__ == "__main__":
	main()