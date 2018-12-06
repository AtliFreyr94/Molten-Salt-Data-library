import asdf
import os
import datetime
from excelScrape import excelScrapeOneSheet

#Prints out the contents of the asdf files excluding the metadata, useful for confirming any changes
def showDataSets(af):
    print('Showing current datasets in file')
    for key in af.tree:
        if key == 'metadata' or key == 'history' or key == 'asdf_library' :
            continue
        print(key)
        for subkeys in af.tree[key]:
            print(subkeys, end='')
            print(af.tree[key][subkeys])
        print('\n \n')


def updateASDF():
    directorLoc = os.getcwd()
    os.chdir(directorLoc + '\\..\\Library')
    print(os.listdir())
    asdfFile = input('What data file do you want to manipulate: ')
    actionType = input('What do you want to do with this file \n Add dataset (A) \n Delete dataset (D) \n Add/Edit notes (N) \n Edit Bib information (E) \n')
    af = asdf.open(asdfFile)

    if actionType.lower() == 'a':
        showDataSets(af)
        newDataSetNumber = len(af.tree) - 2
        os.chdir(directorLoc + '\\..\\InputFiles')
        print(os.listdir())
        excelFile = input('What file contains the new dataset?: ')
        newDataSet = excelScrapeOneSheet(excelFile)
        af.tree['DataSet' + str(newDataSetNumber)] = newDataSet
        showDataSets(af)
        os.chdir(directorLoc + '\\..\\Library')
        af.tree['metadata']['Updated'] = datetime.datetime.now()
        af.write_to(asdfFile)
        print('Dataset successfully added, returning')

    elif actionType.lower() == 'd':
        showDataSets(af)
        dataSetNumber = input('Write the dataset number to delete (e.g. 1, 2 etc.): ')
        keyToDelete = 'DataSet' + dataSetNumber
        #Because asdf doesn't have a delete function the tree has to be recreated but simply skip the deleted dataSet
        tree = {}
        for key in af.tree:
            if key == keyToDelete:
                tree[key] = {keyToDelete: ' Deleted'}
            else:
                tree[key] = af.tree[key]
        #TODO: Reorder the datasets
        af = asdf.AsdfFile(tree)
        showDataSets(af)

        showDataSets(af)
        confirmation = input('Confirm (y or n): ')
        if confirmation.lower() == 'y':
            af.tree['metadata']['Updated'] = datetime.datetime.now()
            af.write_to(asdfFile)
            print('Deletion successful, returning')
        else:
            print('Deletion not performed, returning')
    elif actionType.lower() == 'n':
        pass
    elif actionType.lower() == 'e':
        oldBib = af.tree['metadata']['Bib']
        print(oldBib)
        #TODO: Break bib string into dict
        bibEditing = True
        while bibEditing:
            keyToEdit = input('Type the key to edit: ')
            newValue = input('What is the value associated to the bib key?: ')
            af.tree['metadata']['Bib'][keyToEdit] = newValue
            moreKeys = input('Edit more keys? (y or n): ')
            if moreKeys.lower() == 'n':
                bibEditing = False
            else:
                continue
        newBib = af.tree['metadata']['Bib']
        print(newBib)
        continueBib = input('Confirm (y or n): ')
        if continueBib.lower() == 'y':
            af.write_to(asdfFile)
            print('Edit successfull, returning')
        else:
            print('Changes not implemented, returning')
    else:
        print('Invalid selection, returning to menu')


    os.chdir(directorLoc)
    return None
