from functools import cache, cached_property
from collections import defaultdict
from dataclasses import dataclass
import math


@dataclass
class Shape:
	spots : list[tuple[int, int]]

@dataclass
class Grid:
	w : int
	h : int
	counts : list[int]


def parseShapes(top):
	shapes = []	
	for shape in top:
		ls = shape.split("\n")[1:]

		es = [list(l) for l in ls]
		res = []
		for y, row in enumerate(es):
			for x, e in enumerate(row):
				if e == "#":
					res.append((x, y))
		shapes.append(Shape(res))
	return shapes

def parseGrids(prod):
	grids = []
	for pr in prod.split("\n"):
		ls = pr.split()	
		x, y = [int(e) for e in ls[0][:-1].split("x")]
		counts = [int(e) for e in ls[1:]]
		grids.append(Grid(x, y, counts))
	return grids	

def parseInput(data : str):
	sections = data.split("\n\n")

	top = sections[:-1]
	prod = sections[-1]

	shapes = parseShapes(top)
	grids = parseGrids(prod)
	return shapes, grids

def part1(data : str):
	shapes, grids = parseInput(data)
	totalGrids = len(grids)
	trivialValidGrids = 0
	trivialInvalidGrids = 0	
	undecidedGrids = 0
	for grid in grids:
		totalSize = sum([grid.counts[i] * len(shapes[i].spots) for i in range(len(shapes))])
		shapeCount = sum(grid.counts)
		if totalSize > grid.h * grid.w:
			trivialInvalidGrids += 1
		elif shapeCount * 9 <= grid.h * grid.w:
			trivialValidGrids += 1
		else:
			undecidedGrids +=1 
	print("Total: ", totalGrids, "Valid ", trivialValidGrids, "Invalid ", trivialInvalidGrids, "undecided ", undecidedGrids)

	return 

def part2(data : str):
	p = parseInput(data)
	return 


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