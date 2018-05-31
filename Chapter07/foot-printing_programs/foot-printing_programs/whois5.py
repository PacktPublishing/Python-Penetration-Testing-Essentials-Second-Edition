from lxml.html import fromstring
import requests

domain = raw_input("Enter the domain : ")
url = 'http://whois.domaintools.com/' + domain
user_agent = 'wswp'
headers = {'User-Agent': user_agent}
resp = requests.get(url, headers=headers)
html = resp.text

tree = fromstring(html)
ip = tree.xpath('//*[@id="stats"]//table/tbody/tr//text()')

list1 = []
for each in ip:
    each = each.strip()
    if each == "":
        continue
    list1.append(each.strip("\n"))

ip_index = list1.index('IP Address')
print "IP address ", list1[ip_index + 1]

loc1 = list1.index('IP Location')
loc2 = list1.index('ASN')
print 'Location : ', "".join(list1[loc1 + 1:loc2])
