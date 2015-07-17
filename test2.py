# -*- coding: utf-8 -*-
from random import randint
from random import sample


suit = ["♠", "♥", "♣", "♦"]
rank = ["A ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "10", "J ", "Q ", "K "]
deck = []
pos_used = []
res = ""

for s in suit:
	for r in rank:
		deck.append(s + r)

print "+++++++++++++++++++++++++++++++++++++++++++"
print "+                                         +"
print "+",

cards = sample(deck, 10)
for card in cards:
	print card,

print "+\n+                                         +"
print "+++++++++++++++++++++++++++++++++++++++++++"

"""
ctr = 0
while (ctr < 10):
	pos = randint(1, len(deck))
	print deck[pos]
	ctr = ctr + 1
"""