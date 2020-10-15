import textract
import csv
#import pandas as pd

#bring in data
file = '/Users/scot/Desktop/OfficialNotification.pdf'
#turn this into a monthly query of this page or something:
USPS = 'https://www.forfeiture.gov/pdf/USPS/OfficialNotification.pdf'
CBP = 'https://www.forfeiture.gov/pdf/CBP/OfficialNotification.pdf'

text = str(textract.process(file))

def GetDeadline(text):
    key_phrase = 'DEADLINE TO FILE A CLAIM:'
    phrase_index = text.find('DEADLINE TO FILE A CLAIM:')
    return text[phrase_index + len(key_phrase): phrase_index + text[phrase_index:].find('\\n')].strip()

#2020319500061101-0001-0000, Seized on 07/08/2020; At the port of FED EXP,ANCHORAGE,AK; Pocket Intel PC; 80; EA; Valued at $9,168.00; For violation of 19 USC 1526(e)

#id -- date_seized -- port -- item -- quantity -- type -- value -- violation_of

# get string for determining where data starts
deadline = GetDeadline(text)

#the rest of this will pretty much just be data cleaining:

columns = ['id', 'date_seized', 'port', 'item', 'quantity', 'type', 'value', 'violation']
#initialize dataframe:
forfeiture_db = pd.DataFrame(columns = columns)

dest_file = '/Users/scot/Desktop/CBP.csv'
with open(dest_file, 'w') as CBP:
    
