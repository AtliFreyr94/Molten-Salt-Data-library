#main.py - Use this program to traverse the data library
#It as the function to manipulate .asdf files in the library directly and also view it's contents in a user friendly way
import createASDF
import asdf

onSwitch = True
while onSwitch:
	userRequest = input('Do you wish to create (C), update (U), delete (D), view (V) or exit (X): ')
	if userRequest.lower() == 'c':
		createASDF.createASDF()
	elif userRequest.lower() == 'u':
		pass
	elif userRequest.lower() == 'd':
		pass
	elif userRequest.lower() == 'v':
		pass
	elif userRequest.lower() == 'x':
		onSwitch = False
	else:
		print ('Unidentified input, please try again')

