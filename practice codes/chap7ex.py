fname=input('Enter file name : ')
fh=open(fname)
sum=0
count=0
for line in fh:
    if not line.startswith('X-DSPAM-Confidence:'):continue
    count=count+1
    ipos=line.find(':')
    num=line[ipos+1:]
    num=float(num)
    sum=sum+num
print('Average spam confidence:',sum/count)
