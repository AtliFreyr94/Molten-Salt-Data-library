#createASDF.py -- Run this file when coming accross a new paper to convert it into an .asdf file that can then be added to the library for data processing.

import datetime
import os
import asdf
import shutil
from excelScrape import excelScrape
import sys

def createBib(fileName):

    #TODO: Other type of BibTex entries than just article

	#Gets reference information from user and outputs it in BibTex ready format

	#Get user input
	print('Please fill out the following information')
	title = input('Title: ')
	language = input('language: ')
	publisher = input('publisher: ')
	journal = input('journal: ')
	volume = input('volume: ')
	number = input('number: ')
	pages = input('pages: ')
	year = input('year: ')
	issn = input('issn: ')
	doi = input('doi: ')
	abstract = input('Copy and paste the abstract: ')
	author = input('author: ')

	#Create a bib ready object from user input
	bibDict = {
	'title': title,
	'language': language,
	'publisher': publisher,
	'journal': journal,
	'volume': volume,
	'number': number,
	'pages': pages,
	'year': year,
	'issn': issn,
	'doi': doi,
	'author': author,
    'abstract': abstract

	}

    #Assuming Article format now we join all bib info into a string with correct format for LaTeX
	bibList = ['@article{' + fileName + ',']
	for key in bibDict:
	    bibList.append(key + ' = {' + bibDict[key] + '},')
	bibList[-1] = '}'
	bib = '\n'.join(bibList)
	print(bib)
	return bib

#Function asks user for a file containing the bib information and then prints it out to ask for confirmation
def importBib():
    print(os.listdir())
    bibFileName = input('Which file contains the bib information (exact name with file extension): ')
    bibFile = open(bibFileName)
    bib = bibFile.read()
    bibFile.close()
    print(bib)
    confirmBib = input('Is this bib format correct? (y or n): ')
    if confirmBib.lower() == 'n':
        print('Fix bib file and try again, process exiting')
        sys.exit()
    else:
        return bib

#Main function, handles the creation of new .asdf files
def createASDF():
	#Gather metadata for the file:
	directorLoc = os.getcwd()
	fileName = input('Requested filename, requested format Author-Year, Ex: ross-2018: ')
	fileName = fileName.lower()
	print('Gathering reference information and building bib')
	manualCheck = input('Manual input(m) or import from external file (i): ')
	os.chdir(directorLoc + '\\..\\InputFiles')
	if manualCheck.lower() == 'm':
	    bib = createBib(fileName)
	else:
	    bib = importBib()
	notes = input('Feel like adding any comments to metadata? ')

	#Creates the first metadata file tree
	metadata = {
	'FileName': fileName,
	'dataSets': 'Empty dataset',
	'Bib': bib,
	'notes': notes,
	'Created': datetime.datetime.now(),
	'Updated': datetime.datetime.now()
	}

	#Collecting data
	print('Data collector starting')
	print('Showing current file directory')
	print(os.listdir())
	dataFile = input('Which file contains the desired data (type exact filename with extension)? ')
	if dataFile.endswith('xlsx'):
		dataSetList = excelScrape(dataFile)


	#Add metadata and all datasets into the main asdf tree
	metadata['dataSets'] = len(dataSetList)
	os.chdir(directorLoc + '\\..\\Library')
	print('Creating asdf file')
	print('Metadata added')
	print('Adding the datasets')
	tree = {'metadata': metadata}
	#i here is just to prevent nameclashes of the datasets
	i = 1
	for dataSet in dataSetList:
		tree['DataSet' + str(i)] = dataSet
		i += 1

	#Creating the asdf file and return control to main menu
	af = asdf.AsdfFile(tree)
	af.write_to(fileName + '.asdf')
	os.chdir(directorLoc)
	print('Asdf successfully created, returning to main menu')
	return None
