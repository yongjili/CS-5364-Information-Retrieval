#!/usr/bin/python

import sys

oldKey = None       # tag id 
listID = []
tagrank = {}

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

count = 0
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisId = data_mapped

    if oldKey and oldKey != thisKey:
        #print oldKey, "\t", count 
        tagrank[oldKey] = count
        listID = []
        count = 0
        oldKey = thisKey;

    oldKey = thisKey
    if thisId not in listID:
        listID.append(thisId)       
        count += 1

if oldKey != None:
    #print oldKey, "\t", count
    tagrank[oldKey] = count

for w in sorted(tagrank, key = tagrank.get, reverse = True):
    print w, "\t",  tagrank[w]



