import re
## SEPEHR TAHERI SENG 474 DATA MINING 
## THIS IS THE FINAL STAGE - THIS REMOVES DISCRPENCIES & FALSE DATA 
#$  FROM THE CSV FILE
prevLine = ''
edCount = 0
f = open("out4.txt", "w");
with open("out3.txt") as infile: ## EACH LINE - CHECK IF IT HAS DISCRPENCIES
    for line in infile:
    	if "Cosetta" in line:
    		f.write(line+"21\n ")
    	elif " Charity Accountant" in line:
    		continue
    	elif ", New York" in line:
    		continue
    	elif "New York"	in prevLine and "New York" in line:
    		continue
    	elif "Swiderski" in line:
    		edCount += 1
    		if edCount > 1:
    				line = line + '29 \n Monroe, MI \n Technology Consultant\n'
    		f.write(line)
    	else:
    		f.write(line)
    	prevLine = line	
