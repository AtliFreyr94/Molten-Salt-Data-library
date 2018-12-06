#main.py - This program handles the main menu of directly changing the data library
#It does so by handling function calls to other files that actually manipulate the data
#Think of asdf files as the paper that dataprocessors can work with
#Current features are:
# Create a new asdf file for the data library, for new papers that haven't been added to library
# Update a current asdf file by adding a new dataset or removing a dataset if mistakes were made
# Delete an asdf file from the library, only use if paper is faulty
import createASDF
import updateASDF


onSwitch = True
while onSwitch:
	userRequest = input('Do you want to create (C), update (U), delete (D), view (V) or exit (X): ')
	if userRequest.lower() == 'c':
		while True:
			createASDF.createASDF()
			stopCreate = input('Stop creating files? (y or n): ')
			if stopCreate == 'y':
				break
	elif userRequest.lower() == 'u':
		updateASDF.updateASDF()
	elif userRequest.lower() == 'd':
		pass
	elif userRequest.lower() == 'v':
		pass
	elif userRequest.lower() == 'x':
		onSwitch = False
	else:
		print ('Unidentified input, please try again')
