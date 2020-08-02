fname=input('Enter file name : ')
if len(fname) < 1 : fname = "mbox-short.txt"
fh=open(fname)
count=dict()
for line in fh:
    line=line.rstrip()
    if line.startswith('From:'):
        continue
    if line.startswith('From'):
        words=line.split()
        time=words[5]
        time=time.split(':')
        ntime=time[0]
        count[ntime]=count.get(ntime,0)+1
lst=list()
for k,v in count.items():
    tup=(k,v)
    lst.append(tup)
for k,v in sorted(lst):
    print(k,v)

#sorted((k,v) for k,v in count.items())
