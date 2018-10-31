#createASDF.py -- Run this file when coming accross a new paper to convert it into an .asdf file that can then be added to the library for data processing.

import datetime
import os
import asdf
import openpyxl
import numpy
from excelScrape import excelScrape

def createBib():
	#Gets reference information from user and outputs it in BibTex ready format
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


def createASDF():
	#Gather metadata:
	fileName = input('Requested filename, requested format Author-Year, Ex: Ross-2018: ')
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



	#Create and close the asdf file
	metadata['datasets'] = len(dataSetList)
	print('Creating asdf file')
	print('Metadata added')
	print('Adding the datasets')
	tree = {'metadata': metadata}
	i = 1
	for dataSet in dataSetList:
		tree['DataSet' + str(i)] = dataSet
	print('Asdf successfully created, returning to main menu')
	af = asdf.AsdfFile(tree)
	af.write_to(fileName + '.asdf')
	#go back to main program
