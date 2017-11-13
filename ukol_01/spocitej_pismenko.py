#! /usr/bin/env python3

slovo = "Kokrhat"
pismeno = "k"

def spocitej_pismenko(slovo, pismeno):
	a = list(slovo.lower())
	b = a.count(pismeno)
	print("Ve slove {} se vyskytuje {}-krat pismeno {}.".format(slovo, b, pismeno))

spocitej_pismenko(slovo, pismeno)
			


