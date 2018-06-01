#Dependencies
import os
import csv
from datetime import datetime
#state abbreviations

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

#OPEN CSV FILE 
employee_data_csv = os.path.join('..','Desktop','employee_data1.csv')
#CREATE LISTS TO STORE INFO

empid = []
firstname = []
lastname = []
dates = []
SSN = []
state = []
with open(employee_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)   
    
    for row in csvreader:
        empid.append(row[0])
#name column split into 
        newname = row[1].split()
        #print('New Name: {}'.format(newname))
        firstname.append(newname[0])
        lastname.append(newname[1])
        #print (newname)

#change DOB from yyyymmdd to mmddyyyy importing datetime 
        oldformat = row[2]
        datetimeobject = datetime.strptime(oldformat,'%m/%d/%Y')
        newformat = datetimeobject.strftime('%m-%d-%Y')
        #print('New Format: {}'.format(newformat))
        newformat2 = datetimeobject.strftime('%m/%d/%Y')
        #print (newname,newformat2)
        
#hide first five numbers of SSN 
        newSSN = row[3].split("-")
        newSSN = "***-**-" + newSSN[2]
        #print (newSSN)
        print (newname,newformat2,newSSN,us_state_abbrev[row[4]])

#change state to just abbreviations 
        state.append(us_state_abbrev[row[4]])
        #newstate = [(us_state_abbrev[row[4])]
        #print (newstate)

