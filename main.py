from tkinter import *
import random

root = Tk()

root.iconbitmap(r'images/rock.ico')
root.title("Rock | Paper | Scissor")
root.resizable(width=False,height=False)

click = True


rock_HandPhoto = PhotoImage(file=r'images/rock_hand.png')
paper_HandPhoto = PhotoImage(file=r'images/paper_hand.png')				#hand photos
scissor_HandPhoto = PhotoImage(file=r'images/scissor_hand.png')

rockPhoto = PhotoImage(file=r'images/rock.png') 
paperPhoto = PhotoImage(file=r'images/paper.png')		#element photo
scissorPhoto = PhotoImage(file=r'images/scissors.png')



winPhoto = PhotoImage(file=r'images/win.png')
losePhoto = PhotoImage(file=r'images/lose.png')		#result photo
tiePhoto = PhotoImage(file=r'images/tie.png')


rock_HandButton = ''
paper_HandButton = ''
scissor_HandButton = ''

def start():

	global rock_HandButton,paper_HandButton,scissor_HandButton

	rock_HandButton = Button(root,image=rock_HandPhoto,command=lambda:user_pick('rock'), bg = 'white')

	paper_HandButton = Button(root,image=paper_HandPhoto,command = lambda:user_pick('paper'), bg = 'white')

	scissor_HandButton = Button(root,image=scissor_HandPhoto,command =lambda:user_pick('scissors'), bg = 'white')


	rock_HandButton.grid(row = 0, column =0) 
	paper_HandButton.grid(row = 0, column =1)
	scissor_HandButton.grid(row = 0, column =2)



 


def pc_pick():

	choice = random.choice(['rock','paper','scissors'])

	return choice


def user_pick(user_choice):

	global click

	pcpick = pc_pick()

	if click ==True:

		if user_choice == 'rock':										#
			rock_HandButton.configure(image = rockPhoto, bg ='#1aff1a')				#				
																		#	
			if  pcpick == 'rock':
				paper_HandButton.configure(image = rockPhoto, bg = '#ff1a1a')
				scissor_HandButton.configure(image = tiePhoto)
				click = False
																		# if you choses Rock
			elif pcpick == 'paper':
				paper_HandButton.configure(image = paperPhoto, bg = '#ff1a1a')
				scissor_HandButton.configure(image = losePhoto)
				click = False
																			#
			else:															#	
				paper_HandButton.configure(image = scissorPhoto, bg = '#ff1a1a')			#	
				scissor_HandButton.configure(image = winPhoto)
				click = False




		elif user_choice == 'paper':
			paper_HandButton.configure(image = paperPhoto, bg ='#1aff1a')				#
																			#	
			if  pcpick == 'rock':											#	
				rock_HandButton.configure(image = rockPhoto,bg = '#ff1a1a')				#
				scissor_HandButton.configure(image = winPhoto)
				click = False
																			# if you choses Paper
			elif pcpick == 'paper':
				rock_HandButton.configure(image = paperPhoto, bg = '#ff1a1a')
				scissor_HandButton.configure(image = tiePhoto)
				click = False

			else:															#	
				rock_HandButton.configure(image = scissorPhoto, bg = '#ff1a1a')				#
				scissor_HandButton.configure(image = losePhoto)				#
				click = False												#



		
		elif user_choice == 'scissors':										#
			scissor_HandButton.configure(image = scissorPhoto, bg ='#1aff1a')				#
																			#	
			if  pcpick == 'rock':				
				paper_HandButton.configure(image = rockPhoto, bg = '#ff1a1a')
				rock_HandButton.configure(image = losePhoto)
				click = False
																			# if you choses Scissor
			elif pcpick == 'paper':
				paper_HandButton.configure(image = paperPhoto, bg = '#ff1a1a')
				rock_HandButton.configure(image = winPhoto)
				click = False

			else:															#	
				paper_HandButton.configure(image = scissorPhoto, bg = '#ff1a1a')			#	
				rock_HandButton.configure(image = tiePhoto)					#	
				click = False												#
				
		
	else:
		if 	user_choice == 'rock' or user_choice == 'paper' or user_choice == 'scissors':

			rock_HandButton.configure(image = rock_HandPhoto, bg = 'white')
			paper_HandButton.configure(image	= paper_HandPhoto, bg = 'white')
			scissor_HandButton.configure(image	= scissor_HandPhoto, bg ='white')

			click	= True	




start()



root.mainloop()