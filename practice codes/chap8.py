fname=input('Enter file name : ')
fh=open(fname)
list=list()
for line in fh:
    line=line.rstrip()
    words=line.split()
    for i in words:
        if i in list:
            continue
        else:
            list.append(i)
list.sort()
print(list)
