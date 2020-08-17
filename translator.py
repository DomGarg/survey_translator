## By Dominic Gargala
## August 13, 2020

from docx import Document
from bs4 import BeautifulSoup
import csv
import os
import numpy as np
import re

engtrans = [] #List to hold all cells of desired column to be translated
eng = [] #List to hold all cells of all columns/rows
engword = {} #Dictionary to store key/value pairs from word document table. Key is in English, value is in French.


## Opening word document to fill dictionary with key/values

wordDoc = Document('/Users/domgarg/Documents/WORK/HCW Survey Translation copy.docx')
for table in wordDoc.tables:
    for row in table.rows:
        temp = ''
        for cell in row.cells:
            if temp != '':
                engword[temp] = cell.text
            else:
                temp = cell.text
                
## Opening CSV's to read and written to

with open('PandemicHCWCopy_DataDictionary_2020-08-11 copy.csv', 'r') as rf:
    reader = csv.reader(rf, delimiter=',')
    with open('PandemicHCWCopy_DsataDictionary_2020-08-11 copy 22.csv','w') as fw:
        cw = csv.writer(fw)
        for row in reader:  
            engtrans.append(row[4]) 
            eng.append(row)

## Algorithm to loop through desired rows, parse the HTML from strings and then replace the English strings 
## with French strings using dictionary. Then write the new row into the output CSV.

        for row in eng:
            for i in range(17):
                if row[i] in engtrans and row[i] != '':
                    #row[i] = engword.get(row[i])
                    tag_str = row[i]
                    regex = re.compile('<[\w\W]+\>(.+)<\/\w+>')
                    match = regex.match(tag_str)  # This returns a list of all matches
                    #if match:
                    #if match: 
                    soup = BeautifulSoup(row[i], "html.parser")
                    findtoure = soup.find_all(text=True, recursive=True)
                    #print(findtoure.encode('utf-8'))
                    findtoure = [x.strip(' ') for x in findtoure]
                    print(findtoure)
                    #print(soup)
                    #findtoure.stirng = "yessss"
                    #print(soup)
                    #soup = BeautifulSoup(match.group(), "html.parser")
                    #findtoure = soup.find_all(text=True, recursive=True)
                    #print(findtoure)
                    
                    for key, value in engword.items():
                        #print(findtoure)
                        #if match: 
                            #soup = BeautifulSoup(match.group(), "html.parser")
                            #findtoure = soup.find(text=True, recursive=True)
                            #print(key.encode('utf-8'))
                            #print(match.group())
                            #print(findtoure.encode('utf-8'))
                        for x in findtoure:
                            if key.encode('utf-8') == x.encode('utf-8'):
                                #print(match.group())
                                #print(key)
                                str_to_replace = key  # 1 index is the string in between the tags
                                tag_str.replace(str_to_replace, value)  # standard str.replace()
                                row[i] = tag_str.replace(str_to_replace, value)
            cw.writerow(row)



#print(findtoure)