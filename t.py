import urllib.request, urllib.parse, urllib.error
import json
import ssl



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = "https://py4e-data.dr-chuck.net/comments_1983050.json"
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()

info = json.loads(data)
ans = 0
for elt in info["comments"]:
    ans += int(elt["count"])
    
print(ans)
