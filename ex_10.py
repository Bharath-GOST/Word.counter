fname = input('Enter File: ')
if len(fname) < 1 : fname = 'words.txt' ## save file as words.txt, you don't need to input a file 
hand = open(fname)

di =dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
       di[w] = di.get(w, 0) + 1

#print(di)

tmp = list()
for k,v in di.items() :
     newt = (v,k)
     tmp.append(newt)

#print('Flipped',tmp)
tmp = sorted(tmp, reverse=True)
#print('Sorted', tmp[:5])

for v,k in tmp[:5] :    #only print top 5 items
    print(k,v)
