'''
	Question: A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a 				string is the number of symbols that it contains.

			An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

			Given: A DNA string s of length at most 1000 nt.

			Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

'''



inputString = raw_input("enter input String")

length = len(inputString)

genomeDict = dict()
genomeDict['A'] = 0
genomeDict['T'] = 0
genomeDict['C'] = 0
genomeDict['G'] = 0 
for i in xrange(length):
	if inputString[i] == 'A':
		genomeDict['A'] += 1
	elif inputString[i] == 'T':
		genomeDict['T'] += 1
	elif inputString[i] == 'C':
		genomeDict['C'] += 1
	elif inputString[i] == 'G':
		genomeDict['G'] += 1



print genomeDict
