count=dict()
fname=input('Enter file name : ')
fh=open(fname)
for line in fh:
    line=line.rstrip()
    if line.startswith('From:'):
        continue
    if line.startswith('From'):
        words=line.split()
        key=words[1]
        count[key]=count.get(key,0)+1
bigword=None
bigcount=None
for k,v in count.items():
    if bigcount is None or v>bigcount:
        bigword=k
        bigcount=v
print(bigword,bigcount)
