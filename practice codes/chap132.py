import json
import urllib.request, urllib.parse, urllib.error
import ssl

serviceurl = 'http://py4e-data.dr-chuck.net/comments_775513.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh=urllib.request.urlopen(serviceurl, context=ctx)

data=uh.read().decode()

info = json.loads(data)
print('User count:', len(info))
#print(info)
lst=list()
for item in info["comments"]:
    count= item["count"]
    lst.append(int(count))
print(sum(lst))
