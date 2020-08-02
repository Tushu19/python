#open file
fname=input('Enter file name :')
fh=open(fname)
#content=fh.read()
for line in fh:
    line=line.rstrip()
    print(line.upper())
