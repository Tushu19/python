import re
fname=input('Enter file name : ')
if len(fname) < 1 : fname = "test_sample.txt"
fh=open(fname)
list=list()
for line in fh:
    line=line.rstrip()
    x=re.findall('[0-9]+',line)
    if len(x)<1: continue

    for i in range(len(x)):
        num=int(x[i])
        list.append(num)
print(sum(list))
