import requests
import re

output=''

com=requests.get('https://data.iana.org/TLD/tlds-alpha-by-domain.txt').text
com=re.sub('#.*\n','',com).split('\n')
com.remove('')
for one in com:
  output+='server=/%s/127.0.0.1#5335\n'%one.lower()
with open('docs/dnsmasq-chinadns.conf','w') as f:
  f.write(output)
