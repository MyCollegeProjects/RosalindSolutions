import sys

def main():
	s1 = "TACCAATGGGTCCAGATACATAGTCCATTGCAACTGATGATGAAATTGTTCGTTCCGGACTGTGCGCCTTAAAAGGCCAGGAGGATGGCTGGCTGTGAGCGCAACGTAGCTCGATCTCCCCAATGAAACGAAGGATAAGGCGAGAAGAAACCTCACGCGTAACGAAGATTGGCCATCTGCGGAGGCCAACGCAGTACCAAACAGCTCTGATGTCGGCGCCAACATCAGTACGACACAATACCATCCACGAGAGCACCACAACGTGAACATTGGGCCTATGTATCCTGTGAGGACGTACGGGTCATAGATTCTGAGCCATATGTTACCAGATTTGACTGCTGACCATAGACGGACTTTAAAACCACACGGGCTCGATCGGAAATTGTCAGAGGGTTGCTTTGGACGTTCAATCCGTTACGTGATATAAAAGCCAGGACAGAGCCCCGTTTATACCTAGCGTGGCCTGGAGCCACTCCGCCTCACCACCTCGGGGGGCACAAGGAAAAACTATAACGGAGGACACTTCAGCCCGGCGCTAGGCTCATGCCGGAAGCGTTCCAGGAACTTGGTACTATAGACCAGGCGAATGTGAAGAGGACAATCCGGAGCGTCAGGCGTTAGGTAACATACGCATTTTCGCGCATATGGTCTATACACCGCAATACGGATGTTCGGCCTGTGTCATGCGGATTTCCCCATGCGTGCACTGGTTTGACACGGCAAATCGCCGTAGTCAGCTGCCACCCAAAAGCAGTTCGGCGTTGAGGGCAGCGATCGGATCTTCGATTAAACTTGTTCAATACTATGTTAGGCAACCAACGGAATAGCTTCCCAAGGCAGGAGCGAATAGAATGTCGAACCTCAGAACTGCGCGGGCCTAAACCGACCTGGTTCTAAAGCAAGAACGTATTAGGTCGAACGTTGACAGGCTATTATCGCGTCCCCACCCCTGCGATGCTCAACGGTGTGC"
	s2 = "TCCAAACGGGTGTAATCACATAGTCAAATGATACTGAAGTTGAACTTGCTCAGGGCGGAATGATCACTTCAAAAAGTGTGATACATACTTCCCTAGGGCTGACCCGCAGATCGCTTGAGCTCAAGAGCCGCGACCCCATGCGGTGCAGAAACACACGCCTGGCGAATACTAATAATCTGTCGGGCGCGACTAGTTGCCACAGAAATCGGCCATTCAGGCTTGTATCAAACTAGCAAAGTTCCGTGCACCGGAGAACTTGCACGAGAGCGTTTGGTGATTCGTGTCCGTGAGAAAGAGCGCAGCTGATATCCTAAGTCAGATGGTACCGTAATGCCCAGCGGTTCATAGACCTCGTATCAAGGGACACGTGCAACCTCCTGCCTGATTATGTGACTGCTGTGCTTGGTCAAATTGCCTCGTGGCGTACAAGACGCCTCAAGGTTTGTTCACATTCTGGCTCAAGCAGAAAATACTTAGTAGATCGATCACGAGTTCATCCACTAAGACTTATGCCCACACAGGTACGAGGCCTGCGCGACCCTGGATCGTAAACCTTTCCGGGACATGGTCGAGGTCTCACGCGGGAATTTGAGGTGCCAGGTCGGGACAGTCTGTCGTTACAGAGGTTTAGCCTTTTCGTTGATAACATCTAGACAAGTTAATTCACACGACCGCGCAGTCTAATACGTGCTGTCCGGTCGGGGTCGGGATTAGTTAGGCCAGATATGCGTTATCCGAGGGGCTCGGAATGGAGTGCCACGAGTACGGTGGCAATAGGATCGTTTAATGGACCTGATCGTTACTCTAGTATGAGAAGAGGGACATGCGGCGCCCAGGGAGTGAGAATATCAAACGAGTACCCCATGCCTGCGTGAACCGAAACCCGACGCATTCTGTCGGAGCCGCTTCATAGCTGGCCGGATTACAGGCAACGTACCAGTTTCAACACCACTAGCGCTCAGTGCTAAAG"
	hamm = 0
	l1 = list(s1)
	l2 = list(s2)

	for x in range(0, len(s1), 1):
		if l1[x]!=l2[x]:
			hamm+=1

	print hamm

if "__name__" == main():
	main()