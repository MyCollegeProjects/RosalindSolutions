import sys

def main():
	s = "AGTTACATGCAGTTACACGCCAGTTACAAAAGTTACAAGTTACACGAGTTACAGTTATAGTTACACGGATGAATAGTTACAAGTTACAATGATGAACTTAGTAAGTTACAGCATCAGTTACAAAGTTACACGAGTTACACCAGTTACATAGTTACAATCAGTTACAAGTTACATCTGGAGTTACAAGACGCGAGTTACAATGCATAGTTACAACACAGTTACAAGTTACATACCGTAGTTACATTCAAGTTACATTGGAGAGTTACAAAGTTACAGCAAGTTACAAGTTACAAGTTACAAGTTACAAGTTACACTGAGTTACAAGTTACAAGCAGTTACACTAGTTACAGCAGAGTTACATAGTTACAACGAGTTACAAAAGTTACATGCTTTCCAGTTACAAGTTACACTACCAGTTACATAGTTACACTACCACAGTTACAAAGTTACAAGTTACAAGTTACAAGTTACATAAGTTACAATCAGTTACAAAGTTACAGAGTTACAAAGTTACACATAACCAGTTACAAAGTTACACGGGCGCAGTTACAACAGTTACATTAAAAAGTTACAAAAGTTAGTTACAGAGTTACATGGAGTAGTTACACTTAGTTACAACATCGGAGTTACAAAGTTACATCAGTTACACACGAAGTTACAAAAAGTTACATAGTTACAAAGAGCCACAGTTACAAGTTACAAGAGTTACAACAGCTTAGTTACATAAGTTACATAGTCCGGAGTTACAAGTTACACCAAGTTACACTAGTTACATGTTGGAGTTACATAGTTACAAGTTACATGAGTTACACTAAGTTACAACAGTTACAAAGTTACAAGTTACAATACAGTTACACAGTTACAGGCGGGAAGAAGGCGAGTTACATCTAGTTACAATAGTTACAGAGTTACACAATTCAAGTTACAAGTTACAAATGTCTCTAGTTACAGAAAGTTACAGAGTTACAAAGTTACAAGTTACACAAGTTACA"
	t = "AGTTACAAG"
	for x in range(0, len(s)-len(t), 1):
		if s[x:x+len(t)] == t:
			print x+1,

if '__name__' == main():
	main()