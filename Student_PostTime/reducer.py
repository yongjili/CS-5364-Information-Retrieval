#!/usr/bin/python

import sys

hour_ls = [0 for i in range(24)]        # a list of 24 hours
oldKey = None       # author_id

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisHour = data_mapped

    if oldKey and oldKey != thisKey:
        max_freq = max(hour_ls)
        for hour in range(24): 
            if hour_ls[hour] == max_freq:
                print oldKey, "\t", hour

        oldKey = thisKey;
        hour_ls = [0 for i in range(24)]

    oldKey = thisKey
    hour_ls[int(thisHour)] += 1  # count freq for hour

if oldKey != None:
   max_freq = max(hour_ls)
   for hour in range(24): 
       if hour_ls[hour] == max_freq:
           print oldKey, "\t", hour

