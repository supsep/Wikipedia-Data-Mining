## SEPEHR TAHERI - SENG 474 DATA MINING BACHELOR
## THIS TAKES A CONTESTANTS HOMETOWN AND
## CLASSIFIES IT INTO CLASSES BASED ON LOCATION
## AFTER BEING NORMALIZED 

import re

provinces = ['Alberta','BritishColumbia','Ontario','Nelson','Campbell','Canada','Quebec','Edmonton','Sarnia','Toronto']

europa = ['England','Italy']

other = ['Brazil','Venezuela']

USWest = ['CostaMesa','Berkeley', 'Beverly', 'Alaska', 'Arizona', 'Colorado', 'Hawaii','Idaho','Montana','New Mexico','Nevada','Oregon','Utah','Washington','Wyoming','California']
 
USMidWest =['Iowa','Illinois','Indiana','Kansas','Michigan','Minnesota','Missouri','NorthDakota','Nebraska','Ohio','SouthDakota','Wisconsin','Cuyahoga']

USSouth = ['Alabama','Arkansas','Delaware','Florida','Georgia','Kentucky','Louisiana','Maryland','Mississippi','NorthCarolina','Oklahoma','SouthCarolina',
'Tennessee','Texas','Virginia','WestVirginia','South Carolina','North Carolina','Dallas','PalmHarbor']

USMetro = ['Connecticut','Massachusetts','Maine','NewHampshire','NewJersey','NewYork','Pennsylvania','RhodeIsland','Vermont','New York','New Jersey','Rhode','Hampshire']

## NUMBERED LOCATIONS: 
## NONE 0  - CONTROL
## US WEST 1
## US MIDWEST 2
## US SOUTH 3
## US METRO 4
## EUROPE 5
## CANADA 6
## WORLD 7
q = open("final.csv", "w"); ## FINAL IS CREATED WITHIN EXCEL
with open("bachelorFIXED.csv") as infile:
  for line in infile:
	region = 0
	temp = line
	final = ''
	start = 0
	end = 0
	count = 0
	for i in range(2):
		if other[i] in line:
			region = 7
	for i in range(2):
		if europa[i] in line:
			region = 5
	for i in range(10):
		if provinces[i] in line:
			region = 6
	for i in range(16):
		if USWest[i] in line:
			region = 1
	for i in range(13):
		if USMidWest[i] in line:
			region = 2
	for i in range(20):
		if USSouth[i] in line:
			region = 3
	for i in range(13):
		if USMetro[i] in line:
			region = 4


	if region == 0:
		print "PROBLEM" +line

	temp = line.split(',')
	temp[4] = region
	for i in range(len(temp)):
		final = final +str(temp[i])
		if i < 9:
			final = final +','
	q.write(final)




