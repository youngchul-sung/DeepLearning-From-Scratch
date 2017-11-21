#!/bin/env python

import numpy as np

def operator(x1, x2, w1, w2, b):
	x = np.array([x1, x2])
	w = np.array([w1, w2])

	y = np.sum(w*x) + b
	return 1 if y > 0 else 0

def AND(x1, x2):
	return operator(x1, x2, 0.5, 0.5, -0.7)

def OR(x1, x2):
	return operator(x1, x2, 0.5, 0.5, -0.2)
	
def NAND(x1, x2):
	return operator(x1, x2, -0.5, -0.5, 0.7)

def XOR(x1, x2):
	s1 = NAND(x1, x2)
	s2 = OR(x1, x2)

	return AND(s1, s2)

xs = [(0, 0), (0, 1), (1, 0), (1, 1)]
for x1, x2 in xs:
	print(AND(x1, x2))

for x1, x2 in xs:
	print(OR(x1, x2))

for x1, x2 in xs:
	print(NAND(x1, x2))

for x1, x2 in xs:
	print(XOR(x1, x2))
