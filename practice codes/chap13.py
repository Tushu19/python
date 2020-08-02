import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

#if api_key is False:
#    api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/comments_775512.xml'
#else :
#    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

lst=list()
uh=urllib.request.urlopen(serviceurl, context=ctx)
data=uh.read()
tree=ET.fromstring(data)

print(data)

count=tree.findall('./comments/comment')
for item in count:
    lst.append(int(item.find('count').text))
print(sum(lst))
