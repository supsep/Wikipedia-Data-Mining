import re
## SEPEHR TAHERI - SENG 474 DATA MINING BACHELOR
## THIS NORMALIZES EACH HOMETOWN FROM ABBREVATIONS AND ELSE TO CITY NAME - STATE ABBREVIATION
## 

## MAP FOR STATES + ABBREVIATIONS
states = { 'AK': 'Alaska', 'AL': 'Alabama', 'AR': 'Arkansas', 'AS': 'American Samoa',     
    'AZ': 'Arizona', 'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 
    'DC': 'District of Columbia', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia',     
        'GU': 'Guam', 'HI': 'Hawaii', 'IA': 'Iowa', 'ID': 'Idaho', 'IL': 'Illinois',
        'IN': 'Indiana', 'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana',      
   'MA': 'Massachusetts', 'MD': 'Maryland', 'ME': 'Maine', 'MI': 'Michigan',     
       'MN': 'Minnesota', 'MO': 'Missouri', 'MP': 'Northern Mariana Islands',      
  'MS': 'Mississippi', 'MT': 'Montana', 'NA': 'National', 'NC': 'North Carolina',   
        'ND': 'North Dakota', 'NE': 'Nebraska', 'NH': 'New Hampshire',       
          'NJ': 'New Jersey', 'NM': 'New Mexico', 'NV': 'Nevada', 'NY': 'New York', 
          'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 
          'PA': 'Pennsylvania', 'PR': 'Puerto Rico', 'RI': 'Rhode Island',    
       'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee',    
            'TX': 'Texas', 'UT': 'Utah', 'VA': 'Virginia',        
     'VI': 'Virgin Islands', 'VT': 'Vermont', 'WA': 'Washington',  
            'WI': 'Wisconsin', 'WV': 'West Virginia', 'WY': 'Wyoming' }

provinces = {'Alberta','BritishColumbia','Ontario'}

europa = {'England','Italy'}

other = ['Brazil','Venezuela']

USWest = {'Alaska', 'Arizona', 'Colorado', 'Hawaii','Idaho','Montana','NewMexico','Nevada','Oregon','Utah','Washington','Wyoming'}

USMidWest ={'Iowa','Illinois','Indiana','Kansas','Michigan','Minnesota','Missouri','North Dakota','Nebraska','Ohio','South Dakota','Wisconsin'}

USSouth = {'Alabama','Arkansas','Delaware','Florida','Georgia','Kentucky','Louisiana','Maryland','Mississippi','North Carolina','Oklahoma','South Carolina',
'Tennessee','Texas','Virginia','West Virginia'}

USMetro = {'Connecticut','Massachusetts','Maine','New Hampshire','New Jersey','New York','Pennsylvania','Rhode Island','Vermont'}

f = open("bachelorFIXED.csv", "w");
with open("all.csv") as infile:
    for line in infile:
		temp = line
		for i in range(len(states.values())):	  
					check ='_'+states.keys()[i]      
					if check in line:
						state = states.values()[i]
						state = "_"+state
						temp = re.sub(check,state, line)
						print 'check:  ' +check  
						print 'replace :' + states.values()[i]
						print temp
		f.write(temp)



			
