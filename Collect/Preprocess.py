import re
## SEPEHR TAHERI SENG 474 DATA MINING 
## THIS EXTRACTS VALUABLE INFORMATION FROM THE HTML PARSER
## THE DATA EXTRACTED IS NOT FINAL
## 

seasonCount = 0
contestantCount = 0
attributeCount = 4

defaultSkipCount = 6
skipCount = 0
skipMode = False
inBetweenSeason = False


##THESE ARRAYS OF CONTESTANTS PER SEASONS
dataOne=[]
dataTwo=[]
dataThree=[]
dataFour=[]
dataFive=[]
dataSix=[]
dataSeven=[]
dataEight=[]
dataNine=[]
dataTen=[]                               # will hold the lines of the file
dataEl =[]
dataTw=[]
dataThi=[]
dataFourt=[]
dataFif=[]
dataSixt=[]
dataSevent=[]
dataEightt=[]
dataNineT=[]
dataTwen=[]
dataTwenone=[]
i = 0


def checkNewSeason(line):
  		if "NEW_SEASON_BEGINS" in line: 
  			return True  			
   		return False


def checkEndSeason(line):
	if "ENDTAG: table" in line:
		return True
	return False

def getBlankArray(count):
	count += 1
	smap = {1: dataOne,
            2: dataTwo,
            3: dataThree,
            4: dataFour,
            5: dataFive,
            6: dataSix,
            7: dataSeven,
            8: dataEight,
            9: dataNine,
            10: dataTen,
            11: dataEl,
            12: dataTw,
            13: dataThi,
            14: dataFourt,
            15: dataFif,           
            16: dataSixt,
            17: dataSevent,            
            18: dataEightt,
            19: dataNineT,            
            20: dataTen,
            21: dataTwenone  }          
    	return smap[count]
def checkCountry(line):
		if '%' in line :
	  	   		return True
		return False


currentData = getBlankArray(seasonCount)
with open("out3.txt") as infile:
    contestantBuffer = []
    for line in infile:

    	if inBetweenSeason:
    		print "IN BETWEEN SEASONS!", inBetweenSeason
    		if checkNewSeason(line):
    			skipCount = defaultSkipCount
    			inBetweenSeason = False
    			contestantCount = 0
    			continue
    		else:	
    			continue
    	else:		
	    	if skipCount > 0:
	    		skipCount -= 1
	    		continue
	    	elif checkNewSeason(line):
	    		skipCount = defaultSkipCount
	    		print "NEWSEASON", seasonCount+8
	    		continue
	    	elif checkEndSeason(line):
	    		seasonCount += 1
	    		if seasonCount > 9:
	    			defaultSkipCount = 7
	    		print currentData
	    		currentData = getBlankArray(seasonCount)
	    		inBetweenSeason = True
	    		continue
	    	elif checkCountry(line):
	    		cityStateBuffer = ' '
	    		cityStateBuffer = cityStateBuffer + cityStateBuffer2 + line
	    		cityStateBuffer = cityStateBuffer.replace("\n", "")
	    		cityStateBuffer = cityStateBuffer.replace("%", ",")
	    		if len(contestantBuffer) > 2:
	    			contestantBuffer[2] = cityStateBuffer
	    		continue
	    	else:
		    	if re.search("(?<!\d)\d{2}(?!\d)",line) and len(contestantBuffer) > 1:
						contestantBuffer[1] = line.replace("\n", "")
			elif  "Note" in line:
					continue
		    	elif attributeCount > 3:
		    			attributeCount = 0
		    			contestantCount += 1
		    			currentData.append(contestantBuffer)
		    			contestantBuffer=[]
		    			contestantBuffer.append((line.replace("\n", "")))
		    			#print "contestant", line
		    	else:
		    			attributeCount += 1
		    			cityStateBuffer2 = line
		    			#print "attribute", line
		    			contestantBuffer.append((line.replace("\n", "")))