#createASDF.py -- Run this file when coming accross a new paper to convert it into an .asdf file that can then be added to the library for data processing.

import datetime
import os
import asdf
import openpyxl
import numpy
from excelScrape import excelScrape

def createBib():
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
	bib = {
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
	'author': author

	}

	return bib


#Main function, handles the creation of new .asdf files
def createASDF():
	#Gather metadata for the file:
	fileName = input('Requested filename, requested format Author-Year, Ex: ross-2018: ')
	fileName = filenName.lower()
	dataSets = {}
	print('Gathering reference information and building bib')
	bib = createBib()
	notes = input('Feel like adding any notes? ')

	#Creates the first metadata file tree
	metadata = {
	'FileName': fileName,
	'dataSets': 'Empty dataset',
	'BibTex': bib,
	'notes': notes,
	'Created': datetime.datetime.now(),
	'Updated': datetime.datetime.now()
	}

	#Collecting data
	userReq = input('Start archiving data? (Y or N): ')
	if userReq.lower() == 'y':
		dataCollection = True
	else:
		print('Data collection not starting')
		dataCollection = False

	#TODO: Remove the loop, it is unecessary when excel scraping, the code in loop should not be deleted
	dataSets = {}
	dataIdx = 1
	while dataCollection:
		dataSetName = 'dataset'+str(dataIdx)
		print('Showing current file directory')
		print(os.listdir())
		dataFile = input('Which file contains the desired data (type exact filename with extension)? ')
		if dataFile.endswith('xlsx'):
			dataSetList = excelScrape(dataFile)



		userReq = input('Finished data collection? (Y or N): ')
		if userReq.lower() != 'y':
			dataCollection = False



	#Add metadata and all datasets into the main asdf tree
	metadata['datasets'] = len(dataSetList)
	print('Creating asdf file')
	print('Metadata added')
	print('Adding the datasets')
	tree = {'metadata': metadata}
	#i here is just to prevent nameclashes of the datasets
	i = 1
	for dataSet in dataSetList:
		tree['DataSet' + str(i)] = dataSet

	#Creating the asdf file and return control to main menu
	af = asdf.AsdfFile(tree)
	af.write_to(fileName + '.asdf')
	print('Asdf successfully created, returning to main menu')
	return None
