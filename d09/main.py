from functools import cache 
from collections import defaultdict
from dataclasses import dataclass
from shapely import Polygon
def parseInput(data : str):
	return [[int(e) for e in line.split(",")] for line in data.split("\n")]

def area(x1, y1, x2, y2):
	return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)	

def part1(data : str):
	p = parseInput(data)

	best = 0
	for y in range(len(p)):
		for x in range(y, len(p)):
			x1, y1 = p[y]
			x2, y2 = p[x]
			best = max(best, area(x1, y1, x2, y2))
	return best

def part2(data : str):
	p = parseInput(data)	

	thisP = Polygon(p)
	best = 0
	for p1 in p:
		for p2 in p:
			cx = min(p2[0], p1[0])
			tx = max(p2[0], p1[0])
			cy = min(p2[1], p1[1])
			ty = max(p2[1], p1[1])

			rect = Polygon([(cx, cy),(cx, ty), (tx , ty), (tx, cy), (cx, cy)])
			if thisP.contains(rect):		
				if (area(cx, cy, tx, ty) > best):
					best = max(best, area(cx, cy, tx, ty))	
	return best


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
