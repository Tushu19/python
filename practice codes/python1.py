text = "X-DSPAM-Confidence:    0.8475";
ipos=text.find(':')
mstr=text[ipos+1:]
mstr=float(mstr)
print(mstr)
