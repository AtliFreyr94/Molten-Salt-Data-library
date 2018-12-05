#createASDF.py -- Run this file when coming accross a new paper to convert it into an .asdf file that can then be added to the library for data processing.

import datetime
import os
import asdf
import shutil
from excelScrape import excelScrape

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
	return bib

def importBib():
    print('Howdy partner, function not implemented yet')
    return {}

#Main function, handles the creation of new .asdf files
def createASDF():
	#Gather metadata for the file:
	fileName = input('Requested filename, requested format Author-Year, Ex: ross-2018: ')
	fileName = fileName.lower()
	print('Gathering reference information and building bib')
	manualCheck = input('Manual input(m) or import from external file (i): ')
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
	shutil.move(fileName + '.asdf', 'Library/' + fileName + '.asdf')
	print('Asdf successfully created, returning to main menu')
	return None
