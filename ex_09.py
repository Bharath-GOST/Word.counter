fname = input('Enter File: ')
if len(fname) < 1 : fname = 'words.txt'
hand = open(fname)

di =dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
    # idiom: retrieve/create/update counter
       di[w] = di.get(w, 0) + 1

#print(di)
#now we wnat to find the most common word
largest = -1
theword = None
for k,v in di.items() :
    if v > largest :
        largest = v
        theword = k
print(theword,largest)        #print the largest key and value.