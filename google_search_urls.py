#!/usr/bin/env python
# coding: utf8

# показывает выдачу по заданному ключевому слову

import sys
import urllib2
import urllib
import lxml.html

class GooglePage:
	def __init__(self, query, page = 0):
		self.query = query
		self.page = page
	def getUrl(self):
		return "http://www.google.com/search?q={0}&start={1}".format(urllib.quote(self.query), self.page)
	def _parse(self):
		headers = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux i686; rv:8.0.1) Gecko/20100101 Firefox/8.0.1' }
		req = urllib2.Request(self.getUrl(), None, headers)
		page = urllib2.urlopen(req)
		html = page.read()
		self.root = lxml.html.document_fromstring(html).getroottree().getroot()
		results = self.root.cssselect('ol li a.l')
		for item in results:
			print item.get('href')
	
	def next(self):
		return GooglePage(self.query, self.page + 10)
	def execute(self):
		self._parse()

def usage():
	print "Usage: " + sys.argv[0] + " query page_count"
	print "query - search query"
	print "page_count - count page for parse"


def main():
	if len(sys.argv) != 3:
		print "error"
		usage()
	else:
		query = sys.argv[1]
		count = int(sys.argv[2])
		for page in range(0, count):
			page = GooglePage(query, page * 10)
			page.execute()
if __name__ == "__main__":
	main()



