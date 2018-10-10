#! python3
# asdfParser.py - Script that gets information from user and adds it into a relevant
# asdf file.
# Author: Atli Freyr Magnússon - atlifreyr94@gmail.com
# Version: 0.01
# Created: 26-09-2018
# Last updated: 


import asdf
import numpy as np
import datetime
import os
import re

saltNameCap = input('What salt mixture are you working with, ex: FLiBe: ')
saltName = saltNameCap.lower()
fileList = os.listdir()
fileList = list(map(lambda x: x.rstrip('.asdf').lower(),fileList))

if saltName in fileList:
    print('Opening file ' + saltNameCap + '.asdf')
    dataFile = asdf.open(saltNameCap + '.asdf')
else:
    create = input('Mixture does not exist in database, would like to create a new asdf file?, Y or N: ')
    if create.lower().startswith('y'):
        print('The file ' + saltNameCap + '.asdf will be created upon a successfull run')
        #TODO: Create a barebones structure of an asdf file with the corresponding name
    else:
        exit
        
        
#Function that asks the user for citing materials
def getReference():
    #TODO add more reference items
    authors = input('List the authors, seperate with comma: ')
    year = input('Year: ')
    Reference = {
            'authors': authors,
            'year': year
    }
    return Reference

#We should ask users if their article already exists in the current database
print(dataFile['metadata']['List of references'])    
referenceNeeded = input('Are you adding a new article?, Y or N: ')

#If yes, it should run the function that gathers citation material and then add that material to the database
if referenceNeeded.lower().startswith('y'):
    Reference = getReference()
    #TODO: Scan database for same title and author, to prevent creating duplicates.
    dataFile['metadata']['List of references'].append(Reference)

#If no, they should select the index of the article they are getting the data from since it already exists
#TODO: Add an easier way to select the correct reference if the database gets large
else:
    print(dataFile['metadata']['List of references'])
    Reference = dataFile['metadata']['List of references'][int(input('From 0, select an article where data is from: '))]    

#TODO: Program Excel functionality
print("Note, Excel functionality still in development, activating manual mode")

#Get salt composition, either from database or create a new entry

#TODO: Read new Entry
if False:
    pass

#Creating a new composition entry
else:
    composition = []
    numberOfSalts = int(input('How many different salts in mixture?: '))        #TODO: Make this automatic using Regex of the file name
    for i in range(numberOfSalts):
        presence = float(input('What is the fraction of salt ' + str(i+1)))
        composition.append(presence)
    if sum(composition) > 1.00:
        raise Exception('Sum of composition can not exceed 1')
    dataFile['data']['Composition'].append(np.array(composition))
    
    
addMoreData = True
while addMoreData:
    dataOrCorr = input('Are you adding "data" or "corrolation": ')
    validInputs = ['data', 'corrolation']
    if dataOrCorr not in validInputs:
        raise Exception('Invalid input')
    elif dataOrCorr == 'corrolation':
        a = input('Add parameter a in a*T + b: ')
        b = input('Add parameter b in a*T + b: ')
        

#TODO: Update the timestamp and Update history

#TODO: Update/Create the asdf file and close it.