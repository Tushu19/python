large= None
small=None
while True:
    num=input('Enter any number : ')
    if num=='done': break
    try:
        num=int(num)
        if large is None:
            large=num
            small=num
        elif num>large:
            large=num
        elif num<small:
            small=num
        continue
    except:
        print('Invalid input')
print('Maximun',large)
print('Minimun',small)
