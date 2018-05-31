import urllib
import re
from bs4 import BeautifulSoup
url = raw_input("Enter the URL ")
ht= urllib.urlopen(url)
html_page = ht.read()
email_pattern=re.compile(r'\b[\w.-]+?@\w+?\.\w+?\b')
for match in re.findall(email_pattern,html_page ):
	print match

