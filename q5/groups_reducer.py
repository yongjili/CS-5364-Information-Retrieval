import sys

oldKey = None
posters = []


for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue

	thisKey, author_id = data_mapped

	if oldKey and oldKey != thisKey:
		print oldKey, "\t", posters
		oldKey = thisKey
		posters = []

	oldKey = thisKey
	posters.append(int(author_id))

if oldKey != None:
	print oldKey, "\t", posters
