import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = "https://py4e-data.dr-chuck.net/comments_1983049.xml"

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()

tree = ET.fromstring(data.decode())

results = tree.findall('comments/comment/count')
ans = 0
for elt in results:
    ans += int(elt.text)
print(ans)

