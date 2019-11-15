import sys

def rab_fibbo(pn, pm, n, k):
	cn = 0
	cm = 0

	if n == 1:
		i = pn+pm
		print i
		return i

	else:
		cm = pm+pn
		cn = pm*k
		n = n-1
		rab_fibbo(cn, cm, n, k)

def main():
	n = 32
	k = 5
	r = rab_fibbo(1, 0, n, k)
	print r

if '__name__' == main():
	main()