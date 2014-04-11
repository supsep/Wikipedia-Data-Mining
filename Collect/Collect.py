from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

import urllib2
import re
import sys


## SEPEHR TAHERI SENG 474 DATA MINING 
## THIS USES HTML PARSER + URLIB 
## TO ACQUIRE THE CONTESTANTS TABLE FROM EACH BACHELOR(ETTE) SEASON


readmode = 0
foundinfo = False
tablecount = 0

states = { 'Alaska', 'Alabama','Arkansas','American Samoa','Arizona',  'California','Colorado','Connecticut','District of Columbia','Delaware','Florida','Georgia','Guam',
'Hawaii','Iowa','Idaho','Illinois','Indiana',	'Kansas','Kentucky','Louisiana','Massachusetts','Maryland','Maine','Michigan','Minnesota','Missouri','Mississippi','Montana','National', 'North Carolina','North Dakota', 'Nebraska','New Hampshire','New Jersey','New Mexico','Nevada','New York',
'Ohio','Oklahoma','Oregon','Pennsylvania','Puerto Rico','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Virginia','Virgin Islands','Vermont','Washington','Wisconsin','West Virginia','Wyoming','Alberta','British Columbia','Ontario','England','Brazil','Venezuela',' Veteran',' Cheerleader', 'Gas Consultant',' aide','White House','Pernambuco'
,' Medical Marketing Rep.',' Charity Ac','NHL',' Ice Girl'}


# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
    	global readmode, foundinfo, tablecount
    	if(readmode > 1 & foundinfo == False):
	    	if(tag == 'table'):
		        print "STARTTAG:", tag
		        if (tablecount > 0): foundinfo = True
		        tablecount =+ 1
		        for attr in attrs:
		        	if(attr[0] == 'class'):
		        		if(attr[1] == 'wikitable'):
		                	 print "     attr:", attr

    def handle_endtag(self, tag):
    	global readmode, foundinfo, tablecount
    	if(readmode > 1 & foundinfo == False):
	    	if(tag == 'table'):
	    		
	        	print "ENDTAG:", tag

    def handle_data(self, data):
    	global readmode, foundinfo, tablecount, states
    	if "Contestants" in data: readmode += 1
	if(readmode > 1 & foundinfo == False):
		if (re.search('[a-zA-Z]+|[2-9][0-9]+',data)):  ##CRUCIAL SEARCH - REMOVES UNWANTED DATA
			if(tablecount > 0):
 				if any(data in s for s in states):
 					print "%",data
 				else:
 					print data	


#    def handle_comment(self, data):
 #       print "Comment  :", data

## FOR EACH BACHELOR SEASON
for seasons in xrange(9,19):
	readmode = 0
	foundinfo = False	
	tablecount = 0
	url = "http://en.wikipedia.org/wiki/The_Bachelor_(season_%d)" %seasons
	print "NEW_SEASON_BEGINS" +url
	f = urllib2.urlopen(url)
	html = f.read()
	# instantiate the parser and fed it some HTML
	parser = MyHTMLParser()
	parser.feed(html)
	#url.replace("9","%d" % seasons

## FOR EACH BACHELORETTE SEASON
for seasons in xrange(4,11):
	readmode = 0
	foundinfo = False	
	tablecount = 0
	url = "http://en.wikipedia.org/wiki/The_Bachelorette_(season_%d)" %seasons
	print "NEW_SEASON_BEGINS" +url
	f = urllib2.urlopen(url)
	html = f.read()
	# instantiate the parser and fed it some HTML
	parser = MyHTMLParser()
	parser.feed(html)
	#url.replace("9","%d" % seasons



