fname = input("Enter file name: ")
try:
    fh=open(fname)
except:
    print('Enter valid name!!!')
    quit()

count=0
for line in fh:
    line=line.rstrip()
    if line.startswith('From:'):
        continue
    if line.startswith('From'):
        words=line.split()
        print(words[1])
        count=count+1
print("There were", count, "lines in the file with From as the first word")
